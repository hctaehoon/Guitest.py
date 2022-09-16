from tkinter import*

root =Tk()
root.title("시흥지 종합복지관")
root.geometry("640x480+600+300")
label1 =Label(root, text="안녕하세요")
label1.pack() #버튼과 다르게 글만 나옴.

photo =PhotoImage(file="C:/Users/user/Desktop/img.png")
# 컨트롤 F2 활용 \를 /로 변경
label2 =Label(root, image=photo)
label2.pack()

def change():
  label1.config(text="또 만나요") #config 변경?
  
  global photo2
  photo2 =PhotoImage(file="C:/Users/user/Desktop/img2.png") #글로벌 선언해야 안지움
  label2.config(image=photo2)
btn = Button(root, text="클릭",command=change)
btn.pack()
root.mainloop()