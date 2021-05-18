from datetime import datetime
class timeControl:
    def __init__(self):
        pass
    
    @property
    def time(self):
        """
        Return time in
        hour minute and Secound formate
        """
        tm = datetime.now().strftime("%I : %M : %S")
        return f"Time is {tm}"

    @property
    def date(self):
        """
        Return Current Date
        """
        x = datetime.now().strftime("%A , %d-%B-%Y")
        return f"Current Date is {x}"

if __name__ == "__main__":
    t =  timeControl()
    print(t.time)

