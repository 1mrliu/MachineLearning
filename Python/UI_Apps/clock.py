# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 3:35 PM'

"""
钟表的时间显示
"""
import tkinter
# 获得系统的实际时间
from time import strftime

# initializing the main UI object
top = tkinter.Tk()
# setting title of App
top.title('Clock')
# restricting the resizable property
top.resizable(0, 0)


def time():
    string = strftime('%H:%M:%S %p')
    clockTime.config(text=string)
    clockTime.after(1000, time)

clockTime = tkinter.Label(top, font=('calibri', 40, 'bold'), background='black', foreground='white')

clockTime.pack(anchor='center')
time()

top.mainloop()