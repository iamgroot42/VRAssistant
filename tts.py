#Made by : Rounaq 

import pyttsx
from sys import argv

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def Say(s):
	global engine
	engine.say(s)
	print s
	engine.runAndWait()

Say(argv[1])
