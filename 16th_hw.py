from tkinter import *
import tkinter.messagebox as tmsg
def getval():
    a=f"{slider.get()}"
    with open("16th_hw.txt","w") as f:
        f.write(a)
    tmsg.showinfo("Rating","Thanks for the rating")
root=Tk()

root.geometry("455x344")
Label(root,text="How was our food ?",font ="comicsansms 19 bold").pack()
slider=Scale(root,from_=0, to=10, orient=HORIZONTAL)
slider.pack()
Button(text="Submit",command=getval).pack()

root.mainloop()