from optparse import Values
import tkinter.ttk as ttk
from tkinter import*

root =Tk()
root.title("시흥지 종합복지관")
root.geometry("640x480+600+300")
values =[str(i) +"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5,values=values)
combobox.pack()
combobox.set("카드결제일")

#콤보박스 내 텍스트 삽입 못하게 하는법.
readonly_combobox = ttk.Combobox(root,height=10, values=values,state="readonly")
readonly_combobox.current(0) #0번째 인덱스값 선택
readonly_combobox.pack()





def btncmd():
 print(combobox.get())
 print(readonly_combobox.get())
btn = Button(root, text="선택",command=btncmd)
btn.pack()
root.mainloop()