from tkinter import *
from tkinter import ttk
def fun(): #no neeed to pass parametre in spinbox
    
    print(str(var.get()))
    

win=Tk()
var=IntVar()
spinbx=ttk.Spinbox(win,from_=0,to=10,textvariable=var,wrap=True,command=fun)  #wrap is responsible for circular movement
spinbx.place(x=10,y=10,height=30,width=100)


win.mainloop()