from tkinter import *
from tkinter import messagebox

top=Tk()
top.title('Yousef')
top.geometry('400x500')
lbl=Label(top,text='Size',bg='red',fg='white')
lbl.pack()
scale=Scale(top,from_=100,to=1000,orient=HORIZONTAL)
scale.pack()
top.mainloop()