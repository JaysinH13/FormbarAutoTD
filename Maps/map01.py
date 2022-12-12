import time
import pyautogui


# Follow pyautogui.moveTo(x,y) with a pyautogui.dragTo(x,y, button='left') that way it will drag the towers 


time.sleep(1)
pyautogui.click(966, 960)
pyautogui.click(234, 98)
pyautogui.click(944, 647)
pyautogui.moveTo(472,963)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(384, 635, 0.15)
pyautogui.mouseUp(button='left')
# print(pyautogui.size())
screenSize = pyautogui.size()
# print(screenSize[0], screenSize[1])

if ((screenSize[0] == 1920) and (screenSize[1] == 1080)) :
    print("Correct")
else:
    print("Commit Sepuku") 
