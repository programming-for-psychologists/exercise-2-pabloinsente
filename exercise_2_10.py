'''
10. Output the response times (in ms, e.g., 453 for 453 ms) and accuracy 
(1 for correct, 0 for incorrect) to a file output.txt. 
Output one line per trial: each line should contain the accuracy 
(1 or 0) and the response time (in milliseconds). See the python
documentation for examples of how to write to a file. Ask for help if you are stuck.
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
output_file = open("output.txt","w")

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
    
	dataString = '\t'.join((str(isRight),str(RT)))
	output_file.write(dataString+'\n')
	output_file.flush() #flushes the file buffer to the file. Without this, data to the file is only written once the file is closed.

output_file.close()

