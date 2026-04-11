import pyttsx3
from googletrans import Translator
import speech_recognition as sr
import asyncio

def speak(text):
    tts = pyttsx3.init()
    tts.setProperty('rate',150)
    tts.setProperty("voices", 0)
    
    tts.say(text)
    tts.runAndWait()

def transcribe():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Please speak now...")
        audio = rec.listen(mic)
    try:
        print("Transcribing...")
        txt = rec.recognize_google(audio, language="en-US")
        print(f"You said: {txt}")
        return txt
    except sr.UnknownValueError:
        print(f"Could not understand...")
    except sr.RequestError as e:
        print(f"An error occured while transcribing... | {e}")

async def translate(text, lan):
    engine = Translator()
    translated_txt = await engine.translate(text=text, dest=lan)
    return translated_txt.text


def main():
    print("Welcome to the Ai Live voice translation system.")
    print("There ate 5 languages to choose from: \n [en, fr, es, hi, te]")
    langs = ['en', 'fr', 'es', 'hi', 'te']
    lang = input("Please select a language: ")
    
    for i in langs:
        if i != lang:
            continue
        else:
            text = transcribe()
            speak(text=text)
            print("Translating....")
            print(asyncio.run(translate(text=text, lan=lang)))

main()
