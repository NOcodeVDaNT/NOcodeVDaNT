from tkinter import *

# Creating the main window
win = Tk()
win.geometry("1100x300") 

# Creating the first canvas
can_1 = Canvas(win, relief="sunken", width=500, height=200, bg="grey", bd=5)
can_1.place(x=0, y=0)

# Creating lines
coordinate_1 = 0, 0, 500, 200
line_1 = can_1.create_line(coordinate_1, fill="red")

coordinate_2 = 500, 0, 0, 200
line_2 = can_1.create_line(coordinate_2, fill="red")

# Creating the second canvas
can_2 = Canvas(win, relief="sunken", width=500, height=200, bg="grey", bd=5)
can_2.place(x=550, y=0)

# Correcting the arc coordinates and extent
coordinate_3 = 50, 50, 450, 200   # Proper rectangle for the arc
arc = can_2.create_arc(coordinate_3, start=0, extent=359.9999999, fill="red")  # Semi-circle arc

#When creating an arc in Tkinter, you need to provide coordinates for a bounding rectangle
#(x0, y0) is the top-left corner of the rectangle.
#(x1, y1) is the bottom-right corner of the rectangle.
#start: The starting angle of the arc, measured clockwise from the 3 o'clock position.
#extent: The angular span of the arc, in degrees, measured clockwise.


#polygons
can_3 = Canvas(win, relief="sunken", width=500, height=200, bg="grey", bd=5)
can_3.place(x=0, y=220)

coordinate_4=[10,10,50,50,40,100]
can_3.create_polygon(coordinate_4,fill="red")




win.mainloop()
