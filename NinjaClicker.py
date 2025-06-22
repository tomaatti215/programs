import pyautogui
import time
import os
import keyboard
import sys
# NinjaClicker - Autoclicker for Popcat
print("welcome to NinjaClicker")
time.sleep(1)
input("press enter to continue")


time.sleep(3)  # Anna 2 sekuntia aikaa siirtää hiiri Popcatin päälle

print("autoclicker is started, you can stop it by pressing alt + F4")

try:
    while True:
        for _ in range(5):
            pyautogui.click()
except KeyboardInterrupt:
    print("autoclicker stopped by user")