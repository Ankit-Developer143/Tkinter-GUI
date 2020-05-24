from tkinter import *
root=Tk()
root.geometry("500x300")



#set title
root.title("Ankit")
root.geometry("500x333")

#Important label Options
#text - add the text
#bg - background
#fg - foreground(text color)
#font - set the font
#padx - x padding
#pady - y padding


# Important pack options
# side=TOP,BOTTOM,LEFT,RIGHT (NO SEMI-COLUMN REQUIRED)
# anchor=sw(South-East RHS) se sn ss
#relief- border-style:--(SUNKEN,RAISED,GROOVE)
#fill=X,Y (if you r using fill=X and then if u tried to  stretch text in x position then its automatic fill)



# using all property
title_label=Label(text='''It also contains philosophical and devotional material, such as a discussion of the four "goals of life" or puruṣārtha (12.161).
 \nAmong the principal works and stories in the Mahābhārata are the Bhagavad Gita, the story of Damayanti, an abbreviated version of the Rāmāyaṇa, and the 
 \nstory of Ṛṣyasringa, often considered as works in their own right.''',bg="red", fg="white", padx="113",pady="94" ,font="comicsansms 9 bold",relief=SUNKEN,borderwidth=3)



# title_label.pack(side=RIGHT,anchor="se",fill=X,fill=Y)
title_label.pack()

root.mainloop()