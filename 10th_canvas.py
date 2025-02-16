from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{(canvas_width)}x{(canvas_height)}")
root.title("CANVAS")
can_widget=Canvas(root,width=canvas_width, height=canvas_height)
can_widget.pack()

#The line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

#to create a rectangle specify parameters in this order top_left, bottom_right
can_widget.create_rectangle(3,5,700,300,fill="blue")

#specify parameter of center
can_widget.create_text(200,200,text="Tkinter")

#specify parameter of rectangle
can_widget.create_oval(3,5,700,300,fill="yellow")
root.mainloop()