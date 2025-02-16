from tkinter import *
def harry(event):
    print(f"you clicked on the button at {event.x}, {event.y}")
root=Tk()

root.title("EVENTS IN TKINTER")
root.geometry("644x334")
widget=Button(root,text="Click me please")
widget.pack()

#SEARCH EVENTS IN TKINTER FOR ALL BUTTONS
widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()