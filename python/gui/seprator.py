from tkinter import *
from tkinter import ttk  # ttk module for separator

win = Tk()

Label1 = Label(win, text="ghost")
Label1.pack()

# Create a separator
sep = ttk.Separator(win, orient="horizontal")
sep.pack(fill="x", pady=5)  # fill the separator horizontally with padding

Label2 = Label(win, text="vedant")
Label2.pack()

win.mainloop()
