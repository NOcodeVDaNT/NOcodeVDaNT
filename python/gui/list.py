from tkinter import *
from tkinter import ttk

def fun():
    lab.config(text=var.get())
    

win=Tk()
var=StringVar()

list_1=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]

list=ttk.Combobox(win,values=list_1,textvariable=var,font=(30))
list.set("select month")
list.place(x=100,y=100,height=50,width=150)

lab=Label(win,text="")
lab.place(x=100,y=170)

but=Button(win,text="submit",command=fun)
but.place(x=270,y=112)

win.mainloop()