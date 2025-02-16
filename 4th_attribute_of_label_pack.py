from tkinter import *

root=Tk()
root.geometry("444x233")
root.title("MAHAN AAYUSH")
title_label=Label(text='''Abdul Rashid Salim Salman Khan is an Indian
 \nactor, film producer, and television personality who works predominantly in Hindi films. In a career spanning 
 \nover three decades, Khan has received numerous awards, including two National Film Awards as a film producer,
  \nand a Filmfare Award as an actor.[4] He is cited in the media as one of the most commercially successful 
  \nactors of Indian cinema.[5][6] Forbes has included Khan in listings of the highest-paid celebrities in the 
  \nworld, in 2015 and 2018, with him being the highest-ranked Indian in the latter year.[7][8][9][10] Khan has starred
   \nin the annual highest-grossing Hindi film of 10 individual years, the highest for any actor.[11]''', bg =  "red" , fg = "white" ,
                  padx=23 , pady = 44 , font = ("comicsansms",19, "bold") , borderwidth=30,relief=SUNKEN)

title_label.pack(side=LEFT , anchor="sw" , fill=Y , padx=34 , pady=34)
root.mainloop()