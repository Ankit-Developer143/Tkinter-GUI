from tkinter import *
def getvals():
    print(f"Your Name is :{namevalue.get()}")
    print(f"Your PhoneNumber is :{phonevalue.get()}")
    print(f"Your Gender is :{gendervalue.get()}")
    print(f"Your Emergency Number is :{emergencyvalue.get()}")
    print(f"Your PaymentMode is :{paymentmodevalue.get()}")
    print(f"Your prebookingfood  service value is :{foodservicevalue.get()}")

    #first use "w" to create file and then use "a" to append the file
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")

root=Tk()
root.title("Travels")
root.geometry("655x333")
Label(root,text="Welcome to Ankit Travels",font="comicsansms 9 bold").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="PaymentMode")
name.grid(row=1  ,column=2)
phone.grid(row=2  ,column=2)
gender.grid(row=3  ,column=2)
emergency.grid(row=4  ,column=2)
paymentmode.grid(row=5  ,column=2)

#Declaring variables
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#entries variables
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)

nameentry.grid(row= 1 , column= 3)
phoneentry.grid(row= 2 , column= 3 )
genderentry.grid(row= 3 , column= 3 )
emergencyentry.grid(row= 4 , column=3)
paymentmodeentry.grid(row=5  , column=3)

#CheckButton
foodservice=Checkbutton(root,text="Want to pre book your meals", variable=foodservicevalue)
foodservice.grid(row=6 , column=3)


Button(root,text="Submit to Ankit Travel",command=getvals).grid(row=7,column=3)

root.mainloop()