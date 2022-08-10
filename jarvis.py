from re import search
from token import NUMBER
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pywhatkit
import pyautogui
import PyPDF2

Assistant=pyttsx3.init('sapi5')
voices =Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',200)

def  speak(audio):
    Assistant.say(audio)
    Assistant.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if  hour>=0 and hour<12:
        speak("good morning sir!")
    elif  hour>=12 and hour<18:
        speak("good adfternoon sir!")
    else:
        speak("good evening sir!")
    speak("I am Jarvis")
    speak("what i can do for you sir")

def takecommand():
    #it takes microphone input from user and  return text output.
    r= sr.Recognizer()    
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
   
    return query
#def sendEmail(to, content)
def song():
    speak("which song you have to want to play sir!")
    songName=takecommand()
    songName=songName.replace("song","")
    songName=songName.replace("jarvis","")
    pywhatkit.playonyt(songName)
    speak("enjoy sir!")

def youtube_search():
    speak("what you have to search sir!")
    search=takecommand()
    speak('yes sir, this is what i found for your search')
    search=search.replace("jarvis","")
    results=webbrowser.open("www.youtube.com/results?search_query="+ search)
    speak("done sir!")

def google_search():
    speak("what you have to search sir!")
    search=takecommand()
    speak('yes sir, this is what i found for your search')
    search=search.replace("jarvis","")
    pywhatkit.search(search)
    speak("done sir!")

def wiki_pedia():
    speak("what you have to search sir!")
    search=takecommand()
    speak('Searching wikipedia....')
    search= search.replace("wikipedia","")
    search=search.replace("jarvis","")
    results =wikipedia.summary(search, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

def whatsapp():
    def number(person):
        speak("tell me the message")
        msg=takecommand()
        speak("tell me the time sir")
        speak("time in hour")
        hour=int(takecommand())
        speak("time in minute")
        min=int(takecommand())
        pywhatkit.sendwhatmsg(person,msg,hour,min,50)
        speak("sent sir!")

    while True:
        speak("tell me the name  of the person!")
        name=takecommand().lower()
        if 'deepak' in name:
            number("+919798080667")    

        elif 'sonu' in name:
            number("+919931389064")
        
        elif 'amrit' in name:
            number("+917061443360")
      
        elif 'shibu' in name:
            number("+918578953739")

        elif 'sumit' in name:
            number("+919981982717")

        elif 'saurabh' in name:
            number("+916207270817")

        elif 'rahul singh' in name:
            number("+917479924339")

        elif 'navneet' in name:
            number("+916203298069")
        
        elif 'motion' in name:
            number("+918935877887")

        elif 'ok done' in name:
            return None


def open_App():
    speak("ok sir! wait")
    if 'instagram app' in query:
        webbrowser.open("www.instagram.com")

    elif 'facebook app' in query:
        webbrowser.open("www.facebook.com")

    elif 'whatsapp app ' in query:
        webbrowser.open("web.whatsapp.com")

    elif 'amazon app' in query:
        webbrowser.open("www.amazon.com")

    elif 'open mail' in query:
        webbrowser.open("mail.google.com/mail/u/0/#inbox")

    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
    
    elif 'open visual studio code' in query:
        codePath = "C:\\Users\\hr165\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open microsoft edge' in query:
        codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(codePath)

    elif 'open chrome' in query:
        codePath= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
    
    elif 'google app' in query:
        webbrowser.open("www.google.com")

    elif 'open github' in query:
        webbrowser.open("https://github.com/")

def close_App():
    speak("ok sir! wait")
    if 'close youtube app' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'close chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'close microsoft edge' in query:
        os.system("TASKKILL /F /im msedge.exe")

    elif 'close visual studio code' in query:
        os.system("TASKKILL /F /im code.exe")


if __name__ == "__main__":
    wishme()
    while True:
        query =takecommand().lower()
    #logic for executing tasks based on query
        if 'how are you' in query:
            speak("i am fine sir!")

        elif 'who are you'  in query:
            speak("i am jarvis")

        elif 'your boss' in query:
            speak("Hrithik Choudhary")

        elif 'wikipedia' in query:
            wiki_pedia()
        
        elif 'youtube search' in query:
            youtube_search()
           
        elif 'google app' in query:
            open_App()

        elif 'google search' in query:
            google_search()

        elif 'instagram app' in query:
            open_App()
            
        elif 'amazon app' in query:
            open_App()

        elif 'whatsapp app' in query:
            open_App()

        elif 'facebook app' in query:
            open_App()

        elif 'youtube app' in query:
            open_App()
        
        elif 'close youtube app' in query:
            close_App()

        elif 'open visual studio code' in query:
            open_App()
        
        elif 'close visual studio code' in query:
            close_App()

        elif 'open chrome' in query:
            open_App()
        
        elif 'close chrome' in query:
            close_App()

        elif 'open microsoft edge' in query:
            open_App()

        elif 'close microsoft edge' in query:
            close_App()

        elif 'open mail' in query:
            open_App()

        elif 'play song' in query:
            song()
        
        elif 'open github' in query:
            open_App()

        elif 'whatsapp message' in query:
            whatsapp()

        elif 'map' in query:
            webbrowser.open("www.google.com/maps/@22.5902592,88.408064,12z")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)
        
        elif 'my resume' in query:
            codePath ="C:\\Users\\hr165\\Downloads\\Resume.pdf"
            webbrowser.open_new(codePath)

        elif 'mis website' in query:
            webbrowser.open("https://mis.nita.ac.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA==")
        
        elif 'ok bye' in query:
            sys.exit()
        

        
        

        



