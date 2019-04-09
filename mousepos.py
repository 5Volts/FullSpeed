import pyautogui
import numpy as np
x,y = pyautogui.position()
screen = np.array(pyautogui.screenshot())
print(x,y)
print(screen[y][x])
#402 - 627
