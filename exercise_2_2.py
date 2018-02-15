
'''
2.Open names.txt to see what the names list looks like. Make the script show last
 names instead of first names (don't change the names.txt file).
 '''
 
import os 
os.chdir('C:\Users\pablo\Documents\GitHub\exercise-2-pabloinsente')

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names] #append lastname

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
FixCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(lastNames)
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