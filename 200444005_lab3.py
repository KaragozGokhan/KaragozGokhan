#200444005 GökhanKadirKaragöz
#Question 1
from tkinter import *
import tkinter.font as tkFont
global e
def changeFont():
    global e
    if(str(v.get())=='2'):
        f=tkFont.Font(weight='bold')
    elif(str(v.get())=='3'):
        f=s=tkFont.Font(slant='italic')
    elif(str(v.get())=='4'):
        f=s=tkFont.Font(weight='bold',slant='italic')
    else:
        f=s=tkFont.Font(family="Consolas",size=10)
    e.delete(0,'end')
    e.insert(0,f)

root=Tk()
root.title('Lab4 RadioButton Font Edit')
root.geometry('600x100')
e=Entry(root,bd=5,width=100)
e.pack(side=TOP)
v=StringVar(root,1)
Radiobutton(root, text = 'Plain', variable = v,value = 1,command=changeFont).pack(side = LEFT, ipady = 5)
Radiobutton(root, text = 'Bold', variable = v,value = 2,command=changeFont).pack(side = LEFT, ipady = 5)
Radiobutton(root, text = 'Italic', variable = v,value = 3,command=changeFont).pack(side = LEFT, ipady = 5)
Radiobutton(root, text = 'Bold/Italic', variable = v,value =4,command=changeFont).pack(side = LEFT, ipady = 5)
root.mainloop()