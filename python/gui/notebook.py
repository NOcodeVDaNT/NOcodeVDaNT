from tkinter import *
from tkinter import ttk

win=Tk()

note=ttk.Notebook(win)
note.place(x=10,y=10)

f1=ttk.Frame(note,height=500,width=500,relief="sunken")
f1.pack(fill="x",expand=True,ipadx=100,ipady=100,)
lab1=Label(f1,text="file_1")
lab1.place(x=10,y=10)

f2=ttk.Frame(note,height=500,width=500,relief="sunken")
f2.pack(fill="both",expand=True,ipadx=100,ipady=100)
lab2=Label(f2,text="file_2")
lab2.place(x=10,y=10)

f3=ttk.Frame(note,height=500,width=500,relief="sunken")
f3.pack(fill="both",expand=True,ipadx=100,ipady=100)
lab3=Label(f3,text="file_3")
lab3.place(x=10,y=10)

note.add(f1,text="file1")
note.add(f2,text="file2")
note.add(f3,text="file3")


win.mainloop()