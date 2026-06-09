import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    
    speak(greeting + " I am Jarvis Sir How may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio=r.listen(source)
    try:
        print("Recognizing...")    
        query=r.recognize_google(audio,language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        if 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("Opening Facebook")      
            webbrowser.open("https://web.facebook.com/profile.php?id=61579748162284")

        elif 'open instagram' in query:    
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'open chess.com' in query:
            speak("Opening Chess.com")
            webbrowser.open("https://www.chess.com/home") 

        elif 'open gpt' in query:
            speak("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com/")

        elif 'open Grok' in query: 
            speak("Opening Grok")
            webbrowser.open("https://grok.com/")

        elif 'open canva' in query:
            speak("Opening Canva")
            webbrowser.open("https://www.canva.com/")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HOME\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open github' in query:
            speak("Opening Github")
            webbrowser.open("https://www.github.com")           