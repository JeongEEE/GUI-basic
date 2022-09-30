from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+200") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # 창크기조절 불가

def info():
	msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
	msgbox.showwarning("경고", "해당좌석은 매진되었습니다.")

def error():
	msgbox.showerror("에러", "오류가 발생하였습니다!")

def okcancle():
	msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매 하시겠습니까?")

def retrycancle():
	response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
	if response == 1: # 재시도 
		print("재시도")
	elif response == 0: # 취소
		print("취소") 

def yesno():
	msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
	response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n저장하시겠습니까?")
	# 네:저장후 종료
	# 아니오:저장 하지않고 종료
	# 취소:프로그램 종료 취소(현재화면에서 계속)
	print("응답:", response) 

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancle, text="확인 취소").pack()
Button(root, command=retrycancle, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()
