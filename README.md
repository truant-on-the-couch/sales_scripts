Notes:
- these tools were tested on ubuntu 20 lts
- linkedin autoconnector is calibrated for a 1366 x 768 (16:9) resolution.
- the setup_help folder contains screenshots of the required gui config.

Getting started:
1. download and configure virtualbox with ubuntu 20 lts
2. once in ubuntu: run ``` sudo apt-get install featherpad```
3. configure side-dock to look like required_dock_setup.png (found in setup_help folder) by dragging applications (just chrome, calc, text editor, writer, and featherpad) (which means files app must be on top of chrome)
4. make sure you have pip3 installed. Check by running pip3 --version. Otherwise run ```sudo apt-get install python3-pip```
5. then (referring to https://pyautogui.readthedocs.io/en/latest/install.html) run ```python3 -m pip install pyautogui```
6. run ```sudo apt-get install scrot python3-tk python3-dev python3-opencv```
7. make sure chrome tab that is open is on linkedin home page
8. make sure that in your excel sheet the selected cell is on the 'full name' column, and the 'company name' is to the right of it. Refer to calc_setup.png
9. make sure that all applications (chrome, calc, text editor, writer, featherpad) are maximized (but not in fullscreen mode)
10. head on over to TO RUN: section.



Directions for getting dependencies from fresh install of ubuntu:
...


TO RUN:
1. Make sure chrome is on linkedin home page
2. fullname cell is selected with company name to the right of it
3. writer has messaging content in it
4. text editor and featherpad are both open AND have been saved at least once (no untitled docs)
5. all apps are fully enlarged (but not in fullscreen mode)
6. ```cd linkedin_auto_connector``` run ```python3 main.py```
7. select round1 if first round, round2 after round1 is finished
8. you'll have 10 seconds to get back to the calc sheet with cell highlighted on full name to begin on. THIS IS THE STARTING PLACE
9. ~200 leads can take ~3 hours to run. 

TIPS:
- Don't interfere with GUI. You'll screw everything up. If you do screw up the sequence, try and ctrl tab to terminal and then ctrl c
- round2 is different from round1 in that its profile page connect sequence is hardcoded. This can sometimes be helpful due to connect button false positives from the image analyzer. 
- if you need to configure it to a different resolution, change the hardcoded coordinate values by opening a new terminal window, then type ```python3``` -> ```import pyautogui``` -> ```pyautogui.displayMousePosition()```to find mouse positions and change them accordingly for your system
- there is no official finish or done code atm, so take a look at where it's at in the spreadsheet

Improvement:
- It'd be great if it could dynamically configure the hardcoded coordinates based off of display resolution
- An artifical DONE stamp in the excel sheet would be nice