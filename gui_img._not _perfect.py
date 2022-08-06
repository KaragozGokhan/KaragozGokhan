
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Recep secret galeri")

img2 = ImageTk.PhotoImage(Image.open("imgs.for.gui/recep2.png"))
img3 = ImageTk.PhotoImage(Image.open("imgs.for.gui/recep3.png"))
img4 = ImageTk.PhotoImage(Image.open("imgs.for.gui/ibo.png"))
img6 = ImageTk.PhotoImage(Image.open("imgs.for.gui/recep.jpg"))

image_list =[img2,img3,img4,img6]
status = Label(root, text = "img 1 of " + str(len(image_list)) , bd =1, relief = SUNKEN, anchor=W)

myLabel = Label(image=img2)
myLabel.grid(row=0,column=0,columnspan=3)

def ileri(image_number):
    
    global myLabel
    global button_back
    global button_move

    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_number-1])
    button_move = Button(root, text = "ileri", command= lambda:ileri(image_number+1))
    button_back = Button(root, text = "geri", command= lambda:geri(image_number-1))
    
    if image_number == 4:
        button_move = Button(root, text ="ileri", state=DISABLED)

    myLabel.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_move.grid(row=1,column=2)

    status = Label(root, text = "img" + str(image_number)+"of " + str(len(image_list)) , bd =1, relief = SUNKEN, anchor=W)
    status.grid(row=3, column =0, columnspan= 3, sticky=W+E)

   
def geri(image_number):
    global myLabel
    global button_back
    global button_move

    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_number-1])
    button_back = Button(root, text = "geri", command=lambda: geri(image_number-1))
    button_move = Button(root, text = "ileri", command= lambda: ileri(image_number+1))
    
    if image_number == 1:
        button_back = Button(root, text = "geri", state=DISABLED)

    myLabel.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_move.grid(row=1, column=2) 

    status = Label(root, text = "img" + str(image_number)+"of " + str(len(image_list)) , bd =1, relief = SUNKEN, anchor=W)
    status.grid(row=3, column =0, columnspan= 3, sticky=W+E)


def exit():
    
   

    process=messagebox.askyesno("Exit message","Are you sure you wanna exit ?")
    if process:
        root.destroy()
    

root.protocol('WM_DELETE_WINDOW',exit)
   
    


button_back = Button(root, text = "geri", command= geri, state=DISABLED)
button_move = Button(root, text = "ileri", command= lambda:ileri(2))
button_quit = Button(root, text = "çıkış", command = exit)  #root.quit()

button_back.grid(row=1, column=0)
button_move.grid(row=1, column=2)   #row = 1, column = 1 
button_quit.grid(row=1, column=1, pady= 20) #row = 2 column = 2 de hata alıyorum
status.grid(row=3, column =0, columnspan= 3, sticky=W+E)

root.mainloop()