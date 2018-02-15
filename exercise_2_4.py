        
''''
4.On each presentation of a name, wait for a response ('f' for first name, 'l' 
for last-name) and only proceed to the next name if the response is correct. 
Hint: if you've done steps 2-3 properly, this should be really easy. 
Refer to the psychopy documentation of event.waitKeys() if you have trouble.
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

while True:
	nameShown = random.choice(allnames)
	NameStim.setText(nameShown)


	if nameShown in firstNames:
		correctResponse='f'
	elif nameShown in lastNames:
		correctResponse='l'
	else:
		print '?'

	FixCross.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	NameStim.draw()
	win.flip()

	event.waitKeys(keyList= [correctResponse])


	if event.getKeys(['q']):
          win.close()
          sys.exit()
     
