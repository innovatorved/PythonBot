# waste code

import wikipedia

def wiki(string):
    result = wikipedia.summary(string)
    return string
    
if __name__ == "__main__":
    print(wiki("java"))
