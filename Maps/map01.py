import time
import pyautogui


# Follow pyautogui.moveTo(x,y) with a pyautogui.dragTo(x,y, button='left') that way it will drag the towers 

# print(pyautogui.size())
screenSize = pyautogui.size()
# print(screenSize[0], screenSize[1])

if ((screenSize[0] == 1920) and (screenSize[1] == 1080)) :
    print("Correct")
    time.sleep(1)
    pyautogui.click(966, 960)
    pyautogui.click(234, 98)
    pyautogui.click(944, 647)
    pyautogui.click(337, 95)
    pyautogui.moveTo(472,963)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(384, 635, 0.15)
    pyautogui.mouseUp(button='left')
    time.sleep(11)
    pyautogui.click(384, 635)
    pyautogui.click(444, 427)
    time.sleep(8.9)
    pyautogui.click(439, 384)
    time.sleep(9.2)
    pyautogui.click(443,420)
    time.sleep(8.3)
    pyautogui.click(430, 348)
    time.sleep(7.4)
    # pyautogui.click(3406, 846)
else:
    print("Commit Sepuku") 
