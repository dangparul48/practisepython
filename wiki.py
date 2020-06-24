import wikipedia as wiki
import pyttsx3 as tts
import speech_recognition as sr


def speak(content):
    eng = tts.init()
    eng.setProperty("rate", 95)
    eng.setProperty("voice", eng.getProperty("voices")[1].id)
    eng.say(content)
    eng.runAndWait()


def greetings():
    line = "Hi Dear, I'm a Wikipedia bot! What do you want me to search?"
    print(line)
    speak(line)


def ask_query():
    recognizer = sr.Recognizer()
    query = ""
    with sr.Microphone() as src:
        audio = recognizer.listen(src)
        query = recognizer.recognize_google(audio)

    print(query)
    return query


def get_summary(query):
    query_summary = wiki.summary(query, sentences=5)
    print(query_summary)
    speak(query_summary)


greetings()
summary = ask_query()
get_summary(summary)