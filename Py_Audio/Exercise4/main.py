import sys
import vlc
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel


class AudioPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎵 Simple Audio Player")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("No file loaded")
        self.layout.addWidget(self.label)

        self.btn_open = QPushButton("Open Audio")
        self.btn_open.clicked.connect(self.open_file)
        self.layout.addWidget(self.btn_open)

        self.btn_play = QPushButton("▶ Play")
        self.btn_play.clicked.connect(self.play_audio)
        self.layout.addWidget(self.btn_play)

        self.btn_pause = QPushButton("⏸ Pause")
        self.btn_pause.clicked.connect(self.pause_audio)
        self.layout.addWidget(self.btn_pause)

        self.btn_stop = QPushButton("⏹ Stop")
        self.btn_stop.clicked.connect(self.stop_audio)
        self.layout.addWidget(self.btn_stop)

        self.setLayout(self.layout)

        self.player = None
        self.media = None

    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Audio", "", "Audio Files (*.mp3 *.wav)")
        if file:
            self.label.setText(f"Loaded: {file}")
            self.player = vlc.MediaPlayer(file)

    def play_audio(self):
        if self.player:
            self.player.play()

    def pause_audio(self):
        if self.player:
            self.player.pause()

    def stop_audio(self):
        if self.player:
            self.player.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec())
