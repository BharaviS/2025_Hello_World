import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 1)

class PromptReader:
    def __init__(self, audio) -> None:
        self.__audio = audio

    @property
    def speak(self) -> None:
        engine.say(self.__audio)
        engine.runAndWait()

        return None

if __name__ == '__main__':
    text = input("Enter your text: ")
    prompt = PromptReader(text).speak