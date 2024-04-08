# python3 -m ensurepip
# pip install pyautogui

import pyautogui as gui #pyautogui is used for the automation of the keyboard and mouse.
import time #time is used to provide the delay in the execution of the code.


# Open start menu
gui.press('win') #gui is used for the automation of the keyboard and mouse.
time.sleep(0.5)

# Type 'cmd' and open Command Prompt
gui.typewrite('cmd')
time.sleep(0.5) 
gui.press('enter')
time.sleep(0.5) 

gui.typewrite('curl ascii.live/can-you-hear-me')  #typewrite is used to type the text in the command prompt and curl is used to display the parrot.live

gui.press('enter')

