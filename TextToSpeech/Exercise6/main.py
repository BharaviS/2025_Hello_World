from pydub import AudioSegment
from pydub.playback import play

# Load audio
sound = AudioSegment.from_file("audio.wav")

# Increase speed (1.5x)
faster = sound._spawn(sound.raw_data, overrides={
    "frame_rate": int(sound.frame_rate * 1.5)
}).set_frame_rate(sound.frame_rate)

# Decrease speed (0.7x)
slower = sound._spawn(sound.raw_data, overrides={
    "frame_rate": int(sound.frame_rate * 0.7)
}).set_frame_rate(sound.frame_rate)

print("Playing faster version...")
play(faster)

print("Playing slower version...")
play(slower)
