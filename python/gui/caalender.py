# from tkinter import *
# from tkcalendar import Calendar, DateEntry

# win=Tk()

# cal=Calendar(win,selectmode="day")
# cal.pack() #cal.pack(fill="both", expand=True)



# win.mainloop()

from tkinter import *
from tkcalendar import DateEntry

def display_selected_date():
    selected_date = date_entry.get()  # Get the selected date from DateEntry
    result_label.config(text=f"Selected Date: {selected_date}")

win = Tk()
win.title("Date Picker App")
win.geometry("400x300")

# Label
title_label = Label(win, text="Pick a Date:", font=("Helvetica", 16))
title_label.pack(pady=20)

# DateEntry Widget
date_entry = DateEntry(win, width=12, background='darkblue',
                       foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
date_entry.pack(pady=10)

# Button to Display Selected Date
show_button = Button(win, text="Show Date", command=display_selected_date)
show_button.pack(pady=10)

# Label to Display Result
result_label = Label(win, text="", font=("Helvetica", 14), fg="green")
result_label.pack(pady=20)

win.mainloop()

# datepatters:


# dd/mm/yyyy – 31/12/2024
# mm/dd/yyyy – 12/31/2024
# yyyy-mm-dd – 2024-12-31
# dd mmm yyyy – 31 Dec 2024
# mmmm dd, yyyy – December 31, 2024
# Weekday, dd mmm yyyy – Monday, 31 Dec 2024