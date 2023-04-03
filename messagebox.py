from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root = Tk()
root.title = ("mesaj kutusu ")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def mesaj():
    cevap =messagebox.askyesno("Top secret info", "Nobody knows")
    Label(root, text=cevap).pack()
    if cevap == 1 :
        Label(root, text="Yanlış cevap").pack()

    else :
        Label(root, text = "Tebrikler! Doğru cevap",padx=10).pack()

Button(root, text = "Çoh gizli mesaj", command = mesaj).pack()
root.mainloop()
