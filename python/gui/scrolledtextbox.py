#in scroll bar we have 1st build a txt bx the a scroll bar  and connect them but here we can build it direct
from tkinter import *
from tkinter.scrolledtext import ScrolledText

win =Tk()
ScrolledText_1=ScrolledText(win,height=10,width=50,fg="red",font=(30),bg="black")
ScrolledText_1.pack()

win.mainloop()
