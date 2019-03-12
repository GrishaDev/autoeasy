from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Kontroller
import time
import json
from imagesearch import *


# ===== global variables: =====
mouse = Controller()
keyboard = Kontroller()
shortcutList = []

OFFSET = 5
help = "Welcome to automation of anything, type list to see available commands and exit to exit"
# ==========


# ===== methods: =====
def start():
    # keyboard.press(Key.cmd_l)
    # keyboard.press('r')
    # keyboard.release(Key.cmd_l)
    # keyboard.release('r')

    readConfig()
    print("What would you like to do?")
    while True:
        cmd = input()
        if cmd == "exit":
            break
        elif cmd == "help":
            print(help)
        elif cmd == "list":
            print(getnames())
        else:
            commandParse(cmd)

        print("Anything else?")

def readConfig():
    global shortcutList

    with open('shortcutList.json', 'r') as f:
        shortcutList = json.load(f)

def commandParse(cmd):
    for i in range(len(shortcutList)):
        if cmd == shortcutList[i]['name']:
            print("Executing "+shortcutList[i]['name']+" ..")
            executeCommands(shortcutList[i]['cmds'],shortcutList[i]['repeat'])
            return
    print("Command not found!")

def executeCommands(cmds,repeat):
    for x in range(repeat):
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
            elif(cmds[i]['type'] == "keys"):
                executeKeys(cmds[i]['keys'])
            elif(cmds[i]['type'] == "write"):
                keyboard.type(cmds[i]['write'])
            elif(cmds[i]['type'] == "execute"):
                commandParse(cmds[i]['execute'])
            else:
                print("Error: didn't find "+cmds[i]['type']+" type on your shortcutList.json.")
        print("Finished iteration number "+str(x+1)+" out of "+str(repeat))

def executeKeys(keys):
    for key in range(len(keys)):
        btn = keys[key]
        if not btn.startswith('Key.'):
            keyboard.press(btn)
        else:
            keyboard.press(eval(btn))
    for key in range(len(keys)):
        btn = keys[key]
        if not btn.startswith('Key.'):
            keyboard.release(btn)
        else:
            keyboard.release(eval(btn))

def findPicture(path):
    pos = imagesearch(path)
    if pos[0] != -1:
        print("found! at position: ", pos[0], pos[1])
        mouse.position = (pos[0]+OFFSET, pos[1]+OFFSET)
    else:
        print("Error: didn't find "+str(path)+" on your screen.")

def getnames():
    names = []
    for i in range(len(shortcutList)):
        names.append(shortcutList[i]['name'])
    return names

# ==========

# ===== run: =====
start()
# ==========



# Thanks for drov0 from github for the amazing imagesearch.py


# print('The current pointer position is {0}'.format(
#     mouse.position))