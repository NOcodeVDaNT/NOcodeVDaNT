from tkinter import *

def fun():
    print(var1.get())
    lab3.config(text=f"name: {var1.get()}\npassword: {var2.get()}\n {txt1.get("1.0","end")}") #1.0 mean line 1 character 0 to end

win = Tk()
var1 = StringVar()  # Holds the value for the name field
var2 = StringVar()  # Holds the value for the password field

# Name label and entry
lab = Label(win, text="name")
lab.place(x=100, y=80)
name = Entry(win, bd=8, textvariable=var1)  # Link var1 to this Entry
name.place(x=100, y=120)

# Password label and entry
lab2 = Label(win, text="password")
lab2.place(x=100, y=150)
password = Entry(win, show="*", textvariable=var2)  # Link var2 to this Entry
password.place(x=100, y=170)

#addres using teext box
txt1=Text(win,font=(30),height=10)
txt1.place(x=100,y=200)

# Submit button
but = Button(win, text="submit", command=fun)
but.place(x=100, y=400)

# Result label
lab3 = Label(win, text="", relief="raised",anchor="e") #anchor is used to align label inside
lab3.place(x=100, y=450, width=150)

win.mainloop()
