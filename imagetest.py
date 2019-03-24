from imagesearch import *
import time

# time.sleep(2)

start = time.time()
try:
    pos = pyautogui.locateCenterOnScreen('pics/discord/minimize.png')
    pyautogui.moveTo(pos[0], pos[1])
except:
    print("image not found")
end = time.time()
print(end - start)




# start = time.time()
# x,y = pyautogui.locateCenterOnScreen('pics/discord/minimize.png')
# pyautogui.moveTo(x, y)
# end = time.time()
# print(end - start)


# start = time.time()
# pos = imagesearch("pics/discord/minimize.png")
# pyautogui.moveTo(pos[0], pos[1])
# end = time.time()
# print(end - start)

# pos = imagesearch("pics/discord/minimize.png")
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
#     # pyautogui.click()
# else:
#     print("image not found")

# pos = imagesearch("logitech.png")
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")

#            {"type":"keys","keys":["Key.cmd_l","Key.shift_l","Key.left"]},
#{"type":"find","pic":"pics/reaction/continue.png"},









#====================================================================================
#============ find picture old method

    # pos = imagesearch(path)
    # if pos[0] != -1:
    #     print("found! at position: ", pos[0], pos[1])
    #     mouse.position = (pos[0]+OFFSET, pos[1]+OFFSET)
    # else:
    #     print("Error: didn't find "+str(path)+" on your screen.")


#============ find wait picture old method
    # pos = imagesearch(path)
    # count = 0
    # seconds = 0
    # while pos[0] == -1:
    #     time.sleep(0.01)
    #     pos = imagesearch(path)
    #     count = count + 1
    #     if count >= 100:
    #         seconds = seconds + 1
    #         count = 0
    #         print("Still Waiting for the picture to appear already..")
    # print("found! at position: ", pos[0], pos[1])
    # mouse.position = (pos[0]+OFFSET, pos[1]+OFFSET)