from tkinter import *
from tkinter import messagebox

top=Tk()
top.title('Yousef')
top.geometry('400x500')

def mmm():
    messagebox.showinfo('Secuond Window','You Are in Secound Window')
btn1=Checkbutton(top,text='Red',bg='red',fg='white',activebackground='yellow',command=mmm)
btn1.pack(side=LEFT)

btn2=Checkbutton(top,text='blue',bg='blue',fg='white',command=mmm)
btn2.pack(side=RIGHT)


top.mainloop()