from tkinter import *
win=Tk()

file_menu=Menu(win)
win.config(menu=file_menu)#menu for window win


#guns
f_menu=Menu(file_menu,tearoff=0)
#f_menu.add_command(label="ak")
#submenu for ak
sub_menu=Menu(f_menu,tearoff=0)
sub_menu.add_command(label="ak47")
sub_menu.add_command(label="ak56")
sub_menu.add_command(label="ak95")
f_menu.add_cascade(label="ak",menu=sub_menu)


f_menu.add_command(label="m416")
f_menu.add_separator()
f_menu.add_command(label="Gclock")
f_menu.add_separator()
f_menu.add_command(label="AWM")



file_menu.add_cascade(label="guns",menu=f_menu)

#throwable
f_menu1=Menu(file_menu,tearoff=0)
f_menu1.add_command(label="grende")
f_menu1.add_command(label="flame")
f_menu1.add_command(label="smoke")
f_menu1.add_command(label="flash")

file_menu.add_cascade(label="throwable",menu=f_menu1)


win.mainloop()