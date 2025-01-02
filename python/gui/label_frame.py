from tkinter import *
win=Tk()
win.title("Calculator")
label_frame=LabelFrame(win,text="tittle",font=(30),labelanchor="ne")
label_frame.place(x=100,y=100,width=500,height=200)

lab1=Label(win,text="button",bg="red",fg="yellow")
lab1.place(x=110,y=150,width=100,height=50)


win.mainloop()