from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Treeview Example")
car_icon = PhotoImage(file="img.png",width=10,height=10) 

Lab = Label(win, text="Cars")
Lab.pack()

# Create a Treeview with both tree column and headings
tree = ttk.Treeview(win, columns=("Model", "Year"), show="tree headings")
tree.heading("#0", text="Car Name")  
tree.heading("Model", text="Modelll")
tree.heading("Year", text="Years")

#if show ="headings" then only headings are visible
#if show="tree heading" then a prexist colume called "#0" also visible
#the text="" in tree.insert is assigned to #0 col, and values=() to rest of the column in tree

# Insert data
tree.insert("", END, text="Toyota", values=("Camry", "2023"), iid=0,image=car_icon)
tree.insert("", END, text="Honda", values=("Civic", "2022"), iid=1)

# Insert sub-items
tree.insert("", END, text="Fortuner", values=("SUV", "2022"), iid=2)
tree.insert("", END, text="Legender", values=("SUV", "2022"), iid=3)
tree.insert("", END, text="Crammy", values=("Van", "2022"), iid=4)

# Move sub-items under Toyota
#tree.move(IIDtoMove , desitanceForIID , atwhichIndexit has to be put in destination)
tree.move(2, 0, 0)
tree.move(3, 0, 1)
tree.move(4, 0, 2)

tree.pack()

win.mainloop()
