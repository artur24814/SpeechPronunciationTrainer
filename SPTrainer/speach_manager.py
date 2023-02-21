import pyttsx3
from googletrans import Translator

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

import speech_recognition
import sounddevice
recognition = speech_recognition.Recognizer()

"""
example script for using in simple python code
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
"""

class SpeachManager:

    def __init__(self):
        self.recognition = speech_recognition.Recognizer()
        self.mic = speech_recognition.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)
        # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
        self.translator = Translator()

    def translate(self, text, ResultTrans, language):
        if text != '':
            translation = self.translator.translate(text, dest=language)
            print(translation.text)
            ResultTrans.content = TextInput(text=translation.text)
            ResultTrans().open()

    def record(self, text_in, text_out, ResultTrans, ResultLabel):
        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        try:
            #open microphone
            result = self.check_answer(text_in, text_out)
            ResultTrans.content = ResultLabel(text=result)
            ResultTrans.title = 'Result'
            ResultTrans().open()
            with self.mic as mic:
                self.recognition.adjust_for_ambient_noise(mic)
                print('Say ...')
                audio = self.recognition.listen(mic, timeout = 4)
            print('ok, Try to recognize')
            #recognize text
            text = self.recognition.recognize_google(audio)
            print('ok, I understand')
            text = text.lower()
            print(text)
            text_out.text = text
            return text

        except speech_recognition.UnknownValueError:
            text_out.text = "Oops! Didn't catch that"
            return "Oops! Didn't catch that"
        except speech_recognition.RequestError as e:
            text_out.text = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            return "Uh oh! Couldn't request results from Google Speech Recognition service"

    def say(self, text):
        if text != '':
            self.engine.say(text)
            self.engine.runAndWait()

    def check_answer(self, textIn, textOut):
        list_wordsIn = textIn.text.lower().split(' ')
        list_wordsOut = textOut.text.lower().split(' ')
        result = []
        for word in list_wordsIn:
            if word in list_wordsOut:
                result.append(f'[color=#1de705]{word}[/color]')
            else:
                result.append(f'[color=#e71a05]{word}[/color]')
            list_wordsIn.remove(word)
        return ' '.join(result)





