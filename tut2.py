from tkinter import *


root=Tk()
#all operation perform between them.

'''Screen Geometry:--("width x height")'''
root.geometry("400x200")


#Screen minisize :--minsize(width,height)
root.minsize(300,100)

#Screen Maxsize:--(width,height)
root.maxsize(800,800)

#Label no user interaction envelo
Ankit = Label(text="Hello my name is Ankit Singh and this is my GUI")
Ankit.pack()






root.mainloop();