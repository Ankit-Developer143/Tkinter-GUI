from tkinter import *
root=Tk()
root.geometry("655x333")

frame=Frame(root,borderwidth=6,bg="red", relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,bg="grey",borderwidth=6,text="Print now")
b1.pack(side=LEFT,padx=2)

b2=Button(frame,bg="grey",borderwidth=6,text="Print now")
b2.pack(side=LEFT,padx=2)

b3=Button(frame,bg="grey",borderwidth=6,text="Print now")
b3.pack(side=LEFT,padx=2)

root.mainloop()