import pyautogui
import os
import time
#import msvcrt
from PIL import ImageGrab

os.system('mode con: cols=20 lines=5')

while True:
#    os.system('cls' if os.name == 'nt' else 'clear')
    x = pyautogui.position()
    image = ImageGrab.grab()
    print(x)
    color = image.getpixel(x)
    print(color)
#   if msvcrt.kbhit():
#        key = msvcrt.getch()
#        input("Paused. Press Ctrl + C to exit or Enter to continue...")
    time.sleep(0.2)

