from re import L
from tkinter import*
from venv import create


root =Tk()
root.title("시흥지 종합복지관")
root.geometry("640x480+600+300")

def create_new_file():
  print("새 파일을 만듭니다.")

menu = Menu(root)
#파일메뉴
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_command(label="")
menu_file.add_separator() #구분자
menu_file.add_command(label="open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All",state = "disable") #비활성호
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="Flie", menu=menu_file)
#Edit 메뉴(빈 값)

menu.add_cascade(label="Edit")

#Language 메뉴 추가  라디오 버튼으로
menu_lang = Menu(menu, tearoff=0) #tearoff(언어)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

#chkbox도 가능.View 메뉴 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View",menu=menu_view)




root.config(menu=menu)
root.mainloop()