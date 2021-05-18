def speak(rate = 140 , voiceid = 1):
    """
         # Coroutine
         @param : rate     = 140  default value  (Voice Rate per Minute)
         @param : voiceid  = 0    default value  (Voices id 2 Available)

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
    model.setProperty("voice" , voices[voiceid].id)
    while True :
        x = (yield)
        try :
            model.say(x)
            model.runAndWait()
        except Exception as E:
            print(D)
