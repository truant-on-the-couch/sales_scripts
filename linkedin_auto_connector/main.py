# notes: display is calibrated for 1366 x 768
# pyautogui.displayMousePosition() is a helpful command in the rev loop
import pyautogui
import time

from utility_functions import *
from round1 import *
from round2 import *

print("Welcome. Press control c to cancel.\n")
msgs = input(
    "do you want to add msgs with your connect invitations? Enter 'yes' or 'no'\n")
print("you entered ", msgs)
round = input(
    "Enter 'round1' or 'round2'\n")
if round == 'round1':
    print("you entered ", round)
    print("you have 10 seconds to make sure that all startup conditions are set. Refer to README if unsure.")
    time.sleep(10)
    round1(msgs=True) if msgs == 'yes' else round1()
else:
    print("you entered ", round)
    search_word = input(
        "enter an additonal search item to be placed after name. E.g. security, which gives: Joe Smith security. Press enter to leave blank\n")
    print("you have 10 seconds to make sure that all startup conditions are set. Refer to README if unsure.\n")
    time.sleep(10)
    round2(msgs=True, search_word=search_word) if msgs == 'yes' else round2(
        search_word=search_word)
