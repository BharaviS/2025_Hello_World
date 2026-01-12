import vlc
import time

# Create VLC instance
instance = vlc.Instance()
player = instance.media_player_new()

# Load media
media = instance.media_new("audio.wav")
media.parse_with_options(vlc.MediaParseFlag.local, timeout=5)  # Parse metadata

player.set_media(media)

# Get duration
duration = media.get_duration()
print(f"Media length: {duration} ms")

# Play it
import wave

# Open the WAV file
with wave.open("audio.wav", "rb") as wav_file:
    # Get number of frames
    frames = wav_file.getnframes()
    # Get frame rate (samples per second)
    rate = wav_file.getframerate()
    # Calculate duration
    duration = frames / float(rate)

    print(f"Frames: {frames}")
    print(f"Frame Rate: {rate}")
    print(f"Duration: {duration:.2f} seconds")

player.play()
time.sleep(duration)
player.stop()