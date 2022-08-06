from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title = ("adding frame")

frame = LabelFrame(root, text = "Frame ..", padx = 10, pady =10)
frame.pack(padx = 20, pady = 20)

buton = Button(frame, text = "new button")
buton2 = Button(frame, text = "2nd new button")
buton.grid(row = 0, column = 0)
buton2.grid(row = 2, column = 2)


root.mainloop()