# notes: display is calibrated for 1366 x 768
# pyautogui.displayMousePosition() is a helpful command in the rev loop
import pyautogui
import time
from box import Box


def get_and_send_msg():
    # go to excel to get first name
    pyautogui.click(35, 200)
    time.sleep(1)
    # left 9 times in this case
    pyautogui.press('left', presses=9, interval=.5)
    time.sleep(.5)
    # copy cell
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.5)
    # go back to full name
    pyautogui.press('right', presses=9, interval=.5)
    time.sleep(.5)
    # go to writer
    pyautogui.click(33, 333)
    time.sleep(1)
    # double click name
    pyautogui.doubleClick(376, 294)
    time.sleep(1)
    # paste name
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(.5)
    # backspace to fix \n problem
    pyautogui.press('backspace')
    time.sleep(.5)
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


def log_person():
    # go back to excel
    pyautogui.click(35, 200)
    time.sleep(1)
    # copy name
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    # go to text editor
    pyautogui.click(35, 270)
    time.sleep(1)
    # make a new line on every paste in .txt
    pyautogui.hotkey('ctrl', 'v')
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


print("starting in 10 seconds")
time.sleep(10)

while True:

    # start in excel sheet on name cell
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    #pyautogui.hotkey('alt', 'tab')
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
    #put in time
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
    pyautogui.typewrite('\n', 1)  # hit enter to search
    time.sleep(4)

    # logic for if first button is connect or message
    try:
        x, y = pyautogui.locateCenterOnScreen(
            './images/connect_button.png', grayscale=True)
        pyautogui.click(x, y)
        time.sleep(1.5)
        # if email verif box
        handle_email_verif()
    except TypeError:
        # see if there's a not found
        try:
            x, y = pyautogui.locateCenterOnScreen(
                './images/no_results_found.png', grayscale=False)
            log_person()
        except:
            # click on name to get to profile
            pyautogui.click(x=292, y=400, clicks=1, button='left')
            time.sleep(4)
            # click more
            pyautogui.click(x=873, y=462, clicks=1, button='left')
            time.sleep(1)
            # try and click connect button
            # ? look into need in the haystack
            #region=(950, 700, 100, 100)
            #       left,top,width,height
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    './images/more_connect_button.png', confidence=.5, grayscale=False)
                pyautogui.click(x, y)
                time.sleep(2)
                # false positive on right side
                if x > 950:
                    log_person()
                else:
                    handle_email_verif()

            except TypeError:
                log_person()

    time.sleep(2)
    # go back to excel sheet
    pyautogui.click(35, 200)
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
