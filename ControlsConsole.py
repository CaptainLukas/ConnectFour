import keyboard
import _thread
import sys
from msvcrt import getch
#https://pypi.org/project/keyboard/
#https://stackoverflow.com/questions/24072790/detect-key-press-in-python

def keypress():
    global char
    char = getch()

def GetUserinput():
    #keyboard.wait('1')

    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('You Pressed A Key!')
                break  # finishing the loop
        except:
            pass
    return