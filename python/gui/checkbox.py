from tkinter import *
def toggle_checkbox():
    # Toggle the checkbox state programmatically
    if var.get() == "OFF":  # Currently unchecked
        var.set("ON")       # Check the checkbox
    else:                   # Currently checked
        var.set("OFF")      # Uncheck the checkbox


def fun():
    # Use the current value of the variable to trigger actions
    if var.get() == "ON":
        print("Checkbox is checked (ON)")
        chbx.config(text="ON")
    else:
        print("Checkbox is unchecked (OFF)")
        chbx.config(text="OFF")

win = Tk()

# Use StringVar to manage the Checkbutton state
var = StringVar(value="OFF")  # Default state is unchecked

# Configure the Checkbutton
chbx = Checkbutton(
    win,
    text="OFF",
    font=(50),
    command=fun,  # Called when the Checkbutton is toggled
    variable=var,
    onvalue="ON",  # Value when checked
    offvalue="OFF"  # Value when unchecked
)
chbx.place(x=100, y=100)

but = Button(win, text="submit",command=toggle_checkbox)
but.place(x=200, y=150)

win.mainloop()
