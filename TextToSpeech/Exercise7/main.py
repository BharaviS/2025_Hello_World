import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import os
import tempfile

import pyttsx3
from pydub import AudioSegment
import simpleaudio as sa

AUDIO_PATH = os.path.join(tempfile.gettempdir(), "prompt_reader_audio.wav")

# --- TTS engine (offline) ---
engine = pyttsx3.init()
# Default to voices[1] if available; you can change via dropdown in UI
try:
    voices = engine.getProperty("voices")
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)
except Exception:
    voices = []

def format_time_ms(ms: int) -> str:
    if ms < 0: ms = 0
    s = ms // 1000
    m, s = divmod(s, 60)
    return f"{m:02d}:{s:02d}"

def safe_remove(path: str):
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass

def apply_speed(seg: AudioSegment, rate: float) -> AudioSegment:
    """
    Speed up (or slow down) by changing the frame_rate then resetting to original.
    This changes tempo and pitch (simple/fast method).
    rate=1.5 -> ~1.5x speed.
    """
    if rate <= 0:
        rate = 1.0
    return seg._spawn(seg.raw_data, overrides={
        "frame_rate": int(seg.frame_rate * rate)
    }).set_frame_rate(seg.frame_rate)

class PromptReaderApp:
    def __init__(self, root):
        self.root = root
        root.title("Prompt Reader — Major Siri (pydub)")
        root.geometry("860x560")

        # Text area
        self.text = tk.Text(root, wrap="word", font=("Arial", 12))
        self.text.pack(expand=True, fill="both", padx=10, pady=(10,6))

        # Controls
        controls = tk.Frame(root)
        controls.pack(fill="x", padx=10, pady=(0,10))

        self.play_btn = tk.Button(controls, text="Play ▶", width=10, command=self.on_play)
        self.pause_btn = tk.Button(controls, text="Pause ⏸", width=10, command=self.on_pause, state="disabled")
        self.stop_btn = tk.Button(controls, text="Stop ■", width=10, command=self.on_stop, state="disabled")
        self.back_btn = tk.Button(controls, text="⏪ 5s", width=7, command=lambda: self.seek(-5000), state="disabled")
        self.forward_btn = tk.Button(controls, text="5s ⏩", width=7, command=lambda: self.seek(5000), state="disabled")
        self.load_btn = tk.Button(controls, text="Load .txt", width=10, command=self.load_txt)

        self.play_btn.pack(side="left", padx=6)
        self.pause_btn.pack(side="left", padx=6)
        self.stop_btn.pack(side="left", padx=6)
        self.back_btn.pack(side="left", padx=6)
        self.forward_btn.pack(side="left", padx=6)
        self.load_btn.pack(side="right", padx=6)

        # Voice selection
        left_box = tk.Frame(root)
        left_box.pack(fill="x", padx=10, pady=(0,8))
        ttk.Label(left_box, text="Voice:").pack(side="left", padx=(0,6))
        self.voice_combo = ttk.Combobox(left_box, state="readonly", width=50)
        voice_names = []
        for i, v in enumerate(voices):
            name = getattr(v, "name", f"Voice {i}")
            vid = getattr(v, "id", "")
            voice_names.append(f"{i}: {name} ({vid[:36]})")
        self.voice_combo["values"] = voice_names
        if voice_names:
            self.voice_combo.current(1 if len(voice_names) > 1 else 0)
        self.voice_combo.bind("<<ComboboxSelected>>", self.on_voice_change)

        # Speed selection
        ttk.Label(left_box, text="   Speed:").pack(side="left", padx=(10,6))
        self.speed_var = tk.StringVar(value="1.00x")
        self.speed_combo = ttk.Combobox(left_box, state="readonly", width=8,
                                        values=["0.75x","1.00x","1.25x","1.50x","2.00x"],
                                        textvariable=self.speed_var)
        self.speed_combo.pack(side="left")
        self.speed_combo.bind("<<ComboboxSelected>>", self.on_speed_change)

        # Time / status
        status_frame = tk.Frame(root)
        status_frame.pack(fill="x", padx=10, pady=(0,8))
        self.time_label = tk.Label(status_frame, text="00:00 / 00:00")
        self.time_label.pack(side="left")
        self.status_label = tk.Label(status_frame, text="", anchor="e")
        self.status_label.pack(side="right")

        # Playback state
        self.base_seg = None            # AudioSegment (original speed)
        self.duration_ms = 0
        self.playback_offset_ms = 0     # logical position in ORIGINAL audio timeline
        self.speed_rate = 1.0

        self.is_playing = False
        self.is_paused = False
        self.play_start_walltime = None # wall clock when last (re)started
        self.play_obj: sa.PlayObject | None = None

        # UI updater
        self._poll_job = None
        self._update_poll()

    # -------- Voice / Speed ----------
    def on_voice_change(self, event=None):
        idx = self.voice_combo.current()
        try:
            engine.setProperty("voice", voices[idx].id)
        except Exception as e:
            messagebox.showwarning("Voice", f"Could not set voice:\n{e}")

    def on_speed_change(self, event=None):
        val = self.speed_var.get().replace("x","")
        try:
            rate = float(val)
        except Exception:
            rate = 1.0
        if rate <= 0: rate = 1.0
        # If playing, restart from same logical position at new speed
        was_playing = self.is_playing
        self.speed_rate = rate
        if was_playing or self.is_paused:
            self._restart_from_current_pos()

    # -------- File / TTS -------------
    def load_txt(self):
        path = filedialog.askopenfilename(filetypes=[("Text files","*.txt"), ("All files","*.*")])
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            self.text.delete("1.0", "end")
            self.text.insert("1.0", f.read())
        self.on_stop()

    def on_play(self):
        text_content = self.text.get("1.0", "end").strip()
        if not text_content:
            return messagebox.showwarning("No text", "Please enter or load some text.")
        self._ui_busy(True, "Synthesizing...")

        # stop current playback
        self._stop_playback_only()

        # TTS in background
        threading.Thread(target=self._tts_thread, args=(text_content,), daemon=True).start()

    def _tts_thread(self, text):
        try:
            safe_remove(AUDIO_PATH)
            engine.save_to_file(text, AUDIO_PATH)
            engine.runAndWait()
        except Exception as e:
            self.root.after(0, lambda: self._on_tts_error(e))
            return

        try:
            seg = AudioSegment.from_wav(AUDIO_PATH)
        except Exception as e:
            self.root.after(0, lambda: self._on_tts_error(e))
            return

        self.base_seg = seg
        self.duration_ms = len(seg)
        self.playback_offset_ms = 0

        # Start playback on main thread
        self.root.after(0, self._start_from_offset_zero)

    def _on_tts_error(self, e):
        self._ui_busy(False)
        messagebox.showerror("TTS Error", f"Failed to generate audio:\n{e}")

    # -------- Playback core ----------
    def _start_from_offset_zero(self):
        self._start_playback_from(self.playback_offset_ms)

    def _restart_from_current_pos(self):
        # Stop current and start again at same logical offset
        self._stop_playback_only()
        self._start_playback_from(self.playback_offset_ms)

    def _start_playback_from(self, offset_ms: int):
        if self.base_seg is None or self.duration_ms == 0:
            self._ui_busy(False)
            return
        # Slice from logical position (original timeline)
        offset_ms = max(0, min(offset_ms, self.duration_ms))
        seg = self.base_seg[offset_ms:]
        # Apply speed factor
        if self.speed_rate != 1.0:
            seg = apply_speed(seg, self.speed_rate)

        try:
            # simpleaudio expects raw PCM parameters
            self.play_obj = sa.play_buffer(seg.raw_data, num_channels=seg.channels,
                                           bytes_per_sample=seg.sample_width,
                                           sample_rate=seg.frame_rate)
        except Exception as e:
            self._ui_busy(False)
            return messagebox.showerror("Playback Error", str(e))

        self.playback_offset_ms = offset_ms
        self.play_start_walltime = time.time()
        self.is_playing = True
        self.is_paused = False
        self._ui_busy(False, "Playing")
        self._enable_controls(True)

    def _stop_playback_only(self):
        # Stop current simpleaudio playback if any
        try:
            if self.play_obj and self.play_obj.is_playing():
                self.play_obj.stop()
        except Exception:
            pass
        self.is_playing = False
        self.is_paused = False
        self.play_start_walltime = None

    def on_pause(self):
        if not (self.is_playing or self.is_paused):
            return
        if self.is_playing:
            # compute progress since start in original timeline
            elapsed_wall = time.time() - (self.play_start_walltime or time.time())
            progressed_ms = int(elapsed_wall * 1000 * self.speed_rate)
            self.playback_offset_ms = min(self.playback_offset_ms + progressed_ms, self.duration_ms)
            # stop playback
            self._stop_playback_only()
            self.is_paused = True
            self.is_playing = False
            self.pause_btn.config(text="Resume ▶")
            self.status_label.config(text="Paused")
        else:
            # resume from paused offset
            self._start_playback_from(self.playback_offset_ms)
            self.pause_btn.config(text="Pause ⏸")

    def on_stop(self):
        self._stop_playback_only()
        self.playback_offset_ms = 0
        self.pause_btn.config(text="Pause ⏸", state="disabled")
        self.stop_btn.config(state="disabled")
        self.back_btn.config(state="disabled")
        self.forward_btn.config(state="disabled")
        self.status_label.config(text="Stopped")
        self._update_time_label()

    def seek(self, delta_ms: int):
        if self.base_seg is None:
            return
        # If playing, compute where we are now first
        if self.is_playing:
            elapsed_wall = time.time() - (self.play_start_walltime or time.time())
            progressed_ms = int(elapsed_wall * 1000 * self.speed_rate)
            self.playback_offset_ms = min(self.playback_offset_ms + progressed_ms, self.duration_ms)
        # New logical target
        new_pos = max(0, min(self.playback_offset_ms + delta_ms, self.duration_ms))
        self.playback_offset_ms = new_pos
        if self.is_playing:
            self._restart_from_current_pos()
        else:
            # if paused/stopped, just update label
            self._update_time_label()

    # -------- UI helpers ------------
    def _ui_busy(self, busy: bool, status: str = ""):
        self.play_btn.config(state="disabled" if busy else "normal", text="Play ▶" if not busy else "Generating...")
        self.status_label.config(text=status)

    def _enable_controls(self, enabled: bool):
        state = "normal" if enabled else "disabled"
        self.pause_btn.config(state=state)
        self.stop_btn.config(state=state)
        self.back_btn.config(state=state)
        self.forward_btn.config(state=state)

    def _update_time_label(self):
        total = self.duration_ms
        cur = self.playback_offset_ms
        if self.is_playing and self.play_start_walltime:
            elapsed_wall = time.time() - self.play_start_walltime
            progressed_ms = int(elapsed_wall * 1000 * self.speed_rate)
            cur = max(0, min(self.playback_offset_ms + progressed_ms, total))
        self.time_label.config(text=f"{format_time_ms(cur)} / {format_time_ms(total)}")

    def _poll(self):
        # called periodically
        self._update_time_label()

        # detect finish
        finished = False
        try:
            if self.play_obj and not self.play_obj.is_playing() and self.is_playing:
                # It stopped by itself (reached end)
                finished = True
        except Exception:
            finished = True

        if finished:
            self.is_playing = False
            self.is_paused = False
            self.play_obj = None
            self.playback_offset_ms = 0
            self.pause_btn.config(text="Pause ⏸", state="disabled")
            self.stop_btn.config(state="disabled")
            self.back_btn.config(state="disabled")
            self.forward_btn.config(state="disabled")
            self.status_label.config(text="Finished")
            self._update_time_label()

        self._poll_job = self.root.after(150, self._poll)

    def _update_poll(self):
        self._poll()
    # --------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptReaderApp(root)
    root.mainloop()
