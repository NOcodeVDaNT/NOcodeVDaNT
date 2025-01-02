from tkinter import *
def function():
    lab.config(text="vedant")
    if but2.cget("text") == "ON":  # Use cget to check the current text
        but2.config(text="OFF")
    else:
        but2.config(text="ON")
    
win=Tk()
win.title("Calculator")
win.config(bg="red")

photo = PhotoImage(file=r"V:\my codes\python\gui\img.png")
but=Button(win,text="submit",image=photo,font=(30),bg="yellow",cursor="hand2",relief="sunken",compound="left")
but.place(x=100,y=100,width=300,height=100)

but2=Button(win,text="ON",command=function)
but2.place(x=550,y=100,width=300,height=100)

lab=Label(win,text="ghost")
lab.place(x=550,y=250,width=300,height=100)




win.mainloop()