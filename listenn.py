import speech_recognition as sr

class listen:
    def __init__(self):
        self.lis = sr.Recognizer()

    @property
    def listening(self):
        with sr.Microphone() as source: # Microphone open
            print("Listening .... ")
            self.lis.pause_threshold = 0.5 # stop for 0.5 sec
            audio = self.lis.listen(source)

        try :
            print("Recognizing....")
            qr = self.lis.recognize_google(audio ,language="en-in")
            return qr
        
        except sr.RequestError as e:
            print("Request Error Network Problem")
            return listen().listening
        
        except Exception as e:
            print(e)
            return listen().listening
    
