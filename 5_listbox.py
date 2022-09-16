from tkinter import*
from typing import List

root =Tk()
root.title("시흥지 종합복지관")
# root.geometry("640x480") #가로 세로
root.geometry("640x480+600+300") #플러스는 x,y좌표(실행 시) 

listbox =Listbox(root,selectmode="extended",height=0) #single은 한개만,height 3으로 설정시 3개만보여짐
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()


def btncmd():
  # listbox.delete(0) #0일시 첫번쨰, END 마지막 삭제.
  # print("리스트에는",listbox.size(),"개가 있어요") #size = 갯수표시
  # print("1번째부터 3번째까지의 항목 :",listbox.get(0,2)) 
 #선택된 항목 확인하기.
  # print("선택된 항목: ",listbox.curselection()) #인덱스값으로 출력
  print(listbox.get(listbox.curselection())) #한개만?
btn = Button(root, text="클릭",command=btncmd)
btn.pack()
root.mainloop()