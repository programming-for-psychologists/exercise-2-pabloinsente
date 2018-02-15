'''
6. Now, instead of waiting for a response forever, let's implement a timeout. 
Show accuracy feedback as before, but now also show a red 'X' if no response
is received for 1 sec (and go on to the next trial automatically following 
the feedback). (Use psychopy timers)
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

	response= event.waitKeys(maxWait=1.0, keyList= ['f','l'])
	if response==None:
		response='NA'
	else:
		response=response[0]

	if (nameShown in firstNames and response=='f') or (nameShown in lastNames and response=='l'):
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()

	win.flip()
	core.wait(.5)
	win.flip()

	if event.getKeys(['q']):
		break