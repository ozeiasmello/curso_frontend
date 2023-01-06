from time import time
import pandas as pd
import pyautogui
import pyperclip

pyautogui.PAUSE = 1

#entrar no sistema
#pyautogui.hotkey("Alt","tab")
#pyautogui.hotkey("Ctrl","t")

pyautogui.press("win")

pyautogui.write ("chrome")
pyautogui.press("enter")
pyautogui.alert("Vai começar, aperte OK e não mexa em nada.")
pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press("enter")
pyautogui.sleep(1)
# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=455, y=339, clicks=2)
pyautogui.sleep(1)
pyautogui.click(x=838, y=199, clicks=1)

# Passo 3: Fazer o download do relatório
pyautogui.click(x=891, y=690, clicks=1)


tabela = pandas.read_excel