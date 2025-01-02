from tkinter import *
win=Tk()
win.title("Calculator")
win.iconbitmap(r"")#image should be save with .ico extention , address should be given inside
win.attributes("-alpha",0.5)  #alpha used for transperancy ranges from 0 to 1
win.config(bg="yellow")

#locarion and size of window
win.geometry("300x300+500+200")#width and height of window at x and y position of screen

#placing at centre of any desktop
width= 300
hieght=500
sys_width=win.winfo_screenwidth()
sys_height=win.winfo_screenheight()



centre_x=int(sys_width/2-width/2)
centre_y=int(sys_height/2-hieght/2)

win.geometry(f"{width}x{hieght}+{centre_x}+{centre_y}")

#maximum and minimum size of window
win.maxsize(100,100)
win.maxsize(500,500)

#risize enable or disable
win.resizable(False,True) #True for enable and False for disable,first parameter for width seconf for hieght








win.mainloop()# continous run GUI