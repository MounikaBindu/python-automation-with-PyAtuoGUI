import pyautogui as pg 
import time
time.sleep(2)
#print(pg.position())

#pg.moveTo(763,291)
pg.leftClick(1152,1056,1,1)
time.sleep(1)
pg.typewrite("https://www.instagram.com/direct/inbox/")
time.sleep(1)
pg.press("enter")
time.sleep(4)
pg.leftClick(797,299,1,1)
time.sleep(1)

pg.typewrite("#Hiiii")
time.sleep(2)
pg.press("enter")
time.sleep(2)
for i in range(2):
    pg.typewrite("HLOOO")
    
    pg.press("enter")
    time.sleep(1)
pg.typewrite("Em chestunnav")
pg.press("enter")   


