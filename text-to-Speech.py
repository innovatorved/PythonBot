# python3 text-to-Speech.py

import pyttsx3

def speakC(rate = 150 , voiceid = 1):
    """
         # Coroutine
         @param : rate = 150 default (Voice Rate per Minute)
         @param : voiceid = 1 default (Voices id 2 Available)

         Execute Snnipt:
             sp = speack()
             next(sp)
             sp.send(__your text message__)
             .
             .
             .
             .In last close the Coroutinne by
             sp.close()
    """
    import pyttsx3
    model = pyttsx3.init()
    model.setProperty("rate" , rate)
    voices = model.getProperty("voices")
    model.setProperty("voice" , voices[0].id)
    while True :
        x = (yield)
        model.say(x)
        model.runAndWait()

"""
To Check Voice avail on System We use
model.getProperty("voices")

and for changing voice we use
model.setProperty("voice" , voices[0].id)

if we want to change volumn rate we use
new = __voice rate per minute__
model.setProperty("rate" , new)
"""

def speak(txt):
    model = pyttsx3.init()
    model.say(txt)
    model.runAndWait()

if __name__ == "__main__":
    model = pyttsx3.init()
    model.say("Hello World")
    model.runAndWait()
