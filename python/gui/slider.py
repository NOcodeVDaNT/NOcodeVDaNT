from tkinter import *
from tkinter import ttk

def show_value(var):
    value_label.config(text=f"Value: {int(slider.get())}")# slider.get() Returns a float

win = Tk()

# Create the Scale widget
slider = ttk.Scale(win, from_=0, to=100, orient="vertical", command=show_value)
slider.place(x=100, y=100, height=300, width=50)

# Create a Label to display the value
value_label = Label(win, text="Value: 0")
value_label.place(x=160, y=240)  # Position the label beside the slider

win.mainloop()
