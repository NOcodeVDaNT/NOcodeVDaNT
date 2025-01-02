from tkinter import *

def fun(event):
    print("Hello, world!")

win = Tk()
but = Button(win, text="button")
but.bind('<Button-1>', fun)  # Bind left mouse button click event
but.pack()

win.mainloop()


# Mouse Events: win.bind('<Button-1>', mouse_clicked) 

# <Button-1> – Left mouse button click.
# <Button-2> – Middle mouse button click (if available).
# <Button-3> – Right mouse button click.
# <Double-1> – Double click with the left mouse button.
# <Double-2> – Double click with the middle mouse button (if available).
# <Double-3> – Double click with the right mouse button.
# <Triple-1> – Triple click with the left mouse button.
# <Motion> – Mouse movement (when the mouse moves over a widget).
# <Enter> – Mouse pointer enters the widget.
# <Leave> – Mouse pointer leaves the widget.
# <B1-Motion> – Mouse movement while holding the left mouse button down.
# <B2-Motion> – Mouse movement while holding the middle mouse button down.
# <B3-Motion> – Mouse movement while holding the right mouse button down.

#__________________________________________________________________________________________________________________


# Keyboard Events:  win.bind('<KeyPress>', key_pressed)

# <KeyPress> – Key press event (when any key is pressed).
# <KeyRelease> – Key release event (when any key is released).
# <Key> – This can be used with a specific key, such as:
# <a>, <b>, <c>, etc. (for lowercase letters)
# <A>, <B>, <C>, etc. (for uppercase letters)
# <1>, <2>, etc. (for numbers)
# <space> – Space bar
# <Return> – Enter key
# <BackSpace> – Backspace key
# <Tab> – Tab key
# <Escape> – Escape key
# <Shift>, <Control>, <Alt> – Modifier keys
# <Control-KeyPress> – When a specific key is pressed while the Control key is held down.
# <Shift-KeyPress> – When a specific key is pressed while the Shift key is held down.
# <Alt-KeyPress> – When a specific key is pressed while the Alt key is held down.
# <Enter> – Enter key press event.
# <Delete> – Delete key press event.
# <F1>, <F2>, ..., <F12> – Function keys.

#__________________________________________________________________________________________________________________


# Special Bindings:
# <Control-c> – Binding for copying (Ctrl + C).
# <Control-v> – Binding for pasting (Ctrl + V).
# <Control-x> – Binding for cutting (Ctrl + X).