import pyautogui
import time
from utility_functions import *
# this procedure is different in that inner-profile
# connect position is hardcoded.


while True:
    # go to text editor
    pyautogui.click(35, 270)
    time.sleep(1)
    # click 3 times on top line
    pyautogui.click(108, 80, clicks=3, interval=.3)
    time.sleep(1)
    # cut
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(1)
    # go to chrome
    pyautogui.click(35, 130)
    time.sleep(1)
    # click search bar
    pyautogui.click(x=345, y=157)
    time.sleep(1)
    # delete current text
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite(['backspace'], 1)
    time.sleep(1)
    # paste selection
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # enter
    pyautogui.press('enter')
    time.sleep(4)
    # click more
    pyautogui.click(x=873, y=462)
    time.sleep(1)
    # click connect
    pyautogui.click(x=948, y=630)
    time.sleep(1)
    # make sure box with done button is present
    check_if_done_button()
    time.sleep(1)
