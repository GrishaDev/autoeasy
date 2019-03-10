from pynput.mouse import Button, Controller
import time

mouse = Controller()

print("???")

while True:
    print('The current pointer position is {0}'.format(
    mouse.position))
    time.sleep(1)