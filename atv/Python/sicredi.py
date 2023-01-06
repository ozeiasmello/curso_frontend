from pyautogui import moveTo, click
import pyautogui
import time
import keyboard
import random
import win32api, win32con


pyautogui.alert('O codigo ira começar.')
pyautogui.PAUSE = 0.5
pyautogui.press ('winleft') 
pyautogui.write ('chrome')
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.write('https://agentecredenciado.sicredi.com.br/')
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.click(x=377, y=352)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.write('20252405000124')
pyautogui.click(x=609, y=353)
pyautogui.sleep(1)
pyautogui.click(x=456, y=420)
pyautogui.sleep(1)

pyautogui.locateOnScreen('n1.png')
