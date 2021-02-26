
import pyautogui
import webbrowser as wb
import time
n=input("text : ")
wb.open (input("enter your link:"))

time.sleep(20)
for i in range(200):
    # pyautogui.typewrite("hi")
    pyautogui.typewrite(n)
    # pyautogui.press("i")
    pyautogui.press("enter")

