import pyttsx3
from googletrans import Translator
import speech_recognition as sr
import asyncio


def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text=text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Please speak....")
        audio = recognizer.listen(source=mic)
    
    try:
        print("Converting to text...")
        text=recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Cound not understand...")
    except sr.RequestError as e:
        print(f"API ERROR | {e}")
    return ""

async def translate_text(text, lang="es"):
    translator = Translator()
    translated = await translator.translate(text, dest=lang)
    return translated.text

def display_options():
    langs = {
        1 : "es",
        2 : "fr",
        3 : "it"
    }
    print("Supported language (1-3): \n1. es \n2.fr \n3.it")
    user = int(input("> "))
    return langs.get(user, "es")

def main():
    print("Starting...")
    option = display_options()
    text = speech_to_text()
    
    print("trannslating....")
    translated_text=asyncio.run(translate_text(text=text, lang=option))
    
    print(f"Translated message: {translated_text}")
    speak(translated_text, language=option)

main()
    