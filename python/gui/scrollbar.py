from tkinter import *

win = Tk()

# Create a Text widget
test = Text(win, height=8)
test.place(x=0, y=0, width=300, height=170)

# Create a Scrollbar
scrollbar = Scrollbar(win, orient="vertical", command=test.yview)
scrollbar.place(x=300, y=0, height=170)

# Set the Scrollbar's appearance (workaround for bg and relief)
scrollbar.config(bg="red", relief="sunken")  # This line is unlikely to have a visible effect
scrollbar['activebackground'] = "yellow"  # Change active background color when interacting

# Connect the Text widget and Scrollbar
test.config(yscrollcommand=scrollbar.set)

win.mainloop()
