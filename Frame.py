from tkinter import *
root =Tk()
root.geometry("655x220")


# create y side frame
f1=Frame(root,bg="grey",borderwidth=9,relief=SUNKEN)
f1.pack(side=TOP,fill="x",padx=50)
l=Label(f1,text="Project Tkinter")
l.pack()


#create x side frame
f2=Frame(root,bg="blue", borderwidth=9,relief=SUNKEN)
f2.pack(side=LEFT,fill="y")

l2=Label(f2,text="Index")
l2.pack()
root.mainloop()