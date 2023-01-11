import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty('rate', 125)
# engine.say("I will speak this text")
# engine.runAndWait()

import speech_recognition
import sounddevice
recognition = speech_recognition.Recognizer()


while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognition.adjust_for_ambient_noise(mic, duration=0.2)
            print('Say ...')
            audio = recognition.listen(mic)
            text = recognition.recognize_google(audio)
            text = text.lower()
            print(f'You say {text}')

    except speech_recognition.UnknownValueError:
        recognition = speech_recognition.Recognizer()
        print('Error')
        continue


class SpeachManager:

    def __init__(self):
        self.recognition = speech_recognition.Recognizer()
        self.mic = speech_recognition.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)

    def record(self):
        while True:
            try:
                with self.mic as mic:
                    self.recognition.adjust_for_ambient_noise(mic, duration=0.2)
                    print('Say ...')
                    audio = self.recognition.listen(mic)
                    text = self.recognition.recognize_google(audio)
                    text = text.lower()
                    print(f'You say {text}')

            except speech_recognition.UnknownValueError:
                print('Error')
                continue

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


