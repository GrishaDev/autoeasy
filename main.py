from pynput.mouse import Button, Controller
import time
import json
from imagesearch import *


# ===== global variables: =====
mouse = Controller()
shortcutList = []

OFFSET = 5
# ==========


# ===== methods: =====
def start():
    readConfig()
    print("What would you like to do?")
    while True:
        cmd = input()
        commandParse(cmd)
        print("Anything else?")

def readConfig():
    global shortcutList

    with open('shortcutList.json', 'r') as f:
        shortcutList = json.load(f)

def commandParse(cmd):
    for i in range(len(shortcutList)):
        if shortcutList[i]['name'] == cmd:
            executeCommands(shortcutList[i]['cmds'])
            return
    print("Command not found!")

def executeCommands(cmds):
    for i in range(len(cmds)):
        if(cmds[i]['type'] == "go"):
            mouse.position = (cmds[i]['x'], cmds[i]['y'])
        elif(cmds[i]['type'] == "find"):
            findPicture(cmds[i]['pic'])
        elif(cmds[i]['type'] == "click"):
            mouse.click(Button.left, 1)
        elif(cmds[i]['type'] == "doubleclick"):
            mouse.click(Button.left, 2)
        elif(cmds[i]['type'] == "wait"):
            time.sleep(cmds[i]['seconds'])

def findPicture(path):
    pos = imagesearch(path)
    if pos[0] != -1:
        print("found! at position: ", pos[0], pos[1])
        mouse.position = (pos[0]+OFFSET, pos[1]+OFFSET)
    else:
        print("image not found")

# ==========

# ===== run: =====
start()
# ==========



# Thanks for drov0 from github for the amazing imagesearch.py


# print('The current pointer position is {0}'.format(
#     mouse.position))