from tkinter import *

root=Tk()

root.geometry("655x444")
root.title("Title of my GUI")
root.wm_iconbitmap("22_ico_file.ico")
root.configure(background="red")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="close",command=root.destroy).pack()

root.mainloop()