import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")  
    
    else:
        speak("Good Morning")

    speak("I am jarvis sir. Develope by pranay")

def takeCommand():
    # its take microphone voice and show strin
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")      

    except Exception as e:
        print(e)

        print("say that again please..")
        return "NONE"

    return query


def sendEmail(to,content):
    sever = smtplib.SMTP('smntp.gmail.com', 587)
    sever.ehlo()
    sever.starttls()
    sever.login('pranaybadgujar123@gmail.com','pranay1234')
    sever.sendmail('pranaybadgujar123@gmail.com',to,content)
    sever.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        break

    
   
#    logic
    if 'wikipedia' in query:
        speak('searching wikipedia..')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'play music' in query:
        music_dir = 'C:/Users/Asus/Music/songs'
        

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open chrome' in query:
        codePath = "C:\\Users\\Asus\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
        
    elif 'email to pranay' in query:
        try:
            speak('what should I say?')
            contant = takeCommand()
            to = "pranaybadgujar123@gmail.com"
            sendEmail(to,contant)
            speak('Email has been send')
        except Exception as e:
            print(e)
            speak('sorry my friend pranay iam not able to send email')
