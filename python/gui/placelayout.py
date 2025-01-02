from tkinter import *
win=Tk()
win.title("Calculator")

lab1=Label(win,text="ghost1",font=("Time New Roman",20),bg="red")
lab1.place(x=200,y=300,height=100,width=200)#hieght,width is ipadx,ipady

#realtive position with windows size
lab2=Label(win,text="ghost2",font=("Time New Roman",20),bg="yellow")
lab2.place(relx=0.5,rely=0.5,height=100,width=200,anchor="center")#if anchor =centre used the widget consider as dot and place in the given position if not then the top-left corner of the wdidget is placed at the given position
win.mainloop()