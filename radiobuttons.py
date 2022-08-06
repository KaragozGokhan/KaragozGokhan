
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("radyo butonu len")
#v = IntVar()
#v.set("1")
def click(value):
    myLabel = Label(root, text= value)
    myLabel.pack()
MODES = [
    ("güneş","güneş"),
    ("dünya","dünya"),
    ("venüs","venüs"),
    ("jüpiter","jüpiter"),
]
gezegenler = StringVar()
gezegenler.set("venüs")
for text,mode in MODES:

    Radiobutton(root, text = text, variable = gezegenler, value= mode).pack(anchor = W)


#Radiobutton(root, text = "1st button", variable=v , value = 1, command = lambda: click(v.get())).pack()
#Radiobutton(root, text = "2nd button", variable=v , value = 2, command = lambda: click(v.get())).pack()
#myLabel = Label(root, text= v.get())
#myLabel.pack()

myButton = Button(root, text = "Butonum", command=lambda: click(gezegenler.get()))
myLabel = Label(root, text = "Çoh özel buton")
myButton.pack()

root.mainloop()