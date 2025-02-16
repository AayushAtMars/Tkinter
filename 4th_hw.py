from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("500x400")

strip=Label(text="READY" , bg="red" , fg="white" , padx=10 , pady=10 , font=("comicsansms" , 25 , "bold" ,) 
            , borderwidth=10 , relief=RIDGE)
strip.pack(side=BOTTOM , fill= X , padx=5 , pady=5)
root.mainloop()