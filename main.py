
import speech_recognition as sr
import os
import webbrowser
def say(text):
    os.system(f"say {text}")

def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google_cloud(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occured, Sorry"
if __name__ == '__main__':
    print('PyCharm')
    say("Hello i m dk")
    while True:
        print("Listening...")
        query = input()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
        # say(query)
        if f"what are you doing".lower() in query.lower():
            say("just chilling sir")

