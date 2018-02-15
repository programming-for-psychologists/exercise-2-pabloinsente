'''
5. Now let's implement some feedback. Let's allow either a 'f' or 'l' response 
for each trial. If the response is correct, show a green 'O' before the start 
of the next trial. If the response is wrong, show a red 'X' (you can use textStim 
objects for feedback). Show the feedback for 500 ms. Note: we have someone in 
a class whose last name is a common first name. If this were an experiment, 
how might this affect responses?
'''


import os 
os.chdir('C:\Users\pablo\Documents\GitHub\exercise-2-pabloinsente')

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names] #append lastname
allnames = firstNames + lastNames

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
FixCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
correctFeedback = visual.TextStim(win,text="O", height=40, color="green",pos=[0,0])
incorrectFeedback = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])

while True:
	nameShown = random.choice(allnames)
	NameStim.setText(nameShown)

	FixCross.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	NameStim.draw()
	win.flip()

	response= event.waitKeys(keyList= ['f','l'])[0]
	if (nameShown in firstNames and response=='f') or (nameShown in lastNames and response=='l'):
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	if event.getKeys(['q']):
		break
