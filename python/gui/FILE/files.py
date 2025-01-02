from tkinter import *
from tkinter import filedialog

def openfile():
    # Open file dialog with specific initial directory and file types
    filepath = filedialog.askopenfilename(
        initialdir="/",  # This sets the default directory to the root ("/") when the file dialog opens
        filetypes=(      # This restricts the file types that can be selected in the dialog
            ("txt files", "*.txt"),  # Allows the user to select only .txt files (with .txt extension)
            ("all files", "*.*")     # Allows the user to select any type of file (with any extension)
        ),title="ghost"
    )
    print(f"File selected: {filepath}")  # Print the selected file path

win = Tk()

# Button with command that calls openfile() when clicked
but = Button(win, text="Submit", command=openfile)
but.pack()

win.mainloop()
