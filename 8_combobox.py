from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+200") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # 창크기조절 불가

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height= 5, values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height= 10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 값 선택
readonly_combobox.pack()

def btncmd() : 
	print(combobox.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
