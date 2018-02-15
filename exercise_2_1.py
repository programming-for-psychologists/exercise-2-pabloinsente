'''
1. Create a fixation cross using a TextStim object visual.TextStim set text to"+" and color to "white". 
Make the fixation cross appear for 500 ms before each name and disappears right before the name comes up.
'''

import os 
os.chdir('C:\Users\pablo\Documents\GitHub\exercise-2-pabloinsente')

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
FixCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    
    FixCross.draw()
    win.flip()
    core.wait(0.5)
    win.flip()
    
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        win.close()
        sys.exit()