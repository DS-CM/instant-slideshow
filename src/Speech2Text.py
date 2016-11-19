#!/usr/bin/env python3
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import time as time
from datetime import datetime

TIME = False

class Speech2Text:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):
        # Provide count down until speaking
        for i in range(3):
            print(3-i)
            time.sleep(1)

        # obtain audio from the microphone
        with sr.Microphone() as source:
            print("Say something!")
            # audio = r.record(source, duration=2)
            self.r.phrase_threshold = 2
            audio = self.r.listen(source, timeout = 2)
        
        if TIME: start = datetime.now()
        # self.__localSpeech2Text(audio)
        self.__googleSpeech2Text(audio)
        if TIME: end = datetime.now(); print("Time taken: {}".format(end-start))
    
    def __localSpeech2Text(self, audio):
        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said: " + self.r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

    def __googleSpeech2Text(self, audio):
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said: " + self.r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
