from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+200") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # 창크기조절 불가

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd() : 
	# progressbar.stop() # 중지
	for i in range(101): # 1~100
		time.sleep(0.01) # 0.01초 대기

		p_var2.set(i) # progress bar 의 값 설정
		progressbar2.update() # ui 업데이트
		print(p_var2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
