from tkinter import *
import tkinter.messagebox as tmsg
def myfunc():
 print(Hii)

def labelfunc():
    print("Hello")
def Helpfunc():
    tmsg.showinfo("help","Ankit Will Help You!!")

def ratefunc():
    a=tmsg.askquestion("How was your feeling","please rate us")
    print(a)
root=Tk()
root.geometry("655x333")

# This is Drop - Down list
# mymenu=Menu(root)
# m1=Menu(mymenu)
# m1.add_command(label="New",command=myfunc)
# m1.add_command(label="Edit",command=myfunc)
# m1.add_command(label="Rename",command=myfunc)
# m1.add_command(label="Exit",command=myfunc)
# mymenu.add_cascade(label="File",menu=m1)
# root.config(menu=mymenu)

mymenu=Menu(root)
mymenu.add_command(label="View",command=labelfunc)
mymenu.add_command(label="Task",command=labelfunc)
mymenu.add_cascade(label="Help",command=Helpfunc)
mymenu.add_cascade(label="RateUs",command=ratefunc)
root.config(menu=mymenu)





root.mainloop()