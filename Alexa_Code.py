import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import os
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Using ZIRA as our Alexa
engine.setProperty('voice', voices[0].id)
# Setting the speed of Alexa
engine.setProperty('rate', 150) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        print("Good Morning sir. I am Alexa how may I help you?")
        speak("Good Morning sir. I am Alexa, how may I help you?")

    elif hour>=12 and hour<18:
        print("Good Afternoon sir. I am Alexa, how may I help you?")
        speak("Good Afternoon sir. I am Alexa, how may I help you?")

    else:
        print("Good Evening sir. I am Alexa, how may I help you?")
        speak("Good Evening sir. I am Alexa, how may I help you?")


def takeInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")  
        return "None"
    return query


def wikiPedia(query):
    import wikipedia
    try:
        print('Searching Wikipedia...')
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        print("According to Wikipedia")
        speak("According to Wikipedia")
        print(results)
        speak(results)

    except Exception as e:
        print("Please be specific in your search")
        speak("Please be specific in your search")


def news(query):
    
    import requests
    import json

    url_headines = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"
    url_business = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"
    url_entertainment = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"
    url_health = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"
    url_science = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"
    url_sports = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"
    url_technology = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c6bcdcd9b1924d71a152a54cc34b1aa8"

    
    

    if 'business' in query:
        url = url_business

    elif 'entertainment' in query:
        url = url_entertainment

    elif 'health' in query:
        url = url_health

    elif 'science' in query:
        url = url_science

    elif 'sports' in query:
        url = url_sports

    elif 'technology' in query:
        url = url_technology

    else:
        url = url_headines
        

    news = requests.get(url).text
    news_Dict = json.loads(news)
    arts = news_Dict['articles']
    print("Today's headlines are:")
    speak("Today's headlines are:")
    
    for i in range(1,3,1):
        speak2 = (arts[i]['title'])
        print(speak2)
        speak(speak2)

        if(i==2):
            print("Thank you for listening")    
            speak("Thank you for listening")    
            break
        
        
        print("Next headline is")
        speak("Next headline is")



def date():
    today = str(datetime.date.today())
    current_date = "Today's daye is " + today
    print(current_date)
    speak(current_date)



def time():
    from datetime import datetime

    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    current_time = "Current time is "+ current
    print(current_time)
    speak(current_time)


def playMusic():
    music_dir = r'C:\APURV\4th Year\VISUAL STUDIO CODE\PROJECTS\Alexa\Alexa saved songs'
    songs = os.listdir(music_dir)
    print(songs)   
    random_song = random.randint(0,len(songs)-1) 
    os.startfile(os.path.join(music_dir, songs[random_song]))
    exit()


if __name__=="__main__":

    greetMe()

    while True:

        query = takeInput().lower()


        if 'wikipedia' in query:
            wikiPedia(query)

        elif 'news' in query:
            news(query)


        elif 'sensex' in query:
            print("Opening SENSEX chart. Please wait for few seconds")
            speak("Opening SENSEX chart. Please wait for few seconds")
            webbrowser.open_new('https://in.tradingview.com/symbols/BSE-SENSEX/')


        elif 'nifty' in query:
            print("Opening NIFTY chart. Please wait for few seconds")
            speak("Opening NIFTY chart. Please wait for few seconds")
            webbrowser.open_new('https://in.tradingview.com/symbols/NSE-NIFTY/')

        elif 'open youtube' in query:
            print("Opening youtube. Please wait for few seconds")
            speak("Opening youtube. Please wait for few seconds")
            webbrowser.open_new('http://youtube.com')

        elif 'open google' in query:
            print("Opening google. Please wait for few seconds")
            speak("Opening google. Please wait for few seconds")
            webbrowser.open_new('http://google.com')

        elif 'open stack overflow' in query:
            print("Opening stack overflow. Please wait for few seconds")
            speak("Opening stack overflow. Please wait for few seconds")
            webbrowser.open_new('http://stackoverflow.com')

        elif 'music' in query:
            print("playing music")
            speak("playing music")
            print("Please wait")
            speak("please wait")
            playMusic()

        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'exit' in query:
            print("Have a good day sir")
            speak("Have a good day sir")
            exit()


  




