from tkinter import *
from tkinter import messagebox

def data_open():
    with open("capital.txt") as file:
        data = file.read()
    result_label.config(text=data)


def data_save():
    idiom = idiom_entry.get()
    capital = capital_entry.get()

    if len(idiom) == 0 or len(capital) == 0 :
        messagebox.showinfo(title="저장실패", message="국가와 수도를 하세요")
    else:
        with open("capital.txt", "a") as file:
            file.write(f"{idiom} : {capital}\n")
    result_label.config(text=f"저장완료\n{idiom} : {capital}")
    idiom_entry.delete(0, END)
    capital_entry.delete(0,END)

def data_find():
    word = idiom_entry.get()
    with open("capital.txt", "r") as file:
        for data in file:
            if word in data:
                result_label.config(text=data)




window=Tk()

img = PhotoImage(file="bgimg.png")
img_label = Label(window, image=img)
img_label.grid(column=0, row=0,columnspan=3)

title_label = Label(window, text="수도", font=("고딕", 20, "bold"))
title_label.grid(column=0, row=1,columnspan=3, pady=20)

idiom_label = Label(window, text = "국가", width=10,
                    font=("고딕",15))
idiom_label.grid(column=0, row=2)

idiom_entry = Entry(window, width=30)
idiom_entry.grid(column=1, row=2)


capital_label = Label(window, text="수도",
                      font=("고딕", 15,))
capital_label.grid(column=0, row=3,)


capital_entry = Entry(window, width=30)
capital_entry.grid(column=1, row=3)

button_open = Button(window, text="불러오기",width=10, font=("고딕",12),
                     bg="yellow", command=data_open)
button_open.grid(column=0, row=4, pady=20)

button_save = Button(window, text="저장",width=10, font=("고딕",12),
                     bg="yellow", command=data_save)
button_save.grid(column=1, row=4, pady=20)

button_find = Button(window, text="검색하기",width=10, font=("고딕",12),
                     bg="yellow", command=data_find)
button_find.grid(column=2, row=4, pady=20)

result_label =Label(window, wraplength=300)
result_label.grid(column=0, row=5, columnspan=3)


window.mainloop()
