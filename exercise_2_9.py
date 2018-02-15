'''
9. See if you can figure out how to compute the response times, measured 
from the onset of the name, to the response (Use psychopy timers)
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
userVar = {'Name':'Enter a first name'}

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()


def sanitize_response(response):
    if response==None:
    	return response
    else:
    	return response[0]

while True:
	dlg = gui.DlgFromDict(userVar)
	if userVar['Name'] not in allnames:
		popupError('Not a valid first name or last name')
	else:
		break


while True:
	nameShown = random.choice(allnames)
	NameStim.setText(nameShown)

	win.flip()
	core.wait(.25)

	FixCross.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	NameStim.draw()
	win.flip()
	responseTimer = core.Clock()

	if userVar['Name']==nameShown:
		correctResponse = 'space'
	else:
		correctResponse = None

	responseReceived= sanitize_response(event.waitKeys(maxWait=1.0, keyList=['space']))
	if responseReceived != None:
		RT = responseTimer.getTime()*1000
	else:
		RT = 'NA'

	if responseReceived==correctResponse:
		isRight=1
		correctFeedback.draw()
	else:
		isRight=0
		incorrectFeedback.draw()

	win.flip()
	core.wait(.5)
	win.flip()

	print isRight, RT