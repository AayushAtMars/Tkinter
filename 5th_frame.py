from tkinter import *

root = Tk()

root.geometry("655x333")
f1= Frame(root,bg="grey",borderwidth=6)
f1.pack(side=LEFT)

l1=Label(f1, text="Project Tkinter")
l1.pack()
root.mainloop()