import speech_recognition as sr

l = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening .... ")
    l.pause_threshold = 0.5
    audio = l.listen(source)

try :
    print("Recognizing....")
    qr = l.recognize_google(audio ,language="en-in")
    print(qr)
except Exception as e:
    print(e)
except sr.RequestError as e:
    print("Request Error Network Problem")
