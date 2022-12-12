import time
import pyautogui


# time.sleep(5)


# Follow pyautogui.moveTo(x,y) with a pyautogui.dragTo(x,y, button='left') that way it will drag the towers 


# pyautogui.click(977, 674, duration = 0)
# pyautogui.click(977, 674, duration = 0)
# print(pyautogui.size())
screenSize = pyautogui.size()
# print(screenSize[0], screenSize[1])

if ((screenSize[0] == 1920) and (screenSize[1] == 1080)) :
    print("Correct")
else:
    print("Commit Sepuku") 
