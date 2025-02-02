import openai
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os
from openai import OpenAI

def lightmode():
    win.config(bg="white")
    send_button.config(bg="white", fg="black")
    # lab.config(bg="white", fg="black")
    # chat.config(bg="white", fg="black")
    # entry.config(bg="white", fg="black")
#darkmode
def darkmode():
    win.config(bg="black")
    send_button.config(bg="black", fg="white")
    # lab.config(bg="black", fg="white")
    # chat.config(bg="black", fg="white")
    # entry.config(bg="black", fg="white")
    
# Function to call OpenAI API
def deepseek(query):
    print(query)
    try:
        
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
        )

        response = client.chat.completions.create(
    
        model="openai/gpt-3.5-turbo",
        messages=[
        {
            "role": "user",
            "content": query
        }
        ]
        )
        ans =   response.choices[0].message.content
        print(ans)
        return ans
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print(e)
        return "Sorry, I couldn't process your request."







# Function to handle sending the message
def send():
    user_message = entry.get()
    if not user_message.strip():
        messagebox.showwarning("Input Error", "Please enter a message.")
        return

    chat.insert(END, f"you: {user_message}\n\n")
    response = deepseek(user_message)
    
    entry.delete(0, END)
    chat.insert(END, f"GH0ST_AI: {str(response)}\n\n\n\n")
    chat.yview(END)

# Setting up the Tkinter window
win = Tk()
win.title("GH0ST_AI by Vedant Dahake")
win.geometry("900x600")
win.resizable(0, 0)

# Chat section
lab = Label(win, text="GH0ST_AI", fg="black", font=("Arial", 30))
lab.place(x=450, y=40,anchor="center")
chat = ScrolledText(win, height=20, width=120, fg="black", font=("Arial", 10), bg="white", relief="sunken",bd=8)
chat.place(x=4, y=100)

# Menu
file_menu = Menu(win)
win.config(menu=file_menu)

f_menu = Menu(file_menu, tearoff=0)
submenu = Menu(f_menu, tearoff=0)
submenu.add_command(label="Dark Mode",command=darkmode)
submenu.add_command(label="Light Mode",command=lightmode)
submenu.add_command(label="Versions of GH0ST_AI",command=lambda: messagebox.showinfo("Versions of GH0ST_AI", "GH0ST_AI v1.0.0"))
submenu.add_command(label="Credits",command=lambda: messagebox.showinfo("Credits", "Developed using DEEPSEEK OPEN AI API"))
f_menu.add_cascade(label="Options", menu=submenu)
f_menu.add_separator()
f_menu.add_command(label="Donate")

file_menu.add_cascade(label="Menu", menu=f_menu)
file_menu.add_cascade(label="About Developer", command=lambda: messagebox.showinfo("About Developer", "Vedant Dahake"))

# Input field for user message
entry = Entry(win, width=30, font=("Arial", 30), fg="black",relief="sunken",bd=8)
entry.place(x=4, y=500)

# Send button
send_button = Button(win, text="Ask Ghost", font=("Arial", 20), command=send, width=10, height=1,bd=8)
send_button.place(x=700, y=500)

# Start the Tkinter event loop
win.mainloop()
