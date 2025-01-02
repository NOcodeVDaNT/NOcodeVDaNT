from tkinter import *
def fun():
    
    new=Toplevel(win)
    new.title("New Window")
    new.geometry("400x400")
    label=Label(new,text="Hello, world!")
    label.pack()
   
    new.mainloop()
    
win=Tk()
but=Button(win,text="new window",command=fun)
but.pack()

win.mainloop()