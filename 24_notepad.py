from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file=None

        else:
            #save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad By Aayush")
if __name__ == '__main__':
    #Basic Tkinter setup
    root=Tk()
    root.title("Notepad by Aayush")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    #Menubar
    Menubar=Menu(root)

    #FileMenu starts
    FileMenu = Menu(Menubar, tearoff=0)
    #To open new file
    FileMenu.add_command(label="New",command=newFile)

    #to open already existing file
    FileMenu.add_command(label="Open",command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=FileMenu)
    #FileMenu ends


    #Edit Menu starts
    EditMenu=Menu(Menubar,tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    Menubar.add_cascade(label="Edit", menu=EditMenu)
    #Edit Menu ends


    #Help menu starts
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)


    root.config(menu=Menubar)


    #adding scrollbar
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)



    root.mainloop()