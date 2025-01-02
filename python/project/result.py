from tkinter import *
from tkinter.messagebox import showinfo

def showresult():
    names=name.get()
    phsyics=physics_marks.get()
    maths=mathematics_marks.get()
    chem=chemistry_marks.get()
    
    total=phsyics+maths+chem
    percentage=(total/3)*100
    result.set("Total: "+str(total)+"\nPercentage: "+str(percentage)+"%")
    Messagebox(names,percentage)
    
    
def Messagebox(*data):
    print=f"""name:{data[0]}\npercenatge:{data[1]}"""
    showinfo("Result",print)
    print(data[0])
    
# Create Tkinter window
win = Tk()
win.title("Calculator")
win.resizable(False,False)
win.geometry("400x600")
win.config(bg="grey")

# StringVar and DoubleVar for input fields
name = StringVar()
physics_marks = DoubleVar()
mathematics_marks = DoubleVar()
chemistry_marks = DoubleVar()
result=StringVar()
result.set("result")

# School name label
school_name = Label(win, text="Ghost Private School", font=("times", 25, "bold"))
school_name.pack()

# Student name label and entry
student_name_label = Label(win, text="Name:", font=(20))
student_name_label.place(x=10, y=71)

name_entry = Entry(win, textvariable=name)
name_entry.place(x=100, y=71, width=200)

# SUBJECTS label
subjects_label = Label(win, text="SUBJECTS", font=(25))
subjects_label.pack(pady=70)

# Physics marks input
physics_label = Label(win, text="Physics:", font=(15))
physics_label.place(x=10, y=150)

physics_entry = Entry(win, textvariable=physics_marks)
physics_entry.place(x=100, y=151, width=200)

# Mathematics marks input
mathematics_label = Label(win, text="Maths:", font=(15))
mathematics_label.place(x=10, y=200)

mathematics_entry = Entry(win, textvariable=mathematics_marks)
mathematics_entry.place(x=100, y=201, width=200)

# Chemistry marks input
chemistry_label = Label(win, text="Chemistry:", font=(15))
chemistry_label.place(x=10, y=250)

chemistry_entry = Entry(win, textvariable=chemistry_marks)
chemistry_entry.place(x=100, y=251, width=200)

but=Button(win,text="show result",command=showresult)
but.pack(pady=100)

r=Label(win,text="result",textvariable=result)
r.pack(pady=1)


# Start Tkinter event loop
win.mainloop()
