import pyautogui
import time

time.sleep(5)

try:
    for pos in pyautogui.locateAllOnScreen('/home/michel/sales_scripts/linkedin_auto_connector/images/connect_button.png'):
        print(pos)

except TypeError:
    print("couldn't find anything")

try:
    x, y = pyautogui.locateCenterOnScreen(
        '/home/michel/sales_scripts/linkedin_auto_connector/images/add_a_note_button.png', confidence=.7)
    pyautogui.moveTo(x, y)
except TypeError:
    print("not found")


#region=(837, 521, 101, 25)
#Box(left=837, top=617, width=101, height=25)
# to get the more difficult inner connect:
# test this region too
# Box(left=841, top=570, width=105, height=33)
