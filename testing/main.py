import pyautogui
import time

time.sleep(5)

try:
    for pos in pyautogui.locateAllOnScreen('./../linkedin_auto_connector/images/end_calc.png'):
        print(pos)
except TypeError:
    print("couldn't find anything")

# try:
#     x, y = pyautogui.locateCenterOnScreen(
#         './../linkedin_auto_connector/images/more_connect_button.png', confidence=.5, grayscale=False, region=(841, 610, 105, 33))
#     pyautogui.moveTo(x, y)
# except TypeError:
#     print("not found")


# to get the more difficult inner connect:
# test this region too
# Box(left=841, top=570, width=105, height=33)
