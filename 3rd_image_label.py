from tkinter import *
from PIL import Image, ImageTk    #ImageTk helps to get JPG format file in python imaging library

root = Tk()

root.geometry("655x634")

#for png image only
'''photo = PhotoImage(file="3rd.png")
image_lbl=Label(image=photo)
image_lbl.pack()'''

#For any images(jpg, png)

image=Image.open("3rd.png")
photo=ImageTk.PhotoImage(image)
image_lbl=Label(image=photo)
image_lbl.pack()
root.mainloop()