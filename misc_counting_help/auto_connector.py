import pyautogui
import time

print("starting in 10 seconds...")
time.sleep(10)
print('now running.')


initial_x, initial_y = pyautogui.position()

# while True:
#     print(pyautogui.position())
#     time.sleep(1)


while True:

    pyautogui.hotkey('command', 'c')
    time.sleep(1)

    pyautogui.hotkey('command', 'tab')

    time.sleep(1)

    pyautogui.click(x=508, y=141, clicks=1, interval=1,
                    button='left')  # linkedin search bar location
    time.sleep(1)

    pyautogui.hotkey('command', 'a')
    time.sleep(1)
    pyautogui.typewrite(['backspace'], 1)
    time.sleep(1)

    pyautogui.hotkey('command', 'v')
    time.sleep(1)

    pyautogui.typewrite('\n', 1)  # hitting enter
    time.sleep(2)
    # connect with the first one shown.
    pyautogui.click(x=1110, y=395, clicks=1, interval=1,
                    button='left')  # hit connect button
    time.sleep(1)
    pyautogui.click(x=1176, y=332, clicks=1, interval=1,
                    button='left')  # need to click done button
    time.sleep(1)
    # need to get back to msg box if it's there
    pyautogui.click(x=1544, y=460, clicks=1, interval=1, button='left')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.hotkey('command', 'tab')  # back to excel sheet
    time.sleep(1)
    # =============
    #initial_y += 15
    # ================
    # pyautogui.press('down')
    # time.sleep(1)
    # ==================
    pyautogui.press('enter')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(1)
