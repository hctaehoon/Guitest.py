from msilib.schema import CheckBox
from tkinter import*

root =Tk()
root.title("시흥지 종합복지관")
root.geometry("640x480+600+300")


chkvar =IntVar() #chkvar에 int형 (정수)으로 값을 저장한다.
chkbox =Checkbutton(root,text="오늘 하루 보지 않기",variable=chkvar)
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #선택 해제 처리

chkbox.pack()
chkvar2 = IntVar()
chkbox2 =Checkbutton(root, text="일주일 열지 않기",variable=chkvar2)
chkbox2.pack()
def btncmd():
 print(chkvar.get()) # 0:체크해제 , 1:체크완료
 print(chkvar2.get())
btn = Button(root, text="클릭",command=btncmd)
btn.pack()
root.mainloop()