from tkinter import *
win=Tk()
frame_1=Frame(win,bg="yellow",bd=5,relief="raised")
frame_1.place(x=0,y=0,height=300,width=600)

frame_2=Frame(win,bg="green",bd=5,relief="raised")
frame_2.place(x=620,y=0,height=300,width=600)

lab=Label(frame_1,text="i am inside frame_1",fg="red",font=(50))
lab.pack()

but=Button(frame_2,text="submit")
but.pack()
win.mainloop()