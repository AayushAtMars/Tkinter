from tkinter import *
import tkinter.messagebox as tmsg
def order():
    tmsg.showinfo("Order recieved", f"we have recieved your order for {var.get()}, thanks for ordering")

root=Tk()

root.title("Radio Button")
root.geometry("555x444")

var = IntVar()
#var.set=(1)
Label(root, text="What you like to have sir?",font ="lucid 19 bold", justify=LEFT,padx=14).pack()

radio=Radiobutton(root, text="Dosa", padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root, text="Idly", padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root, text="Momos", padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root, text="Samosa", padx=14,variable=var,value=4).pack(anchor="w")
#TODO using for loop

Button(text="Order now",command=order).pack()
root.mainloop()