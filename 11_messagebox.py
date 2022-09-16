from logging import warning
import tkinter.messagebox as msbox # as = 이름변경시 유용
from tkinter import*



root =Tk()
root.title("시흥지 종합복지관")
root.geometry("640x480+600+300")
#기차 예매 시스템이라 가정
def info():
  msbox.showinfo("알림","정상적으로 예매 완료되었습니다.")
  
def warn():
  msbox.showwarning("경고","해당 좌석은 매진 되었습니다.")
  
def error():
  msbox.showerror("에러","결제 오류가 발생하였습니다.")

def okcancel():
  msbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
  
def retrycancel():
  response =msbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 재시도 하겠습니까?")
  if response == 1:
     print("예")
  elif response == 0:
     print("아니요")
def yesno():
  msbox.askyesno("예/ 아니오","해당 좌석은 역방향입니다. 예매하시겠습니까?")
def yesnocancel():
  response =msbox.askyesnocancel(title=None,message="예매 내역이 저장 X \n 저장 후 프로그램 종료하시겠습니까?")
  #네 :저장 후 종료 , 아니오: 저장 X 종료 # 취소: 현재 화면에서 계속 작업
  # True,False,None
  if response == 1:
    print("예")
  elif response == 0:
    print("아니요")
  else:
    print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()