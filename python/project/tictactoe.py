from tkinter import *
from tkinter import messagebox
count=0
x_chance=True
winner=False

def reset():
    b1.config(text=" ",state=NORMAL,bg="white")
    b2.config(text=" ",state=NORMAL,bg="white")
    b3.config(text=" ",state=NORMAL,bg="white")
    b4.config(text=" ",state=NORMAL,bg="white")
    b5.config(text=" ",state=NORMAL,bg="white")
    b6.config(text=" ",state=NORMAL,bg="white")
    b7.config(text=" ",state=NORMAL,bg="white")
    b8.config(text=" ",state=NORMAL,bg="white")
    b9.config(text=" ",state=NORMAL,bg="white")
    

win=Tk()
win.title("Tic Tac Toe by ghost")
win.geometry("300x400")
win.resizable(0,0)

b1=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b1))
b2=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b2))
b3=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b3))

b4=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b4))
b5=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b5))
b6=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b6))

b7=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b7))
b8=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b8))
b9=Button(win,text=" ",font=(20),width=10,height=5,command=lambda:fun(b9))

lab=Label(win,text="Tic Tac Toe\n BY GHOST",font=(20))

def check():
    global winner, count
    winning_combinations = [
        (b1, b2, b3),
        (b4, b5, b6),
        (b7, b8, b9),
        (b1, b4, b7),
        (b2, b5, b8),
        (b3, b6, b9),
        (b1, b5, b9),
        (b3, b5, b7),
    ]
    
    # Check for a winning combination
    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != " ":
            for button in combo:
                button.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"{combo[0]['text']} Wins!")
            reset()
            return
    
    # Check for a draw
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        reset()
    

def fun(b):
    global x_chance,count,lab
    if b["text"]==" " and x_chance==True:
        b["text"]="x"
        x_chance=False
        count+=1
        b.config(state=DISABLED)
        lab.config(text="0's Turn")
        check()
    elif b["text"]==" " and x_chance==False:
        b["text"]="0"
        x_chance=True
        count+=1
        b.config(state=DISABLED)
        lab.config(text="x's Turn")
        check()
    else:
        messagebox.showerror("Error","Invalid Move")
    
    



#menu creation
game_menu=Menu(win)
win.config(menu=game_menu)  

menu_options=Menu(game_menu,tearoff=0)
menu_options.add_command(label="New Game",command=reset)
game_menu.add_cascade(label="Options",menu=menu_options)


#board creation



b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)


b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)


b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)


lab.place(x=110,y=330)








win.mainloop()
