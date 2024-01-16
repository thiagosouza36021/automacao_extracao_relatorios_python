import pyautogui
import keyboard
from time import sleep
from datetime import datetime
import os

# 1 - abrir o firefox
pyautogui.doubleClick(32,131,duration=2)
# 2 - abrir link sharipoint
pyautogui.click(296,105,duration=8)
# clicar em exportar
pyautogui.click(853,267, duration=2)
# clicar em CSV
pyautogui.click(871,307,duration=2)
# Salvar aquivo
pyautogui.click(667,686, duration=2)
#salvar e substituir
pyautogui.click(726,367,duration=2)

