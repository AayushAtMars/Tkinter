from tkinter import *
import tkinter.messagebox as tmsg
def myfunc():
    print("hahahahahahahahahhahaha")

def help():
    print("I will help you")
    a=tmsg.showinfo("Help","Aayush will hyelp you with this GUI")
    #print(a)

def rate():
    value=tmsg.askquestion("was your experince good?", "you used this gui......was your experince good")
    #print(value)
    if value=="yes":
        msg ="Great..Rate us on appstore"

    else:
        msg="Tell us what went wrong. we will call you soon"

    tmsg.showinfo("Experince",msg)

def divya():
    ans=tmsg.askretrycancel("Divya se dosti kar lo","Sorry Divya dost nhi banegi")
    if ans:
        print("retry krne pe bhi kuch nhi hoga")

    else:
        print("achha hua cancel kr diya wrna pit te")

root=Tk()

root.title("Menus and Submenus")
root.geometry("733x566")

#use this to create a non-drop menu
'''mymenu=Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)'''

mainmenu=Menu(root)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Save as", command=myfunc)
m1.add_separator()
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)


m2=Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Apply",menu=m2)

m3=Menu(mainmenu, tearoff=0)
m3.add_command(label="Rate Us",command=rate)
m3.add_command(label="Help",command=help)
m3.add_command(label="Befriend_Divya",command=divya)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)
root.mainloop()