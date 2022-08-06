from email import message
from re import A
from tkinter import *

def motion(event):
    print("mouse location is(%d,%d) " %(event.x, event.y))
    return

master = Tk()

msg1 = "Hepsi ameriganın oyunu"
msg2 = Message(master, text = msg1)
msg2.config(bg = "yellow", font = ("times", 16 , "italic"))
msg2.pack()

msg2.bind("<Motion>",motion)

mainloop()


    


