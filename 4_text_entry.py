from tkinter import*

root =Tk()
root.title("시흥지 종합복지관")
# root.geometry("640x480") #가로 세로
root.geometry("640x480+600+300") #플러스는 x,y좌표(실행 시) 

txt = Text(root,width=30,height=5)
txt.pack()  #글자 작성 가능.

txt.insert(END,"글자 입력하세요")
#미리 글자 넣기
e = Entry(root,width=30)
e.pack() #다른 공간 위치. 차이는 엔터가 안됩니다. 로그인시 사요
e.insert(0, "한 줄만")

#글자가져오기.
def btncmd():
  print(txt.get("1.0",END)) #처음부터 끝까지 라인 1부터 0번째 index 
  print(e.get())
  
  txt.delete("1.0",END)
  e.delete(0,END)
btn = Button(root, text="클릭",command=btncmd)
btn.pack()
root.mainloop()