
from tkinter import *


root = Tk()

girdi = Entry(root, borderwidth=8)
girdi.pack()

def Tikla():

    mesaj = "Tipini sikim, "+ girdi.get()
    myLabel = Label(root, text = mesaj)
    myLabel.pack()

button = Button(root, text ="Adini gir, ve tikla", command = Tikla , fg="red",bg="blue" ) 
button.pack()


root.mainloop()