import time
import pyautogui


# Follow pyautogui.moveTo(x,y) with a pyautogui.dragTo(x,y, button='left') that way it will drag the towers 


# pyautogui.mouseInfo()
time.sleep(5)
pyautogui.click(966, 960)
pyautogui.click(234, 98)
pyautogui.click(944, 647)
pyautogui.moveTo(472,963)
# pyautogui.click(977, 674, duration = 0)
# print(pyautogui.size())
screenSize = pyautogui.size()
# print(screenSize[0], screenSize[1])

if ((screenSize[0] == 1920) and (screenSize[1] == 1080)) :
    print("Correct")
else:
    print("Commit Sepuku") 
