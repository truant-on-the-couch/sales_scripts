# notes: display is calibrated for 1366 x 768
# pyautogui.displayMousePosition() is a helpful command in the rev loop
import pyautogui
import time
from box import Box


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
    #pyautogui.write(", ")


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
    # move over to company cell
    pyautogui.press('right')
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
    time.sleep(3)

    # logic for if first button is connect or message
    try:
        x, y = pyautogui.locateCenterOnScreen(
            './images/connect_button.png', grayscale=True)
        pyautogui.click(x, y)
        time.sleep(1.5)
        # if email verif box
        try:
            x, y = pyautogui.locateCenterOnScreen(
                './images/email_verif_box.png', confidence=.5, grayscale=True)
            pyautogui.press('esc')
            log_person()
        except TypeError:
            # still need to click done button
            pyautogui.click(930, 340)
            # safety escape
            pyautogui.press('esc')
    except TypeError:
        # see if there's a not found
        try:
            x, y = pyautogui.locateCenterOnScreen(
                './images/no_results_found.png', grayscale=False)
            log_person()
        except:
            # click on name to get to profile
            pyautogui.click(x=292, y=400, clicks=1, button='left')
            time.sleep(3)
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
                    # still need to click done button
                    pyautogui.click(935, 340)
                    # safety escape
                    pyautogui.press('esc')

            except TypeError:
                log_person()

    time.sleep(2)
    # go back to excel sheet
    pyautogui.click(35, 200)
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)


# extra/broken:
# if pyautogui.locateOnScreen('./images/connect_button.png') == Box(left=1056, top=397, width=105, height=40):
#     button_point = Box(left=1056, top=397, width=105, height=40).center()
#     pyautogui.click(button_point[0], button_point[1])
# elif pyautogui.locateOnScreen('./images/message_button.png') == Box(left=1056, top=397, width=105, height=40):
#         # click name
#         pyautogui.click(x=535, y=403, clicks=1, button='left')
#         time.sleep(3)
#         # click more
#         pyautogui.click(x=1116, y=463, clicks=1, button='left')
#         time.sleep(1)
#         # try and click connect button
#         x, y = pyautogui.locateCenterOnScreen(
#             './images/more_connect_button.png', grayscale=True)
#         if x and y:
#             pyautogui.click(x, y)
#             time.sleep(2)
#             # still need to click done button
#             pyautogui.click(1173, 340)
# else:
#         print("didn't recognize anything")
#         break
