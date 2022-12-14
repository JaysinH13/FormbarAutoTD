import time
import pyautogui


# Follow pyautogui.moveTo(x,y) with a pyautogui.dragTo(x,y, button='left') that way it will drag the towers 

# print(pyautogui.size())
screenSize = pyautogui.size()
# print(screenSize[0], screenSize[1])

if ((screenSize[0] == 1920) and (screenSize[1] == 1080)) :
    print("Correct")
    time.sleep(5)
    pyautogui.click(966, 960)
    pyautogui.click(234, 98)
    pyautogui.click(944, 647)
    pyautogui.click(337, 95)
    pyautogui.moveTo(472,963)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(605,688, 0.15)
    pyautogui.mouseUp(button='left')
    pyautogui.click(605,688)
    print("Basic Tower 1 Placed")
    time.sleep(11)
    pyautogui.click(640,483)
    print("Basic Tower Projectile Bounce Bought")
    time.sleep(8.9)
    pyautogui.click(644,436)
    print("Basic Tower Speed Bought")
    time.sleep(9.1)
    pyautogui.click(650,407)
    print("Basic Tower Range Bought")
    time.sleep(8.6)
    pyautogui.click(659,472)
    print("Basic Tower Strength Bought")
    # pyautogui.click(3407,845)
else:
    print("Commit Sepuku") 