from tkinter import *

def update_label(selected_gun):
    lb.config(text=f"You selected: {selected_gun}")

win = Tk()
win.title("Gun Selector")

# Create a Menubutton
menu_but = Menubutton(win)
menu_button = Menu(menu_but, tearoff=0)  # Tear-off for detachable menu

# Add options to the menu
menu_button.add_command(label="AK-47", command=lambda: update_label("AK"))
menu_button.add_command(label="M416", command=lambda: update_label("M416"))
menu_button.add_command(label="Glock", command=lambda: update_label("Glock"))
menu_button.add_command(label="AWM", command=lambda: update_label("AWM"))


# Link the menu to the Menubutton
menu_but["menu"] = menu_button

menu_but.pack(pady=10)

# Label to display the selected gun
lb = Label(win, text="You selected:")
lb.pack(pady=10)

win.mainloop()
