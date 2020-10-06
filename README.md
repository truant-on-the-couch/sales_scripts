Notes:
- these tools were tested on ubuntu 20 lts
- linkedin autoconnector is calibrated for a 1366 x 768 (16:9) resolution. Use ```VBoxManage controlvm "Name_of_VM" setvideomodehint 1366 768 32``` command on the host machine to set screen size
- the setup_help folder contains screenshots of the required gui config.
- here is a youtube video on how to configure it from scratch: https://www.youtube.com/watch?v=4aofRBBGRpo&feature=youtu.be

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
10. chrome's bookmark bar must be shown
11. head on over to TO RUN: section.

TO RUN:
0. if using virtual box, use ```VBoxManage controlvm "Name_of_VM" setvideomodehint 1366 768 32``` command on the host machine to set screen size
1. make sure chrome is on linkedin home page
2. fullname cell is selected with company name to the right of it
3. writer has messaging content in it
4. text editor and featherpad are both open AND have been saved at least once (no untitled docs) (use .txt format)
5. all apps are fully enlarged (but not in fullscreen mode)
6. ```cd linkedin_auto_connector``` run ```python3 main.py```
7. select round1 for first time usage. Use round2 after text editor list populates via round1.
8. you'll have 10 seconds to get back to the calc sheet with the fullname cell highlighted. This is the starting place for round1. Round2 does not need a starting place.
9. ~200 leads can take ~3 hours to run. 

TIPS:
- Don't interfere with GUI. You'll screw everything up. If you do screw up the sequence, try and ctrl tab to terminal and then ctrl c
- if you need to configure it to a different resolution, change the hardcoded coordinate values by opening a new terminal window, then type ```python3``` -> ```import pyautogui``` -> ```pyautogui.displayMousePosition()```to find mouse positions and change them accordingly for your system
- there is no official finish or done code atm, so take a look at where it's at in the spreadsheet every so often

Improvement:
- It'd be great if it could dynamically configure the hardcoded coordinates based off of display resolution
- An artifical DONE stamp in the excel sheet would be nice

More on round2:
After round1, there may be some cases where a connection invite couldn't be had, likely due to a bad search result. The log made in Text Editor with just the name of the person will be the source for searches done by round2 in addition to the optional searchword specified at launch, e.g. if you have the name joe smith in the Text Editor file, and you entered 'banking', then the round2 search will enter joe smith banking, which can improve results.

Known problems:
- Sometimes the directory for the images in linkedin_auto_connector can have permission problems. Your error would look like: ```OSError: Failed to read ./images/connect_button.png because file is missing, has improper permissions, or is an unsupported or invalid format```, even though it's not actually missing. To fix this, cd to linkedin_auto_connector, then ```mkdir new_images``` -> ```mv images/* new_images``` -> ```rm -rf images``` -> ```mv new_images images```. You can also do this via a gui.

