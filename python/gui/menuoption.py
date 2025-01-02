from tkinter import *
def fun(var): #it required some argument to be passed in 
    lb.config(text=value.get())
    
win=Tk()
opt_list=["c#","c++","python","java"]
value=StringVar()
value.set("select laganuge")
op=OptionMenu(win,value,command=fun,*opt_list)
op.pack()

lb=Label(win,text="selected langauage")
lb.pack()

win.mainloop()