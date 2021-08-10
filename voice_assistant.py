import speech_recognition as sr
import pyttsx3
import os
import datetime
from prettytable import PrettyTable
import match
import run
import random
import openpyxl

# File Manipulation
greet = []
error = []
xlsx = openpyxl.load_workbook("d:\\harish\\python\\Family-AI\\Data\\Greet.xlsx")
Xlsx = openpyxl.load_workbook("d:\\harish\\python\\Family-AI\\Data\\Error.xlsx")
Greet = xlsx["Sheet1"]
Error = Xlsx["Sheet1"]
for cell in Greet["A"]:
    if cell.value is not None:
        greet.append(cell.value)
for cell in Error["A"]:
    if cell.value is not None:
        error.append(cell.value)
# End of File Manipulation

# Functions

def speak(text): # Function to Speak text
    engine.say(text)
    engine.runAndWait()

def takeCommand(): # Function to get Input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("F-AI >>> Listening...")
        speak("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"F-AI >>> User said : {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("F-AI >>> Hello,Good Morning")
        speak("Hello,Good Morning")
    elif hour>=12 and hour<18:
        print("F-AI >>> Hello,Good Afternoon")
        speak("Hello,Good Afternoon")
    else:
        print("F-AI >>> Hello,Good Evening")
        speak("Hello,Good Evening")
        
# End of Functions

# Voice Configuration
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# Main Program
if __name__ == "__main__":
    print("\n \n \n")
    head = PrettyTable()
    head.field_names = ["Welcome to F-AI , Your Personal Assistant"]
    print(head)
    speak("Welcome to F-AI , Your Personal Assistant")
    wishMe()
    speak(greet[random.randrange(0,10,1)])

    while True:
        try:
            statement = takeCommand().lower()
            if statement==0:
                continue
            elif match.whopbirth(statement) == 100:
                ans = []
                ans, place = run.whopbirth_finder(statement)
                anslen = len(ans)
                ans1 = ''
                if anslen > 1:
                    for i in range(0,anslen,1): ans1 = ans1 + ans[i] + ", "
                    ans1 = ans1 + " were born in " + place
                elif ans[0] == "Results not Found":
                    ans1 = "Results not Found"
                else:
                    ans1 = ans[0] + " was born in " + place
                print("F-AI >>> ",ans1)
                speak(ans1)
            elif match.whonative(statement) == 100:
                ans = []
                ans, place = run.whonative_finder(statement)
                anslen = len(ans)
                ans1 = ''
                if anslen > 1:
                    for i in range(0,anslen,1): ans1 = ans1 + ans[i] + ", "
                    ans1 = ans1 + " has native " + place
                elif ans[0] == "Results not Found":
                    ans1 = "Results not Found"
                else:
                    ans1 = ans[0] + " has " + place
                print("F-AI >>> ",ans1)
                speak(ans1)
            elif match.dobmatch(statement) == 100:
                ans = run.dob_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.pobmatch(statement) == 100:
                ans = run.pob_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.nativematch(statement) == 100:
                ans = run.native_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.parentmatch(statement) == 100:
                ans = run.parent_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.fathermatch(statement) == 100:
                ans = run.father_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.mothermatch(statement) == 100:
                ans = run.mother_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.jobmatch(statement) == 100:
                ans = run.job_finder(statement)
                print("F-AI >>> ",ans)
                speak(ans)
            elif match.biomatch(statement) == 100:
                ans, tell = run.bio_finder(statement)
                print("F-AI >>> Bio Data ")
                print(ans)
                speak(tell)
            elif "clear" in statement or "clean" in statement or "flush" in statement:
                os.system('cls') if os.name == 'nt' else os.system('clear')
            elif "terminate" in statement or "stop" in statement or "shutdown" in statement or "shut down" in statement:
                print('F-AI >>> Your personal assistant F-AI is shutting down, Good bye')
                speak('your personal assistant F-AI is shutting down, Good bye')
                break
            else:
                i = random.randrange(0,5,1)
                print("F-AI >>> ",error[i])
                speak(error[i])
        except:
            i = random.randrange(0,5,1)
            print("F-AI >>> ",error[i])
            speak(error[i])