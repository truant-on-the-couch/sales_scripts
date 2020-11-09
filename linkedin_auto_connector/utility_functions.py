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
    # pyautogui.click(955, 450)
    # click done button
    try:
        x, y = pyautogui.locateCenterOnScreen(
            '/home/michel/sales_scripts/linkedin_auto_connector/images/send_button.png')
        pyautogui.click(x, y)
        mark_with_an_x()

    except TypeError:
        # click send button manually
        #pyautogui.click(930, 450)
        print('couldnt find send button')

    time.sleep(1)


def log_person(second_round=bool):

    if second_round is True:
        # should already have name in clipboard
        # go to FeatherPad
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
        # need to go to excel to get name again
        pyautogui.click(35, 200)
        time.sleep(1)
        # should be on name cell
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.5)
        # go to text editor
        pyautogui.click(35, 270)
        time.sleep(1)
        # make a new line on every paste in .txt
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.5)
        # make a new line
        # don't need it anymore I guess.
        # pyautogui.press('enter')
        # time.sleep(.5)
        # save
        pyautogui.hotkey('ctrl', 's')
        time.sleep(.5)


def handle_email_verif(second_round=bool, msgs=bool):
    # if email verif box
    try:
        x, y = pyautogui.locateCenterOnScreen(
            '/home/michel/sales_scripts/linkedin_auto_connector/images/email_verif_box.png', confidence=.5)
        # go to excel
        pyautogui.click(35, 200)
        time.sleep(1)
        # go one cell left to email
        pyautogui.press('left')
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.5)
        # go back to name cell
        pyautogui.press('right')
        time.sleep(.5)
        # go to chrome
        pyautogui.click(35, 130)
        time.sleep(.5)
        # click on email box
        pyautogui.click(634, 306)
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.5)
        # click add a note
        pyautogui.click(816, 389)
        time.sleep(.5)
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
        time.sleep(1)
        # paste selection
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # see if send button is blue
        try:
            # is the send button blue?
            x1, y1 = pyautogui.locateCenterOnScreen(
                '/home/michel/sales_scripts/linkedin_auto_connector/images/send_button.png', confidence=.8)
            pyautogui.click(x1, y1)
            time.sleep(2)
            mark_with_an_x()
        except TypeError:
            pyautogui.press('esc')
            log_person(
                second_round=True) if second_round is True else log_person()

    except TypeError:
        if msgs is True:
            # still need to click add a note button
            # used to be: pyautogui.click(820, 340)
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    '/home/michel/sales_scripts/linkedin_auto_connector/images/add_a_note_button.png', confidence=.7)
                pyautogui.click(x, y)

            except TypeError:
                # click add a note button manually
                print('couldnt find add a note button')
                #pyautogui.click(815, 333)

            time.sleep(.5)
            get_and_send_msg()
        else:
            # click send button
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    '/home/michel/sales_scripts/linkedin_auto_connector/images/send_button.png')
                pyautogui.click(x, y)
                mark_with_an_x()

            except TypeError:
                # click send button manually
                #pyautogui.click(930, 311)
                # mark_with_an_x()
                print('couldnt find send button')

            time.sleep(1)


def check_if_done_button(second_round=bool, msgs=bool):
    try:
        # did we pull up the box with add|send button?
        pyautogui.locateCenterOnScreen(
            '/home/michel/sales_scripts/linkedin_auto_connector/images/done_box.png', confidence=.7, grayscale=False)
        # if yes run handle_email_verif()
        handle_email_verif(msgs=True) if msgs is True else handle_email_verif()
    except TypeError:
        log_person(second_round=True) if second_round is True else log_person()


def mark_with_an_x():
    # click calc
    pyautogui.click(34, 204)
    time.sleep(.5)
    pyautogui.press('right', presses=4, interval=.5)
    time.sleep(.5)
    pyautogui.typewrite('x')
    time.sleep(.5)
    pyautogui.press('left', presses=4, interval=.5)
    time.sleep(.5)
