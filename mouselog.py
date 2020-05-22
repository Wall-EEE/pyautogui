import pyautogui
from time import sleep
filename = "test.txt"
with open(filename, 'a') as file:
    while True:
        pos = pyautogui.position()
        file.write(f'{pos[0]}, {pos[1]}\n')
        sleep(0.1)
        print(pos)