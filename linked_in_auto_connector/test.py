import pyautogui
import time

time.sleep(5)
try:
    x, y = pyautogui.locateCenterOnScreen(
        './images/not_found.png', grayscale=False)
    pyautogui.moveTo(x, y)
except TypeError:
    print("not found")
