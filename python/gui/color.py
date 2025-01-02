from tkinter import *
from tkinter.colorchooser import askcolor
def fun():
    color = askcolor(title="choose color")
    print(color)
    print(color[1])
    print(color[0])
    win.config(bg=color[1])
win=Tk()

but=Button(win,text="show color",command=fun)
but.pack()

win.mainloop()