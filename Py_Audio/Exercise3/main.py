import vlc
import time

# Create VLC instance and player
instance = vlc.Instance()
player = instance.media_player_new()

# Load a media file (MP3, MP4, WAV, etc.)
media = instance.media_new("audio.wav")
player.set_media(media)

# Play
player.play()
time.sleep(5)  # play for 5 sec

# Pause
player.pause()
time.sleep(2)

# Resume
player.play()
time.sleep(5)

# Stop
player.stop()
