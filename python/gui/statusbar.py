from tkinter import *

def fun():  
    # Toggle status bar text
    current_text = status_bar.cget("text")  # Get the current text of the label
    if "OFF" in current_text:
        status_bar.config(text="status bar\t\t\t\t\t\t\t\t\t\tON")
    else:
        status_bar.config(text="status bar\t\t\t\t\t\t\t\t\t\tOFF")

win = Tk()

# Create status bar label
status_bar = Label(win, text="status bar\t\t\t\t\t\t\t\t\t\tOFF", relief="sunken", anchor="w", bd=8, height=1)
status_bar.pack(side="bottom", fill="x")

# Create button
but = Button(win, text="submit", command=fun)
but.place(x=300, y=300)

win.mainloop()
