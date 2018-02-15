'''         
7. Pop up a box that accepts a first name, and check to make sure that the name exists.
If it doesn't, pop-up a 'Name does not exist'error box
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


while True:
	dlg = gui.DlgFromDict(userVar)
	if userVar['Name'] not in firstNames:
		popupError('Not a valid first name')
	else:
		break


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