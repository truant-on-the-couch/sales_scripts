# start where withdraw buttons are located.

import pyautogui
import time

# 99 people can fill up one linkedin withdraw page screen
# BUT it auto adds more people

i = 99


print('beginning auto withdraw')
time.sleep(10)

while i > 0:
    pyautogui.click(875, 420)
    time.sleep(1)
    pyautogui.click(815, 465)
    time.sleep(2)

