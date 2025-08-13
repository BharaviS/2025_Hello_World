import tkinter as tk
import pyttsx3

class PromptReader:
    def __init__(self, audio) -> None:
        self.__audio = audio

    @property
    def speak(self) -> None:
        try:
            engine = pyttsx3.init()

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 130)
            engine.setProperty('volume', 1)

            engine.say(self.__audio)
            engine.runAndWait()

            return self.__audio
        except Exception as e:
            print(e)

root = tk.Tk()
root.geometry('800x520')
root.title('Prompt Reader')

text = tk.Text(root, wrap="word", font=("Arial", 12))
text.pack(expand=True, fill="both", padx=10, pady=(10, 6))

controls = tk.Frame(root)
controls.pack(fill="x", padx=10, pady=(0, 10))

def on_play():
    try:
        audio = text.get("1.0", tk.END)
        prompt = PromptReader(audio).speak
        print(prompt)
    except Exception as e:
        print(e)

play_btn = tk.Button(controls, text="Play ▶", width=10, command = on_play)
pause_btn = tk.Button(controls, text="Pause ⏸", width=10)#, command= on_pause, state="disabled"
stop_btn = tk.Button(controls, text="Stop ■", width=10)#, command=on_stop, state="disabled"
back_btn = tk.Button(controls, text="⏪ 5s", width=7)#, command=lambda: seek(-5), state="disabled")
forward_btn = tk.Button(controls, text="5s ⏩", width=7)#, command=lambda: seek(5), state="disabled")
load_btn = tk.Button(controls, text="Load .txt", width=10)#, command=load_txt

play_btn.pack(side="left", padx=6)
pause_btn.pack(side="left", padx=6)
stop_btn.pack(side="left", padx=6)
back_btn.pack(side="left", padx=6)
forward_btn.pack(side="left", padx=6)
load_btn.pack(side="left", padx=6)
play_btn.pack(side="left", padx=6)
back_btn.pack(side="left", padx=6)

root.mainloop()