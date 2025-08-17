import pyaudio
import wave

FILE = "audio.wav"

wf = wave.open(FILE, "rb")

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

# Read and play back
data = wf.readframes(1024)

print("🔊 Playing...")

while data:
    stream.write(data)
    data = wf.readframes(1024)

# Stop and close
stream.stop_stream()
stream.close()
audio.terminate()

print("✅ Done.")
