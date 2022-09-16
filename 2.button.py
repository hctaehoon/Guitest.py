from tkinter import*

root =Tk()
root.title("시흥지 종합복지관")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5,pady=10,text="버튼233333") #pad x크기 y크기
btn2.pack()

btn3 = Button(root, padx=10,pady=5,text="버튼3")
btn3.pack()

btn4 = Button(root,width=10,height=3,text="버튼44444444444")
btn4.pack()
#width,heiht 는 고정값, padx,y는 여백

btn5 = Button(root, fg="red",bg="yellow",text="버튼5")
btn5.pack()

photo= PhotoImage(file="C:/Users/user/Desktop/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
  print("버튼이 클릭 되었어요")
btn7 =Button(root, text ="동작 버튼",command=btncmd)
btn7.pack()





root.mainloop()