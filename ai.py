import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import asyncio
import time

def speak(text,language):
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    voices=engine.getProperty('voices')
    if language=="en":
        engine.setProperty('voice',voices[0].id)
    else:
        engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in english......")
        audio=recognizer.listen(source)
    try:
        print("??? Recognizing Sppech.....")
        text=recognizer.recognize_google(audio,language="en-US")
        print(f"You said : {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print(f"API ERROR: {e}")
    return ""

if __name__ == "__main__":
    print("Starting program...")
    text = speech_to_text()
    print("repeating...")
    speak(text=text, language="en")