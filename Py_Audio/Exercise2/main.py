import pyaudio
import wave

# Settings
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1              # Mono
RATE = 44100              # 44.1kHz sampling rate
CHUNK = 1024              # Buffer size
RECORD_SECONDS = 5        # Duration
OUTPUT_FILE = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("🎤 Recording...")

frames = []

# Read audio data in chunks
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("✅ Recording finished.")

# Stop and close
stream.stop_stream()
stream.close()
audio.terminate()

# Save to file
wf = wave.open(OUTPUT_FILE, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

print(f"💾 Saved as {OUTPUT_FILE}")