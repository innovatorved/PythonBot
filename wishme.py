from random import randint
from datetime import datetime
class Wishes:
    def __init__(self):
        self.dic = ["{} Sir ! I am here to Help You" , "{} Sir Glad to See You"]
        # print(random.randint(3, 9)) 

    @property
    def wish(self):
        w = randint(0 , 1)
        t = int(datetime.now().strftime("%I"))

        if t >=6 and t < 12:
            return self.dic[w].format("Good Morning")
        elif t>=12 and t<=17:
            return self.dic[w].format("Good AfterNoon")
        elif t>=17 and t<24:
            return self.dic[w].format("Good Evening")
        else:
            return self.dic[w].format("Good Everning") + " But I think You Want to Sleep Time is So late"

if __name__ == "__main__":
    w = Wishes()
    print(w.wish)
