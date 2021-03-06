import pyautogui
import time
from utility_functions import *
# this procedure is different in that inner-profile
# connect position is hardcoded.


def round2(msgs=bool, search_word=str):
    while True:
        # go to text editor
        pyautogui.click(35, 270)
        time.sleep(1)
        # save
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        # click 3 times on top line
        pyautogui.click(127, 78, clicks=3)
        time.sleep(1)
        # cut
        pyautogui.hotkey('ctrl', 'x')
        time.sleep(1)
        # cleanup
        pyautogui.press('down')
        time.sleep(.5)
        pyautogui.press('backspace')
        time.sleep(.5)
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
        pyautogui.write(' '+search_word, interval=.25)
        time.sleep(.5)
        # enter
        pyautogui.press('enter')
        time.sleep(3)
        # see if we have a no_results_found page
        try:
            x, y = pyautogui.locateCenterOnScreen(
                './images/no_results_found.png', grayscale=False)
            log_person(second_round=True)
        except TypeError:
            # for round2, DON"T see if there's a connect button in plain sight
            # try:
            #     x, y = pyautogui.locateCenterOnScreen(
            #         './images/connect_button.png', grayscale=True)
            #     pyautogui.click(x, y)
            #     time.sleep(1.5)
            #     # if email verif box
            #     handle_email_verif(
            #         msgs=True, second_round=True) if msgs is True else handle_email_verif(second_round=True)
            # except TypeError:
            # click on name to get to profile
            pyautogui.click(x=292, y=400, clicks=1, button='left')
            time.sleep(4)
            # click more
            pyautogui.click(x=873, y=462, clicks=1, button='left')
            time.sleep(1)
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    './images/more_connect_button.png', confidence=.5, grayscale=False, region=(841, 610, 105, 33))
                pyautogui.click(x, y)
                time.sleep(2)
                check_if_done_button(
                    second_round=True, msgs=True) if msgs is True else check_if_done_button(second_round=True)
                time.sleep(1)
            except TypeError:
                try:
                    x, y = pyautogui.locateCenterOnScreen(
                        './images/more_connect_button.png', confidence=.5, grayscale=False, region=(841, 570, 105, 33))
                    pyautogui.click(x, y)
                    time.sleep(2)
                    check_if_done_button(
                        second_round=True, msgs=True) if msgs is True else check_if_done_button(second_round=True)
                    time.sleep(1)
                except TypeError:
                    log_person(second_round=True)
