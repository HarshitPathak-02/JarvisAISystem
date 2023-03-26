from time import strftime
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os


engine = pyttsx3.init('''sapi5''')
voices = engine.getProperty('''voices''')
print(voices[0].id)
engine.setProperty('''voice''', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('''Good Morning''')

    elif hour>=12 and hour<18:
        speak('''Good Afternoon''')

    else :
        speak('''Good Evening''')

    speak('''I am your personal assistant please tell me how can i help you?''')

def takeCommand():
    #it takes microphone input from the users and string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('''Listening....''')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('''Recognising....''')
        query = r.recognize_google(audio, language='''en-in''')
        print(f'''User said: {query}\n''')

    except Exception as e :
        print('''Say that again please...''')
        return '''None'''
    return query

if __name__ == '''__main__''':
    speak('''Hello Harshit Sir''')
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic ecxecuting task
        if '''wikipedia''' in query:
            speak('''Searching Wikipedia...''')
            query = query.replace('''wikipedia''','''''')
            results = wikipedia.summary(query, sentences=2)
            speak('''According to wikipedia''')
            print(results)
            speak(results)

        elif '''open youtube''' in query:
            webbrowser.open('''youtube.com''')

        elif '''open google''' in query:
            webbrowser.open('''google.com''')

        elif '''play music''' in query:
            music_dir = '''C:\\Personal\\Songs'''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif '''the time''' in query:
            strTime = datetime.datetime.now().strftime('''%H:%M:%S''')
            speak(f'''The time is {strTime}''')

        elif '''open vs code''' in query:
            codePath = '''C:\\Users\\HARSHIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'''
            os.startfile(codePath)

        elif '''open telegram''' in query:
            d = "C:\\Users\\HARSHIT\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(d)

        elif '''open Microsoft Office''' in query:
            e = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(e)

        elif '''open amazon''' in query:
            webbrowser.open('''amazon.com''')   

        elif '''open excel''' in query:
            f = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(f)

        elif '''open google chrome''' in query:
            g = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(g)

        elif '''open stackoverflow''' in query:
            webbrowser.open('''stackoverflow.com''')

        elif '''open adobe photoshop''' in query:
            h = "C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"

        elif '''open PowerPoint''' in query:
            i = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"

        elif '''open shortcut''' in query:
            j = "C:\\Program Files\\Shotcut\\shotcut.exe"

        elif '''open word''' in query :
            k = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"

        elif '''what is my name''' in query :
            l = speak("Your name is Harshit Pathak")

        elif '''exit''' in query:
            exit()
            
        


