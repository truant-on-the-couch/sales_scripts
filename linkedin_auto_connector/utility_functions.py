import pyautogui
import time


def get_and_send_msg():
    # go to writer
    pyautogui.click(33, 333)
    time.sleep(1)
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

    # name with company should already be in clipboard
    time.sleep(1)
    if second_round is True:
        # go to ....
        pyautogui.click(32, 404)
        time.sleep(1)
        # paste
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(.5)
        # save
        pyautogui.hotkey('ctrl', 's')
    else:
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


def handle_email_verif(second_round=bool, msgs=bool):
    # if email verif box
    try:
        x, y = pyautogui.locateCenterOnScreen(
            './images/email_verif_box.png', confidence=.5, grayscale=True)
        pyautogui.press('esc')
        log_person(second_round=True) if second_round is True else log_person()

    except TypeError:
        if msgs is True:
            # still need to click add a note button
            pyautogui.click(820, 340)
            time.sleep(.5)
            get_and_send_msg()
        else:
            # click done button
            pyautogui.click(955, 337)
            time.sleep(1)


def check_if_done_button(second_round=bool, msgs=bool):
    try:
        # did we pull up the box with done button?
        x1, y1 = pyautogui.locateCenterOnScreen(
            './images/done_box.png', confidence=.7, grayscale=False)
        # if yes run handle_email_verif()
        handle_email_verif(msgs=True) if msgs is True else handle_email_verif()
    except:
        log_person(second_round=True) if second_round is True else log_person()
