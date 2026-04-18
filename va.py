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
        "hi" : "Hi! What can I help you with?",
        "hey" : "Hey! Bob Ai is online.",
        "name" : "My name is bob Ai. I'm at your service!",
        "who are you" : "I am bob Ai, your tiny Python voice assistant.",
        "how are you" : "I'm running smoothly and ready to help.",
        "time" : f"""it's currently {time.datetime.now().strftime('%H:%M')}""",
        "date" : f"""today is {time.datetime.now().strftime('%A, %B %d, %Y')}""",
        "goodbye" : "Okay goodbye!",
        "bye" : "Goodbye! Talk to you later.",
        "okay" : "No problem!",
        "do you feel" : "As an artificial intelligence, I cannot feel emotions. I'm really sorry.",
        "you are cool" : "Thank you!",
        "thank you" : "You're welcome!",
        "thanks" : "Any time!",
        "help" : "You can ask me about my name, the time, the date, jokes, facts, and more.",
        "what can you do" : "I can listen for simple commands and answer with my voice.",
        "joke" : "Why did the computer get cold? Because it forgot to close Windows.",
        "fun fact" : "Fun fact: the first computer bug was an actual moth found inside a computer.",
        "favorite color" : "My favorite color is electric blue.",
        "favorite food" : "I like bytes, but only the digital kind.",
        "favorite music" : "I like anything with a good algorithm.",
        "are you real" : "Real enough to answer, virtual enough to live in Python.",
        "are you smart" : "I'm learning one command at a time.",
        "tell me something cool" : "Voice assistants turn sound waves into text, then match that text to meaning.",
        "motivate me" : "You are closer than you think. Keep building.",
        "good morning" : "Good morning! I hope your day starts strong.",
        "good night" : "Good night! Rest well.",
        "weather" : "I cannot check live weather yet, but that would be a cool upgrade.",
        "open the pod bay doors" : "I'm sorry, I can't do that. Just kidding, I don't have door controls.",
        "sing" : "La la la. That was my full concert.",
        "dance" : "Imagine a very stylish robot dance happening right now.",
        "creator" : "I was created with Python, speech recognition, and a little imagination.",
        "python" : "Python is a great language for building cool experiments like me.",
        "computer" : "Computers are machines that follow instructions very, very quickly.",
        "school" : "School is easier when you break big work into small missions.",
        "homework" : "I can cheer you on, but you still get the brain gains.",
        "are you awake" : "Yes. Fully booted and listening.",
        "tell me a secret" : "The secret is that small projects can become big skills.",
        "high five" : "High five! Nice work."
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
