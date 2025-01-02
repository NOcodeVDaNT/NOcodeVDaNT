from tkinter import *
win=Tk()
win.title("Calculator")
win.geometry("500x500")
win.config(bg="yellow")
var1=StringVar(win,value="vedant\ndahake")
#var2=Stringvar()
#var2.set()
lab1=Label(win,text=var1.get(),font=("Helvetica",30,"bold italic"),bg="red",fg="yellow",cursor="plus",justify="left",relief="raised",underline=1)
#justify will only work when normal text given or given with textvariable=var2


lab1.place(x=250,y=250,anchor="center",width=400)

#image adding
photo = PhotoImage(file=r"V:\my codes\python\gui\img.png")

lab2=Label(win,image=photo)
lab2.place(x=330,y=290,width=300,height=300)


win.mainloop()
