from tkinter import *
def myfunc():
    print("This is filemenu")

def menufunc():
    print("hi this is dropdown list")

root=Tk()
root.geometry("680x440")
root.title("Ankit Notepad")

# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Refractor",command=myfunc)
# mymenu.add_command(label="Run",command=myfunc)
# mymenu.add_command(label="Terminal",command=myfunc)
# mymenu.add_command(label="exit",command=quit)
# root.config(menu=mymenu)          #using this technique to pack the command
# m1=Menu(mymenu)

menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="edit",command=menufunc)
m1.add_command(label="Save",command=menufunc)
m1.add_separator()
m1.add_command(label="new",command=menufunc)
m1.add_command(label="rename",command=menufunc)
m1.add_command(label="Exit",command=quit)
menubar.add_cascade(label="File",menu=m1)
root.config(menu=menubar)



root.mainloop()