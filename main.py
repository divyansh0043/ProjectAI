import openai
from openai import OpenAI
import speech_recognition as sr
from config import apikey
import os
import re
import webbrowser


chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    client = OpenAI(api_key=apikey)
    chatStr += f"DK: {query}\nAI: "
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    chatStr += f"{response.choices[0].text}\n"
    say(response.choices[0].text)
    return response.choices[0].text


def ai(prompt):
    client = OpenAI(api_key=apikey)
    text = f"OpenAI response for Prompt: {prompt} \n*****************\n\n"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap inside a try catch block


    text += response.choices[0].text

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def say(text, speed=200, voice='Samantha'):
    os.system(f"say -r {speed} -v {voice} {text}")

def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            print(query)
            return query
        except Exception as e:
            return "Some Error occured, Sorry"
if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am your assistant from NurtureHeal may i know your name?")
    print("Listening...")
    query = input()
    result = re.findall('\\b[A-Z][A-Za-z]+\\b', query)

    while True:

        # sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"],]
        # for site in sites:
        #     if f"Open {site[0]}".lower() in query.lower():
        #         say(f"Opening {site[0]} sir")
        #         webbrowser.open(site[1])
        # say(query)
        say(f"{result[0]} Are you facing any physical or mental pain?")
        print("Listening...")

        query = input()
        if (query=="physical pain"):
            say(f"{result[0]} at what place you are feeling pain in the body upper or lower body?")
            query = input()



        # if f"what are you doing".lower() in query.lower():
        #     say("just chilling sir")

        # elif "Using artificial intelligence".lower() in query.lower():
        #     ai(prompt=query)
        # elif "AI Quit".lower() in query.lower():
        #     exit()
        #
        # elif "reset chat".lower() in query.lower():
        #     chatStr = ""
        else:
            print("Chatting...")
            chat(query)
