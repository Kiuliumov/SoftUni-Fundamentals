import pyautogui
import keyboard
while True:
    pyautogui.click()
    if keyboard.is_pressed('space'):
        break