

'''
3.Make the program randomly alternate between first names and last names.
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
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
FixCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(allnames)
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