import pyautogui
import time
import numpy as np

leftcorner = [129,135]
rightcorner = [283,285]
pixelval = 0

redtext_coor = (164,9) #color at that point is 170,68,43

print("Automated Script made by Tan Run En (Eric). Press CTRL+C to end the program.")

while(1):
	print("Waiting for ISBN...")
	# Keep taking screenshot until RedText is seen
	while True:
		screen = np.array(pyautogui.screenshot())
		if screen[redtext_coor[0]][redtext_coor[1]][1] < 150:
			print("ISBN Detected")
			break
		time.sleep(0.15)

	time.sleep(0.5)
	print("Selecting the book on table...")
	# Go down the screen to look for highlighted book
	for i in range(404,627,2):
		if(screen[i][119][0] < 160):
			print(screen[i][119])
			highlighted = (119,i+2)
			break

	print("Clicking on the book...")
	# Click on highlighted book
	pyautogui.moveTo(highlighted[0],highlighted[1],duration=0.2)
	pyautogui.click()

	print("Clicking on Book/Course Info...")
	# Click on Book/Course Info
	pyautogui.moveTo(746,505,duration=0.2)
	pyautogui.click()

	print("Waiting for screen to change...")
	# Wait for screen change
	while screen[redtext_coor[0]][redtext_coor[1]][1] < 150:
		screen = np.array(pyautogui.screenshot())
		time.sleep(0.1)

	print("Showing course info for 4 seconds")
	# Show Book Course Info for 4 seconds
	time.sleep(4)

	print("Clicking on Back Button...")
	# Go to back button
	pyautogui.moveTo(683,713,duration=0.2)
	pyautogui.click()
	time.sleep(1)