from tkinter import *
top=Tk()
top.title('Welcome_Yousef')
top.geometry('400x500')

name=Label(top,text="Name")
name.grid(row=0,column=0,padx=10,pady=5)
e1=Entry(top)
e1.grid(row=0,column=1)

age=Label(top,text='Age')
age.grid(row=1,column=0,padx=10,pady=5)
e2=Entry(top)
e2.grid(row=1,column=1)

gender=Label(top,text='Gender')
gender.grid(row=2,column=0,padx=10,pady=5)
e3=Entry(top)
e3.grid(row=2,column=1)

btn1=Button(top,text="Submit")
btn1.grid(row=3,column=0)

top.mainloop()
