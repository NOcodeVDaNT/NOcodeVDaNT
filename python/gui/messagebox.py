from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning,askquestion,askyesno

def warning():
    showwarning("Warning", "This is a warning message") #showarning("tittle","message")
    
def error():
    showerror("Error", "This is an error message")#showerror("tittle","message")
    
def info():
    showinfo("Info", "This is an info message")#showinfo("tittle","message")
    
def question():
    askquestion("tittle","your question")
    
def show():
    askyesno("tittle","your question")
    
#return type of askyesno is true false but return type of askquestion is "yes" and "no"
win=Tk()

but_1=Button(win,text="warning",command=warning)
but_1.place(x=100,y=100)

but_2=Button(win,text="error",command=error)
but_2.place(x=300,y=100)

but_3=Button(win,text="info",command=info)
but_3.place(x=500,y=100)


but_4=Button(win,text="show question",command=question)
but_4.place(x=700,y=100)


but_5=Button(win,text="show",command=show)
but_5.place(x=900,y=100)




win.mainloop()