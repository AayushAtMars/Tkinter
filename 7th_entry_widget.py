from tkinter import *

def getval():
    print(f"The value of username is {uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")

root = Tk()

root.geometry("655x333")

user=Label(root, text="Username")
password=Label(root, text="Password")
user.grid()
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, text=uservalue)
passentry=Entry(root, text=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1,column=1)

Button(text="Submit", command=getval).grid()

root.mainloop()