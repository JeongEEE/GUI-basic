from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+200") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # 창크기조절 불가

txt = Text(root, width=30, height=5) # 여러줄로 입력받을때 text
txt.pack()

txt.insert(END, "글자를 입력하세요") 

e = Entry(root, width=30) # 한줄로 입력받을때 entry
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd() :
	# 내용 출력
	print(txt.get("1.0", END)) # 텍스트에서 값 가져오기
	print(e.get())

	# 내용 삭제
	txt.delete("1.0", END)
	e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
