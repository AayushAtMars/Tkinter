from tkinter import *
import tkinter.messagebox as tmsg
def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("..",f"we have credited {myslider2.get()} dollars to your bank account")
root=Tk()

root.title("Sliders")
root.geometry("455x233")

'''myslider= Scale(root, from_=0, to=455)
myslider.pack()'''

Label(root,text="How many dollars you want?").pack()
myslider2= Scale(root, from_=0, to=100, orient=HORIZONTAL,tickinterval=50)
#myslider2.set(5)
myslider2.pack()

Button(root,text="Get Dollar", pady=10, command=getdollar).pack()

root.mainloop()