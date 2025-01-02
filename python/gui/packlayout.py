from tkinter import Tk, Label

# Create the main window
win = Tk()

# Set the geometry of the window
win.geometry("800x200")


#layout managment
#pack layout
#grid layout
#place layout

#pack layout:
#1. it is default layout
#2. it is used to add widget in window
#3. it is used to add widget in window in vertical manner
#4. it is used to add widget in window in horizontal manner
#6. it is used to add widget in window in both manner with equal space between them
# Create a label with the correct syntax
lab = Label(win, text="GHOST", font=("Times New Roman", 30, "bold"), bg="red")

# Place the label on the window
lab.pack(padx=200,pady=50,ipadx=50,ipady=10,fill="x",expand=True) #pad is external displacement from the border of the window


# Run the application
win.mainloop()
