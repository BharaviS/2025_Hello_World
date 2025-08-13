import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
from tts_controller import TTSController

class TextToSpeechGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Reader")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize TTS controller
        self.tts_controller = TTSController()
        
        # Current state variables
        self.is_playing = False
        self.is_paused = False
        self.current_position = 0
        
        # Setup GUI
        self.setup_gui()
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_gui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame, text="Text-to-Speech Reader", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Text input area
        text_frame = ttk.LabelFrame(main_frame, text="Text to Read", padding="5")
        text_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, 
                                                  width=60, height=15,
                                                  font=("Arial", 11))
        self.text_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Sample text
        sample_text = ("Enter your text here to be read aloud. You can use the controls below to "
                      "play, pause, and navigate through the speech playback. The forward and "
                      "backward buttons will skip approximately 5 seconds of speech content.")
        self.text_area.insert("1.0", sample_text)
        
        # Controls frame
        controls_frame = ttk.LabelFrame(main_frame, text="Playback Controls", padding="10")
        controls_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Control buttons
        button_frame = ttk.Frame(controls_frame)
        button_frame.grid(row=0, column=0, columnspan=2)
        
        self.play_button = ttk.Button(button_frame, text="▶ Play", 
                                     command=self.play_text, width=12)
        self.play_button.grid(row=0, column=0, padx=5)
        
        self.pause_button = ttk.Button(button_frame, text="⏸ Pause", 
                                      command=self.pause_text, width=12,
                                      state="disabled")
        self.pause_button.grid(row=0, column=1, padx=5)
        
        self.backward_button = ttk.Button(button_frame, text="⏪ -5s", 
                                         command=self.backward_5s, width=12,
                                         state="disabled")
        self.backward_button.grid(row=0, column=2, padx=5)
        
        self.forward_button = ttk.Button(button_frame, text="⏩ +5s", 
                                        command=self.forward_5s, width=12,
                                        state="disabled")
        self.forward_button.grid(row=0, column=3, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="⏹ Stop", 
                                     command=self.stop_text, width=12,
                                     state="disabled")
        self.stop_button.grid(row=0, column=4, padx=5)
        
        # Status frame
        status_frame = ttk.Frame(controls_frame)
        status_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky=(tk.W, tk.E))
        status_frame.columnconfigure(1, weight=1)
        
        ttk.Label(status_frame, text="Status:").grid(row=0, column=0, sticky=tk.W)
        self.status_label = ttk.Label(status_frame, text="Ready", 
                                     foreground="green", font=("Arial", 10, "bold"))
        self.status_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # Progress frame
        progress_frame = ttk.Frame(controls_frame)
        progress_frame.grid(row=2, column=0, columnspan=2, pady=(5, 0), sticky=(tk.W, tk.E))
        progress_frame.columnconfigure(1, weight=1)
        
        ttk.Label(progress_frame, text="Progress:").grid(row=0, column=0, sticky=tk.W)
        self.progress_label = ttk.Label(progress_frame, text="0 / 0 words")
        self.progress_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress_bar.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="Voice Settings", padding="10")
        settings_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        # Voice rate control
        rate_frame = ttk.Frame(settings_frame)
        rate_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 20))
        
        ttk.Label(rate_frame, text="Speed:").grid(row=0, column=0, sticky=tk.W)
        self.rate_var = tk.IntVar(value=200)
        self.rate_scale = ttk.Scale(rate_frame, from_=50, to=400, 
                                   variable=self.rate_var, orient=tk.HORIZONTAL,
                                   command=self.update_rate, length=150)
        self.rate_scale.grid(row=0, column=1, padx=(10, 10))
        self.rate_label = ttk.Label(rate_frame, text="200 wpm")
        self.rate_label.grid(row=0, column=2)
        
        # Voice selection
        voice_frame = ttk.Frame(settings_frame)
        voice_frame.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(voice_frame, text="Voice:").grid(row=0, column=0, sticky=tk.W)
        self.voice_var = tk.StringVar()
        self.voice_combo = ttk.Combobox(voice_frame, textvariable=self.voice_var,
                                       state="readonly", width=20)
        self.voice_combo.grid(row=0, column=1, padx=(10, 0))
        self.voice_combo.bind('<<ComboboxSelected>>', self.update_voice)
        
        # Initialize voice list
        self.load_voices()
    
    def load_voices(self):
        """Load available voices into the combobox"""
        try:
            voices = self.tts_controller.get_voices()
            voice_names = [voice['name'] for voice in voices]
            self.voice_combo['values'] = voice_names
            if voice_names:
                self.voice_combo.set(voice_names[0])
                self.tts_controller.set_voice(voices[0]['id'])
        except Exception as e:
            print(f"Error loading voices: {e}")
            self.voice_combo['values'] = ["Default Voice"]
            self.voice_combo.set("Default Voice")
    
    def update_rate(self, value=None):
        """Update speech rate"""
        rate = int(self.rate_var.get())
        self.rate_label.config(text=f"{rate} wpm")
        self.tts_controller.set_rate(rate)
    
    def update_voice(self, event=None):
        """Update selected voice"""
        try:
            voices = self.tts_controller.get_voices()
            selected_name = self.voice_var.get()
            for voice in voices:
                if voice['name'] == selected_name:
                    self.tts_controller.set_voice(voice['id'])
                    break
        except Exception as e:
            print(f"Error updating voice: {e}")
    
    def update_status(self, status, color="black"):
        """Update status label"""
        self.status_label.config(text=status, foreground=color)
    
    def update_progress(self, current_word, total_words):
        """Update progress display"""
        self.progress_label.config(text=f"{current_word} / {total_words} words")
        if total_words > 0:
            progress = (current_word / total_words) * 100
            self.progress_bar['value'] = progress
    
    def update_button_states(self, playing=False, paused=False):
        """Update button states based on playback status"""
        if playing and not paused:
            self.play_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")
            self.backward_button.config(state="normal")
            self.forward_button.config(state="normal")
        elif paused:
            self.play_button.config(state="normal", text="▶ Resume")
            self.pause_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.backward_button.config(state="normal")
            self.forward_button.config(state="normal")
        else:
            self.play_button.config(state="normal", text="▶ Play")
            self.pause_button.config(state="disabled")
            self.stop_button.config(state="disabled")
            self.backward_button.config(state="disabled")
            self.forward_button.config(state="disabled")
    
    def play_text(self):
        """Start or resume text playback"""
        text = self.text_area.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to read.")
            return
        
        if self.is_paused:
            # Resume from pause
            self.is_paused = False
            self.is_playing = True
            self.update_status("Playing...", "green")
            self.update_button_states(playing=True)
            self.tts_controller.resume()
        else:
            # Start new playback
            self.is_playing = True
            self.is_paused = False
            self.current_position = 0
            self.update_status("Playing...", "green")
            self.update_button_states(playing=True)
            
            # Start playback in separate thread
            threading.Thread(target=self._play_text_thread, args=(text,), daemon=True).start()
    
    def _play_text_thread(self, text):
        """Thread function for text playback"""
        try:
            def progress_callback(current_word, total_words):
                self.root.after(0, self.update_progress, current_word, total_words)
                self.current_position = current_word
            
            def finished_callback():
                self.root.after(0, self._playback_finished)
            
            self.tts_controller.speak_text(text, progress_callback, finished_callback)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Playback error: {str(e)}"))
            self.root.after(0, self._playback_finished)
    
    def _playback_finished(self):
        """Handle playback completion"""
        self.is_playing = False
        self.is_paused = False
        self.current_position = 0
        self.update_status("Ready", "green")
        self.update_button_states()
        self.progress_bar['value'] = 0
        self.update_progress(0, 0)
    
    def pause_text(self):
        """Pause text playback"""
        if self.is_playing:
            self.is_paused = True
            self.is_playing = False
            self.update_status("Paused", "orange")
            self.update_button_states(paused=True)
            self.tts_controller.pause()
    
    def stop_text(self):
        """Stop text playback"""
        self.tts_controller.stop()
        self._playback_finished()
    
    def forward_5s(self):
        """Skip forward approximately 5 seconds"""
        if hasattr(self.tts_controller, 'skip_forward'):
            self.tts_controller.skip_forward()
            self.update_status("Skipped forward", "blue")
            # Reset status after 1 second
            self.root.after(1000, lambda: self.update_status("Playing...", "green") if self.is_playing else None)
    
    def backward_5s(self):
        """Skip backward approximately 5 seconds"""
        if hasattr(self.tts_controller, 'skip_backward'):
            self.tts_controller.skip_backward()
            self.update_status("Skipped backward", "blue")
            # Reset status after 1 second
            self.root.after(1000, lambda: self.update_status("Playing...", "green") if self.is_playing else None)
    
    def on_closing(self):
        """Handle window closing"""
        try:
            self.tts_controller.stop()
            self.tts_controller.cleanup()
        except:
            pass
        self.root.destroy()

def main():
    root = tk.Tk()
    app = TextToSpeechGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
