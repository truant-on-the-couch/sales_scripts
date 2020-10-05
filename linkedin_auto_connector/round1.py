import pyautogui
import time

from utility_functions import *


def round1(msgs=bool):
    while True:
        # start in excel sheet on full name cell
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        # click chrome
        pyautogui.click(35, 130)
        time.sleep(2)
        # click search bar
        pyautogui.click(x=345, y=157, clicks=1, button='left')
        time.sleep(1)
        # delete current text
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.typewrite(['backspace'], 1)
        time.sleep(1)
        # put quotes around name
        pyautogui.typewrite('"', .5)
        time.sleep(.5)
        # paste name
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.5)
        pyautogui.typewrite('"', .5)
        time.sleep(.5)
        pyautogui.press('space')
        time.sleep(.5)
        # switch back to excel to get company
        # click calc app
        pyautogui.click(35, 200)
        time.sleep(2)
        # first do date and time entries
        # move over 3 to the right
        pyautogui.press('right', presses=3, interval=.5)
        time.sleep(.5)
        # put in time
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press(';')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        time.sleep(.5)
        # move over left
        pyautogui.press('left')
        time.sleep(.5)
        pyautogui.keyDown('ctrl')
        pyautogui.press(';')
        pyautogui.keyUp('ctrl')
        time.sleep(.5)
        # move over to company cell
        pyautogui.press('left')
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        # move back to name
        pyautogui.press('left')
        time.sleep(.5)
        # go back to chrome
        pyautogui.click(35, 130)
        time.sleep(2)
        # paste company name
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # copy for possible log later
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.5)
        pyautogui.press('enter')  # hit enter to search
        time.sleep(4)

        # logic for if first button is connect or message
        try:
            x, y = pyautogui.locateCenterOnScreen(
                './images/connect_button.png', grayscale=True)
            pyautogui.click(x, y)
            time.sleep(1.5)
            # if email verif box

            handle_email_verif(
                msgs=True) if msgs is True else handle_email_verif()
        except TypeError:
            # see if there's a not found
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    './images/no_results_found.png', grayscale=False)
                log_person()
            except TypeError:
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
                        msgs=True) if msgs is True else check_if_done_button()

                except TypeError:
                    try:
                        x, y = pyautogui.locateCenterOnScreen(
                            './images/more_connect_button.png', confidence=.5, grayscale=False, region=(841, 570, 105, 33))
                        pyautogui.click(x, y)
                        time.sleep(2)
                        check_if_done_button(
                            msgs=True) if msgs is True else check_if_done_button()
                    except TypeError:
                        log_person()

        time.sleep(2)
        # go back to excel sheet
        pyautogui.click(35, 200)
        time.sleep(1)
        # save
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
