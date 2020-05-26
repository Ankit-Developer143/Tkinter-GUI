from tkinter import *

root=Tk()
root.geometry("455x233")
def getdollar():
    print(f"We Have Credit  {myslider1.get()}$ in Your Account")





# #vertical slide
# myslider=Scale(root,from_=0,to=455)
# myslider.pack()

#Horizontal
Label(text="How Many Label You Want").pack()
myslider1=Scale(root,from_=0, to=400, orient=HORIZONTAL)
myslider1.pack()
Button(root,text="Get Dollor!!",command=getdollar).pack(padx=40)

root.mainloop()