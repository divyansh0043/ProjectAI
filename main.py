# import openai
from openai import OpenAI
import speech_recognition as sr
from config import apikey
import os
import webbrowser
import random


def ai(prompt):
    client = OpenAI(api_key=apikey)
    text = f"OpenAI response for Prompt: {prompt} \n*****************\n\n"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap inside a try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")
    print(text)




def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google_cloud(audio, language="en-in")
            print(f"User said:{query}")
            print(query)
            return query
        except Exception as e:
            return "Some Error Occured, Sorry"
if __name__ == '__main__':
    print('PyCharm')
    say("Hello i m dk")
    while True:
        print("Listening...")
        query = input()
        # sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"],]
        # for site in sites:
        #     if f"Open {site[0]}".lower() in query.lower():
        #         say(f"Opening {site[0]} sir")
        #         webbrowser.open(site[1])
        # say(query)
        if f"what are you doing".lower() in query.lower():
            say("just chilling sir")

        # if "Using artificial intelligence".lower() in query.lower():
        #     ai(prompt=query)


