from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showwarning(title="Ошибка!", message='Упс! \n К сожалению я не могу заблокировать виндовс. \n И вообще, зачем ты зашёл сюда?')
window=Tk()
window.title("Winlocker")
window.geometry("777x400")

Label(text="Вы хотите заблокировать виндовс?").pack()
Button(text="Заблокировать виндовс", width='50', height='1', background='red',foreground='yellow',activebackground='yellow',activeforeground="red",command=button_1).pack()


window.mainloop()