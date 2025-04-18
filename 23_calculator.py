from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"
                screen.update()

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() +text)
        screen.update()

root=Tk()
root.geometry("644x900")
root.title("Calculator by Aayush")
root.wm_iconbitmap("22_ico_file.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)




f=Frame(root,background="grey")

b=Button(f,text="C",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="<-",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()





f=Frame(root,background="grey")

b=Button(f,text="9",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack(fill=X)



f=Frame(root,background="grey")

b=Button(f,text="6",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack(fill=X)



f=Frame(root,background="grey")

b=Button(f,text="3",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack(fill=X)




f=Frame(root,background="grey")

b=Button(f,text="00",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="=",bg="orange",fg="white",padx=28,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()