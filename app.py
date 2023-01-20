from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/ai")
def assistant():
    #importing lib
    import pyttsx3
    import speech_recognition
    from datetime import date, datetime
    import webbrowser
    #lib for play search video on Youtube
    import pywhatkit
    #declaring
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot_brain=""
    #looping for non stop conversation AI
    while True:
        #listening code
        with speech_recognition.Microphone(sample_rate=48000) as mic:
            print("Robot: I'm Listening")
            audio = robot_ear.record(mic, duration=7)
        print("Robot: ...")
        #you= robot_ear.recognize_google(audio,language="vi-VI")
        try:
            you= robot_ear.recognize_google(audio)
        except:
            you = ""
        print("You: "+you)
        #AI part:
        #text responding code
        if you == "" :
            robot_brain = "I can't hear you, try again"
        elif "hello" in you:
            robot_brain="Hello Khang"
        elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
        elif "time" in you:
            now = datetime.now()
            robot_brain=now.strftime("%H hours %M minutes %S seconds")
        elif "president of America" in you:
            robot_brain="Joe Biden"
        elif "stop program" in you:
            robot_brain = "Goodbye Khang!"
            print("Robot: "+robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            #break
            return render_template('index.html')
        elif "YouTube" in you:
            
            filter = ['play', 'on YouTube']
            result = ''
            for i in filter:
                if(you!=filter):
                    result = you.replace(i,'')
            webbrowser.open("https://www.youtube.com/results?search_query="+result)
            #pywhatkit.playonyt("https://www.youtube.com/results?search_query="+result)
            robot_brain = "Find " + result + "on Youtube"
            #search query for youtube : https://www.youtube.com/results?search_query=
        elif "Google" in you:
            filter = ['search','find', 'on Google']
            result=''
            for i in filter:
                if(you!=filter):
                    result = you.replace(i,'')
            pywhatkit.search(result)
            robot_brain="Search" + result + "on Google"
        else:
            robot_brain = "I can't hear you, try again"
        print("Robot: "+robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
