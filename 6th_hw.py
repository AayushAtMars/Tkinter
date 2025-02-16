from tkinter import *

root=Tk()

def name1():
    print("AAYUSH")

def name2():
    print("KUMAR")

def name3():
    print("SINGH")

root.geometry("666x333")
f1=Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

b1=Button(f1, bg="yellow",fg="blue", text="FIRST NAME", command=name1)
b1.pack(side=LEFT,padx=23)

b2=Button(f1, bg="yellow",fg="blue", text="MIDDLE NAME", command=name2)
b2.pack(side=LEFT,padx=23)

b3=Button(f1, bg="yellow",fg="blue", text="LAST NAME", command=name3)
b3.pack(side=LEFT,padx=23)

root.mainloop()