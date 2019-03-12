from imagesearch import *
import time

time.sleep(2)

pos = imagesearch("./pics/putty.png")
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    # pyautogui.click()
else:
    print("image not found")

# pos = imagesearch("logitech.png")
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")