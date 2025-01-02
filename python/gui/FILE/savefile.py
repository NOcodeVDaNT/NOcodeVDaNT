from tkinter import *
from tkinter import filedialog
#saveasfilename()  This method opens a "Save As" dialog and returns the path where the file should be saved, but does not actually save the file.
#saveasfile() directly save the file

def openfile_1():
    file_path=filedialog.asksaveasfilename(title="ghost",initialdir="/",filetypes=(("text file","*.txt"),("python file","*.py")))
    print(file_path)
    
def openfile_2():
    file=filedialog.asksaveasfile(title="ghost",initialdir="/",filetypes=(("text file","*.txt"),("python file","*.py")),defaultextension="*.txt")
    file.write("hello")
    file.close()
    

win=Tk()


but_1 = Button(win, text="Save file location", command=openfile_1)
but_1.pack()



but_2 = Button(win, text="Save file ", command=openfile_2)
but_2.pack()


win.mainloop()