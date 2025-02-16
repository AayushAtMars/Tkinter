from tkinter import *

def getval():
    w=width.get()
    l=length.get()
    root.geometry(f"{w}x{l}")

root=Tk()

root.title("Window Resizer")
root.geometry("344x244")

w=Label(root,text="Enter Width")
l=Label(root,text="Enter Length")
w.grid()
l.grid(row=1)

width=IntVar()
length=IntVar()

width_entry=Entry(root,textvariable=width)
length_entry=Entry(root,textvariable=length)
width_entry.grid(row=0,column=1)
length_entry.grid(row=1,column=1)

Button(text="Submit",command=getval).grid()

root.mainloop()