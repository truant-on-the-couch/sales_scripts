# notes: display is calibrated for 1366 x 768
# pyautogui.displayMousePosition() is a helpful command in the rev loop
import pyautogui
import time
from box import Box

from utility_functions import *
from round1 import *
from round2 import *


round = input(
    "Welcome. Press control c to cancel.\n Enter 'round1' or 'round2'\n")
if round == 'round1':
    print("you entered %s.", round)
    print("you have 10 seconds to make sure that all startup conditions are set. Refer to README if unsure.")
    round1()
else:
    print("you entered %s.", round)
    print("you have 10 seconds to make sure that all startup conditions are set. Refer to README if unsure.")
    time.sleep(10)
    round2()
