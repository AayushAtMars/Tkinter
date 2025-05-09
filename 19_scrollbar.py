from tkinter import *

root=Tk()

root.title("Scroll Bar")
root.geometry("555x444")

#For connecting scrollbar to a widget
#1. widget(yscrollcommand = scrollbar.set)
#2. scrollbar.config(command=widget.yview)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(root, yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item{i}")

listbox.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)
root.mainloop()