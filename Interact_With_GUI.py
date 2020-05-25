from tkinter import *
root=Tk()
root.geometry("655x333")
def Hello():
    print("Hello")
def name():
    print("My name is Ankit Singh")

frame=Frame(root,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,bg="red",relief=SUNKEN,text="Say Hello",borderwidth=6,command=Hello)
b1.pack(side=LEFT,pady=2)

b2=Button(frame,bg="red",relief=SUNKEN,text="Say  name",borderwidth=6,command=name)
b2.pack(side=LEFT,pady=2)


root.mainloop()