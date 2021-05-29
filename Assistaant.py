# Assistant

# Importing Dependencies
from datetime import datetime
from Speakk import speak
from timeSay import timeControl
from wishme import Wishes
from listenn import listen

# initialise Assistant
jiya = speak()       # for speak
next(jiya)           # execute prerequite setting to be executed
t = timeControl()    # for controlling the timeFlow
w = Wishes()         # Initialize wises
l = listen()         # Listen Initialise



# print()
# jiya.send(l.listening)
# jiya.send(w.wish)
# jiya.send(t.time)
# jiya.send(t.date)
# jiya.close()
