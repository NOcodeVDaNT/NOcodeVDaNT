from tkinter import *

def fun():
    lab.config(text=var.get())

def deselect_all():
    var.set("")  # Clear the selection

win = Tk()
list = (("large", "xxl"), ("medium", "xl"), ("small", "l"))
var = StringVar()

# Position each radio button using `place`
y_position = 10  # Starting Y-coordinate
for i in list:
    Radiobutton(win, text=i[0], variable=var, value=i[1]).place(x=10, y=y_position)
    y_position += 30  # Increment Y-coordinate for the next button

but = Button(win, text="Submit", command=fun)
lab = Label(win, text="Your size")
deselect_but = Button(win, text="Deselect All", command=deselect_all)

lab.place(x=10, y=130)
but.place(x=10, y=150)
deselect_but.place(x=10, y=180)

win.mainloop()
