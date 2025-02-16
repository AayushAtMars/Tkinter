from tkinter import *

def getvals():
    print("It Works")

root=Tk()
root.title("Travel Form")

root.geometry("644x344")
#Heading
Label(root,text="Welcome To Aayush Travels", font="comicsansms 13 bold",pady=5).grid(row=0, column=3)

#text for form
name= Label(root, text="Name")
phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
emergency=Label(root, text="Emergency Contact")
payment=Label(root, text="Payment Mode")

#packing
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

#Tkinter variables for storing
name_value=StringVar
phone_value=StringVar
gender_value=StringVar
emergency_value=StringVar
payment_value=StringVar
food_value=IntVar

#enteries for form
nameentry= Entry(root, textvariable=name_value)
phoneentry= Entry(root, textvariable=phone_value)
genderentry= Entry(root, textvariable=gender_value)
emergencyentry= Entry(root, textvariable=emergency_value)
paymententry= Entry(root, textvariable=payment_value)

#packing enteries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#checkbox
foodsevice=Checkbutton(text="Want to pre-book your meal", variable=food_value)
foodsevice.grid(row=6,column=3)

#button to submit

Button(text="Submit to Aayush travels",command=getvals).grid(row=7,column=3)

root.mainloop()
