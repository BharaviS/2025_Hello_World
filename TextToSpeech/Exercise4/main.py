import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class PromptReaderGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Prompt Reader")
        self.root.geometry("800x520")

        self.text = tk.Text(root, wrap="word", font=("Arial", 12))
        self.text.pack(expand=True, fill="both", padx=10, pady=(10, 6))

        controls = tk.Frame(root)
        controls.pack(fill="x", padx=10, pady=(0, 10))

        self.play_btn = tk.Button(controls, text="Play ▶", width=10)#, command=self.on_play
        self.pause_btn = tk.Button(controls, text="Pause ⏸", width=10,  state="disabled") # command=self.on_pause,
        self.stop_btn = tk.Button(controls, text="Stop ■", width=10,  state="disabled") # command=self.on_stop,
        self.back_btn = tk.Button(controls, text="⏪ 5s", width=7,  state="disabled") # command=lambda: self.seek(-5),
        self.forward_btn = tk.Button(controls, text="5s ⏩", width=7,  state="disabled") # command=lambda: self.seek(5),
        self.load_btn = tk.Button(controls, text="Load .txt", width=10)#, command=self.load_txt

        self.play_btn.pack(side="left", padx=6)
        self.pause_btn.pack(side="left", padx=6)
        self.stop_btn.pack(side="left", padx=6)
        self.back_btn.pack(side="left", padx=6)
        self.forward_btn.pack(side="left", padx=6)
        self.load_btn.pack(side="right", padx=6)

        self.root.mainloop()

if __name__ == "__main__":
    main = PromptReaderGui(tk.Tk())