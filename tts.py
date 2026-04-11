import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import asyncio


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


async def translate_text(text,target_language="es"):
    translator=Translator()
    translation=await translator.translate(text,dest=target_language)
    print(f"Translated Text..... {translation.text}")
    return translation.text




def display_language_options():
    print("Available translation langauges: ")
    print("1. Hindi")
    print("2. Tamil")
    print("3. Teulgu")
    print("4. Bengali")
    print("5. Marathi")
    print("6. Gujarati")
    print("7. Malayalam")
    print("8. Punjabi")


    choice=input("Please select the target language number 1- 8: ")
    language_dict={
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4":"bn",
        "5":"mr",
        "6":"gu",
        "7":"ml",
        "8":"pa"
    }
    return language_dict.get(choice,"es")
def main():
    target_language=display_language_options()
    original_text=speech_to_text()
    if original_text:
        translated_text=asyncio.run(translate_text(original_text,target_language=target_language))
        speak(translated_text,language="en")
        print("Translation spoken out")
main()