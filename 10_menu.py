from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+200") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # 창크기조절 불가

def create_new_file():
	print("새 파일을 만듭니다.")

menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새 파일", command=create_new_file)
menu_file.add_command(label="새 창")
menu_file.add_separator() # 구분선
menu_file.add_command(label="파일 열기")
menu_file.add_separator() # 구분선
menu_file.add_command(label="파일 저장", state="disable")
menu_file.add_separator() # 구분선
menu_file.add_command(label="종료", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")

# 라디오 버튼을 통해서 택1
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="파이썬")
menu_lang.add_radiobutton(label="자바")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="언어", menu=menu_lang)

# view 메뉴
menu_view= Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="미니맵 보기")
menu.add_cascade(label="보기", menu=menu_view)

root.config(menu=menu)
root.mainloop()
