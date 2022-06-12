# program to spam a lot of messages

import pyautogui
import time

msg = input("Enter the message: ")
n = input("How many times ?: ")

i = 0

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Lesssgoooo!!!!")

# It will write the messages where the insertion point is
while(int(n) >= int(i)):	
	pyautogui.typewrite(str(msg))
	pyautogui.press("enter")
	i = i + 1

#code from https://medium.com/@junaidrahim/a-dead-simple-spammer-in-python-5d539f75342f modified by ME