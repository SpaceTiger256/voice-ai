import pyttsx3
import speech_recognition as sr
import datetime as time

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 1)
    engine.say(text=text)
    engine.runAndWait()

def rec():
    voice = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        audio = voice.listen(mic)
        try:
            text = voice.recognize_google(audio)
            print(f"You : {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand what you said.")
            return "An error occured. Please try again"
        except sr.RequestError as e:
            print(f"An error occured | {e}")
            return "An error occured. Please try again"

def reply_to_command(text):
    keywords_and_answers = {
        "hello" : "Hello there!",
        "name" : "My name is bob Ai. I'm at your service!",
        "time" : f"""it's currenty {time.datetime.now().strftime('%H:%M')}""",
        "goodbye" : "Okay goodbye!",
        "okay" : "No problem!",
        "i love you" : "As an artificial inteligence, I cannot feel emotions. I'm really sorry",
        "you are cool" : "Thankyou!"
    }
    
    for key in keywords_and_answers:
        if key in text:
            speak(text=keywords_and_answers[key])
            return
    speak("I don't understand sorry.")

def main():
    print("Starting bob Ai...")
    while True:
        user = rec()
        if user == "exit":
            break
        
        reply_to_command(text=user)
    
if __name__ == "__main__":
    main()