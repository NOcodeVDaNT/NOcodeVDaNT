from tkinter import *
win=Tk()
win.title("Calculator")

var1=StringVar(win,value="ghost")
print(var1) #encrypted data
print(var1.get())
print(var1.set("vedant"))
print(var1.get())

var2=IntVar(win,value=90)
print(var2.get())

var3=BooleanVar(win,value=True)
print(var3.get())

var4=DoubleVar(win,value=90.9999)
print(var4.get())


win.mainloop()


