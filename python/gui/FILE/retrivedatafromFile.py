from tkinter import *
from tkinter import filedialog

def openfile():
    # Open file dialog to select a file
    file_data = filedialog.askopenfile(
        initialdir="/",  # Set the default directory to root
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")),  # Filter for file types
        title="Select a file"  # Set the title of the file dialog
    )
    
    # If a file is selected
    if file_data:
        data = file_data.read()  # Read the file's content
        print(data)  # Print the content of the file
        file_data.close()  # Close the file after reading
    else:
        print("No file selected")  # If no file is selected

win = Tk()

# Button to trigger openfile function
but = Button(win, text="Submit", command=openfile)
but.pack()

win.mainloop()
