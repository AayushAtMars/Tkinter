from tkinter import *
from PIL import Image, ImageTk

def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text




root =Tk()
root.title("Aayush News")

root.geometry("1000x800")

texts=[]
photos=[]
for i in range(0,3):
    with open(f"12th_{i+1}t.txt") as f:
        text=f.read()
        texts.append(every_100(text))

    image=Image.open(f"12th_{i+1}.png")
    #TODO resize these image
    image=image.resize((225,265))
    photos.append(ImageTk.PhotoImage(image))

f0=Frame(root,width=800,height=70)
Label(f0,text="Aayush News", font="lucida 33 bold").pack()
Label(f0,text="march 03, 2024", font="lucida 13 bold").pack()
f0.pack()

f1= Frame(root,width=900,height=200)
Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")

f2= Frame(root,width=900,height=200)
Label(f2,text=texts[1],padx=22,pady=22).pack(side=RIGHT)
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")

f3= Frame(root,width=900,height=200)
Label(f3,text=texts[2],padx=22,pady=22).pack(side=LEFT)
Label(f3,image=photos[2],anchor="e").pack()
f3.pack(anchor="w")
root.mainloop()