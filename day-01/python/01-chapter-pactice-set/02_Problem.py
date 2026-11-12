# 3. Install an external module and use it to perform an operation of your interest. 

import wikipedia
summary = wikipedia.summary("Python (programming language)", sentences=5)
print(summary)


import pyttsx3 # Text ot Speak Module
import pyttsx3
engine = pyttsx3.init()

engine.say("I am speaking this text")
engine.runAndWait()