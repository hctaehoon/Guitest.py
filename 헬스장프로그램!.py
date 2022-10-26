from tkinter import*
from turtle import color
import pyautogui
import time
import os
from datetime import datetime, timedelta
import tkinter as tk


def 헬스장오픈():
    time.sleep(1)
    pyautogui.click(x=1858, y=932)
    pyautogui.click(x=1858, y=932)
    time.sleep(5)
    pyautogui.click(x=1002, y=563)
    pyautogui.write('a6020933', 0.1)
    time.sleep(1)
    pyautogui.click(x=1010, y=590)
    pyautogui.write('09330933', 0.1)
    time.sleep(1)
    pyautogui.click(x=1082, y=574)
    time.sleep(1)
    pyautogui.click(x=1856, y=843)
    pyautogui.click(x=1856, y=843)


def refund():

    print("환불 요청 날짜를 입력하세요(EX)20221026)")
    date = datetime.strptime(str(input()), "%Y%m%d")
    print("만료 날짜를 입력하세요(EX)20221026)")
    date2 = datetime.strptime(str(input()), "%Y%m%d")
    # date2 = date + timedelta(days=int(input()))
    # print(date2)

    date3 = days = (date2 - date)
    a = (date3.days)
    print("결제 금액을 입력하세요 ex > 125000")
    b = int(input())
    print("이용일수를 입력하세요 ex > 90")
    c = int(input())
    # b = 125000
    # c = 90

    d = (round(b/c)*a)
    f = b*0.1
    print("환불 받으실 금액은 {}원 입니다.".format(d-f))

    input()

    # 환불요청 날짜20220101 , 만료일자 20220130, 결제 금액 b , 이용 기간c
    import turtle as myTurtle

    n = 64

    myTurtle.shape('turtle')

    myTurtle.mainloop()


gui = Tk(className='헬스장')
gui.geometry("150x200+1300+500")

gui['background'] = 'tomato'


button1 = Button(gui, text="헬스장 오픈", width=20, height=2, command=헬스장오픈)
button1.pack()
button2 = Button(gui, text="환불 계산기", width=20,
                 height=2, command=refund)
button2.pack()
button3 = Button(gui, text="마스크 안내 방송", width=20, height=2)
button3.pack()
button4 = Button(gui, text="주차장 안내 방송", width=20, height=2)
button4.pack()
button5 = Button(gui, text="소방점검 안내 방송", width=20, height=2)
button5.pack()


gui.mainloop()
