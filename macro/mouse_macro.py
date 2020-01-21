# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:34:58 2020

@author: dohee
"""

from tkinter import *
from tkinter import ttk
from pynput import mouse
import pyautogui
 
root = Tk()
root.title("마우스 좌표 찾기")
root.geometry("350x100")
 
########################################
label1 = Label(root, text = "X좌표")
label1.grid(row=1, column=1)
 
entry1 = Entry(root, width=10 )
entry1.grid(row=1, column=2)
 
label2 = Label(root, text = "Y좌표")
label2.grid(row=1, column=3)
 
entry2 = Entry(root, width=10 )
entry2.grid(row=1, column=4)
 
button1 = Button(root, text="마우스위치", command = lambda:aaa())
button1.grid(row=1, column=5)
 
############################################
 
label3 = Label(root, text = "반복횟수")
label3.grid(row=2, column=1)
 
entry3 = Entry(root, width=10)
entry3.grid(row=2, column=2)
entry3.insert('end','100')
###########################################
 
button2 = Button(root, text="클릭 시작", command = lambda:click_m())
button2.grid(row=3, column=3)
 
########################################  
def aaa():
    with mouse.Listener(
        on_click=bbb
        ) as listener:
        listener.join()
    entry1.insert("end",x1)
    entry2.insert("end",y1)
 
def bbb(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        x1 = x
        y1 = y
        
    if not pressed :
        return False
 
def ccc():
    entry1.insert("end",x1)
    entry2.insert("end",y1)
 
 
def click_m():
    click_num = int(entry3.get())
 
    ##반복시작
    for a in range(0,click_num):
        pyautogui.click(x1,y1)
        
root.mainloop()

import time

for i in range(5):
    print(i)
    time.sleep(1)
