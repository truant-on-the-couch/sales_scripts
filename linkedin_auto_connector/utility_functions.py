import pyautogui
import time
from box import Box


def get_and_send_msg():
    # go to excel to get first name
    # pyautogui.click(35, 200)
    # time.sleep(1)
    # left 9 times in this case
    # pyautogui.press('left', presses=9, interval=.5)
    # time.sleep(.5)
    # copy cell
    # pyautogui.hotkey('ctrl', 'c')
    # time.sleep(.5)
    # go back to full name
    # pyautogui.press('right', presses=9, interval=.5)
    # time.sleep(.5)
    # go to writer
    pyautogui.click(33, 333)
    time.sleep(1)
    # double click name
    # pyautogui.doubleClick(364, 294)
    # time.sleep(1)
    # paste name
    # pyautogui.hotkey('ctrl', 'v')
    # time.sleep(1)
    # backspace to fix \n problem
    # pyautogui.press('backspace')
    # time.sleep(.5)
    # select all
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.5)
    # switch back to chrome
    pyautogui.click(35, 130)
    time.sleep(2)
    # paste selection
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # click done button
    pyautogui.click(955, 450)
    time.sleep(1)


def log_person(second_round=bool):

    # make sure you're on chrome
    pyautogui.click(35, 130)
    time.sleep(1)
    # click search field
    pyautogui.click(345, 157)
    time.sleep(1)
    # select all
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    # copy name
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    if second_round=True:
        #go to ....
        pyautogui.click()
        
    # go to text editor
    pyautogui.click(35, 270)
    time.sleep(1)
    # make a new line on every paste in .txt
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(.5)
    # make a new line
    pyautogui.press('enter')
    time.sleep(.5)
    # save
    pyautogui.hotkey('ctrl', 's')
    time.sleep(.5)


def handle_email_verif():
    # if email verif box
    try:
        x, y = pyautogui.locateCenterOnScreen(
            './images/email_verif_box.png', confidence=.5, grayscale=True)
        pyautogui.press('esc')
        log_person()
    except TypeError:
        # still need to click add a note button
        pyautogui.click(820, 340)
        time.sleep(.5)
        get_and_send_msg()


def check_if_done_button():
    try:
        # did we pull up the box with done button?
        x1, y1 = pyautogui.locateCenterOnScreen(
            './images/done_box.png', confidence=.7, grayscale=False)
        # if yes run handle_email_verif()
        handle_email_verif()
    except:
        log_person()
