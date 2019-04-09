import pyautogui
import time
import numpy as np
import cv2

leftcorner = [166,170]
rightcorner = [250,156]
pixelval = 0
screen = np.array(pyautogui.screenshot())
redtext_coor = [161,160] #color at that point is 170,68,43
mousespeed = 0.2
loopdelay = 0.15
showcourse_time = 2.5

print("Automated Script made by Tan Run En (Eric). Press CTRL+C to end the program.")

if screen[100][5][0] < 250:
	print("Windowed mode detected")
	leftcorner[0] += 7
	leftcorner[1] += 7
	rightcorner[0] += 7
	rightcorner[1] += 7
	redtext_coor[0] += 7
	redtext_coor[1] += 7

while(1):
	old = screen[rightcorner[1]:leftcorner[1]]
	print("Waiting for ISBN...")
	while True:
		screen = np.array(pyautogui.screenshot())
		new = screen[rightcorner[1]:leftcorner[1]]
		difference = np.sum(np.subtract(old,new))
		print(difference)
		if difference > 100:
			print("ISBN Detected")
			break
		old = new
		time.sleep(loopdelay)

	print("Selecting the book on table...")
	for i in range(404,627,2):
		if(screen[i][119][0] < 160):
			print(screen[i][119])
			highlighted = (119,i+2)
			break

	print("Clicking on the book...")
	pyautogui.moveTo(highlighted[0],highlighted[1],duration=mousespeed)
	pyautogui.click()

	print("Clicking on Book/Course Info...")
	pyautogui.moveTo(746,505,duration=mousespeed)
	pyautogui.click()

	print("Waiting for screen to change...")

	while True:
		screen = np.array(pyautogui.screenshot())
		if screen[redtext_coor[1]][redtext_coor[0]][0] > 200:
			break
		time.sleep(loopdelay)

	print(f"Showing course info for {showcourse_time} seconds")

	time.sleep(showcourse_time)

	print("Clicking on Back Button...")
	pyautogui.moveTo(683,713,duration=mousespeed)
	pyautogui.click()

	while True:
		screen = np.array(pyautogui.screenshot())
		if screen[redtext_coor[1]][redtext_coor[0]][0] < 200:
			break
		time.sleep(loopdelay)
