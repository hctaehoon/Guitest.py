from optparse import Values
import tkinter.ttk as ttk
from tkinter import*
import time

root =Tk()
root.title("시흥지 종합복지관")
root.geometry("640x480+600+300")

# progressbar = ttk.Progressbar(root, maximum=100,mode="determinate") #결정되지않다 indeterminate determinate><
# progressbar.start(10) #10미리 세컨드마다 움직임.
# progressbar.pack()


p_var2 = DoubleVar() 
progressbar = ttk.Progressbar(root, maximum=100, length=150 ,variable=p_var2)
progressbar.pack()


def btncmd2():
 for i in range(101):
   time.sleep(0.01)
   
   p_var2.set(i)
   progressbar.update() #업데이트 해줘야함
   print(p_var2.get()) #숫자 나오게.
   
   
btn = Button(root, text="시작",command=btncmd2)
btn.pack()
root.mainloop()