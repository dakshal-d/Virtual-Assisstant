import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import pyjokes
import smtplib
import ctypes
import requests
import json
import shutil
import tkinter
import subprocess
import pywhatkit as kit
import wolframalpha
import cv2

print ("initialising EDITH")
MASTER = "sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()    


def play_on_youtube(video):
    kit.playonyt(video)
def search(text):
    kit.search(text)

       

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morninng" + MASTER)

    elif hour >= 12 and hour<18 :
        speak("good Afternoon" + MASTER)

    else:
        speak("good evening" + MASTER)    
    
    
    

def takecommand():
    recording = sr.Recognizer()

    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recording.listen(source)
        
    try:
        print("recognising...")
        query = recording.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")   
        

    except Exception as e:
        print(e)
        return("None")
    return query    
def tellDay():
    

    day = datetime.datetime.today().weekday() + 1
    
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)   

speak("initialising EDITH")
if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()
wishMe()
chance = 3
while(chance != 0):
    speak("please authenticate")
    password =(input('Enter the password:'))
    cpass= '12345'
    if password == cpass:
        print("correct")
        speak("i am EDITH. how may i help you?")

        while True:
            
                query = takecommand().lower()

                if 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}") 

                elif 'open movies folder' in query:
                    dd = "D:\\Movies"
                    os.startfile(dd)
                
                elif 'open stackoverflow' in query:
                    speak("Here you go to Stack Over flow.Happy coding")
                    webbrowser.open("stackoverflow.com")

                elif 'powerpoint presentation' in query:
                    speak("opening Power Point presentation")
                    power = "D:\\voice assisstant\\PowerPoint Presentation.pptx"
                    os.startfile(power)


                elif "camera" in query or "take a photo" in query:
                    vid = cv2.VideoCapture(0)
  
                    while(True):
                        ret, frame = vid.read()
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    vid.release()
                    cv2.destroyAllWindows()

                elif "restart" in query:
                    os.system("shutdown /r /t 0")
                   

                elif 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences = 3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
                elif "what is" in query or "calculate" in query:
                    
                    question=input("what is the question:")
                    client = wolframalpha.Client("5YYYLV-6AA6K459XY")
                    res = client.query(question)
                    
                    try:
                        print (next(res.results).text)
                        speak (next(res.results).text)
                    except StopIteration:
                        print ("No results")
                
                elif "write a note" in query:
                    speak("What should i write, sir")
                    note = takecommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    sm = takecommand()
                    if 'yes' in sm or 'sure' in sm:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                
                elif "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read(6))

                elif " final review" in query:
                    xyz= "C:\\Users\\\\Downloads\\Project Exhibition 2 Final Review.pptx"
                    os.startfile(xyz)    

                elif "hibernate" in query or "sleep" in query:
                    speak("Hibernating")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif "log off" in query or "sign out" in query:
                    speak("signing-out")
                   
                    os.system("shutdown /l")
                
                elif 'shutdown system' in query:
                    speak("Your system is on its way to shut down")
                    subprocess.call('shutdown / p /f')
                
                elif 'empty recycle bin' in query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")        
                
                elif 'open folder' in query:
                    codePath = "D:\VIT sem5\AI"
                    os.startfile(codePath)
                
                elif 'open code' in query:
                    asd = "C:\\Users\\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    os.startfile(asd)        

                elif "day" in query:
                    tellDay()     
                        
                elif 'youtube' in query:
                    speak('What do you want to play on Youtube, sir?')
                    video = takecommand().lower()
                    play_on_youtube(video)
                    
                
                elif 'search on google' in query:
                    speak('What do you want to search on google, sir?')
                    text = takecommand().lower()
                    search(text)

                elif 'joke' in query:
                    My_joke = pyjokes.get_joke(language="en", category="neutral")
                    print(My_joke)
                    speak(My_joke)  
                
                elif 'how are you' in query:
                    speak("I am fine, Thank you")
                    speak("How are you, Sir")

                elif 'fine' in query or "good" in query:
                    speak("It's good to know that you are fine")
                
                elif 'exit' in query:
                    speak("Thanks for giving me your time")
                    exit()    
                
                elif "who are you" in query:
                    speak("I am your virtual assistant")

        
                elif "weather" in query:
                    api_key = "your key"

                    base_url = "https://api.openweathermap.org/data/2.5/weather?"

                    city_name = input("Enter city name : ")

                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    
                    response = requests.get(complete_url)

                    x = response.json()
        

                    if x["cod"] != "404":
        

                        y = x["main"]

                        current_temperature = y["temp"]
                        speak("the current temperature in" + city_name+ "is")
                        speak(current_temperature)
                        speak("kelvin units")
                        
        
                        current_pressure = y["pressure"]

                        current_humidity = y["humidity"]

                        z = x["weather"]
        

                        weather_description = z[0]["description"]

                        print(" Temperature (in kelvin unit) = " +
                                        str(current_temperature) +
                            "\n atmospheric pressure (in hPa unit) = " +
                                        str(current_pressure) +
                            "\n humidity (in percentage) = " +
                                        str(current_humidity) +
                            "\n description = " +
                                        str(weather_description))
        
                    else:
                        print(" City Not Found ")
        break

    elif password != cpass:
        print("Password is not correct, please try again")
        chance=chance-1
    



               

	   

              

		
    


               


    
    
 



               

	   

              

		
    


               


    
    
