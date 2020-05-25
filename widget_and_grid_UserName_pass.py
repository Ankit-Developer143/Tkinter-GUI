from tkinter import *
def getvalue():
    print(f"your user name is:{uservalue.get()}")
    print(f"Your Password is:{passvalue.get()}")
root=Tk()
root.geometry("650x333")

user=Label(root,text="Username")
Password=Label(root,text="Password")
user.grid()
Password.grid(row=1)

# variable class in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

#Define datatype
uservalue=StringVar()
passvalue=StringVar()

#use data type here
userentry=Entry(root,textvariable=uservalue)  #in textvariable we declared datatype
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

#Creating Button

Button(text="Submit",command=getvalue).grid()

root.mainloop()
