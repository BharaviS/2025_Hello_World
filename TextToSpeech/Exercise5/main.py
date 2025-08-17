import pyttsx3
import os
import tempfile
import pygame
import time

AUDIO_PATH = os.path.join(tempfile.gettempdir(), "audio.wav")
engine = pyttsx3.init()
pygame.mixer.init()

def main(my_text):
    my_text = my_text.strip()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 125)
    engine.setProperty("volume", 0.8)
    engine.setProperty("voice", voices[1].id)

    engine.save_to_file(text=my_text, filename=AUDIO_PATH)
    engine.runAndWait()

    print(text, "\n", AUDIO_PATH)

def audio():
    if not os.path.exists(AUDIO_PATH):
        print("Audio file not found!")
        return

    pygame.mixer.music.load(AUDIO_PATH)
    pygame.mixer.Sound(AUDIO_PATH)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


if __name__ == "__main__":
    text = """Get started learning Python with DataCamp's free Intro to Python tutorial. 
    Learn Data Science by completing interactive coding challenges and watching videos by 
    expert instructors. Start Now!
    This site is generously supported by DataCamp. DataCamp offers online interactive 
    Python Tutorials for Data Science. Join 11 million other learners and get started learning 
    Python for data science today!
    Good news! You can save 25% off your Datacamp annual subscription with the code LEA"""
    main(text)
    audio()
    print("Hi")