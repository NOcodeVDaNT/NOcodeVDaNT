from tkinter import *
def fun(event):
    # Get the selected indices
    selected_indices = list_box.curselection() #this method fetches the indices of selected items in the Listbox.,The variable selected_indices is a tuple.
    # Retrieve the selected items using the indices
    selected_items = [list_box.get(i) for i in selected_indices]
    print("Selected items:", selected_items)

win=Tk()
lis=["audi","bmw","lamborgini","ferrari","bugatti","mercedes"]
p=StringVar(value=lis)
list_box=Listbox(win,listvariable=p,selectmode="multiple")
list_box.pack()

list_box.bind('<<ListboxSelect>>',fun)

win.mainloop()