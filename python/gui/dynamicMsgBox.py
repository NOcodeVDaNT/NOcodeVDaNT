from tkinter import *
from tkinter.messagebox import askokcancel,askretrycancel
def fun():
    result = askokcancel("Question", "Do you want to quit?")
    print(result)
def fun2():
    result = askretrycancel("Question", "Do you want to retry?")
    if result:
        fun2()
    else:
        askokcancel("Question", "Do you want to quit?")
    
win=Tk()

But=Button(win,text="show_1",command=fun)
But.pack()


But=Button(win,text="show_2",command=fun2)
But.pack()


win.mainloop()