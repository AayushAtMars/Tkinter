from tkinter import *

def myfunc():
    print("hahahahahahahahahhahaha")

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
root.mainloop()