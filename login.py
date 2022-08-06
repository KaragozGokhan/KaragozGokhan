from tkinter import *


root = Tk()

root.title("Komeron ")
root.geometry("500x500")

email = Label(text = "Email ", padx = 5, pady = 10)
email.place (x=0,y=5)

password = Label(text = "Password ", padx = 5, pady = 10)
password.place(x=0,y=50)

email = Entry( root, width= 20 , borderwidth=5)
email.grid(row=1, column=1 ,columnspan=2, padx = 60 , pady = 10)

password = Entry ( root, width= 20 , borderwidth=5)
password.grid(row=2, column=1 ,columnspan=2, padx = 65 , pady = 10)


def signin():
    email2 = Label(text = "Email2 ", padx = 5, pady = 10   )
    email2.place (x=0,y=50)
    email2 = Entry( root, width= 20 , borderwidth=5)
    email2.grid(row=10, column=1 ,columnspan=2, padx = 60 , pady = 10  )

    password1 = Label(text = "Password1 ", padx = 5, pady = 10   )
    password1.place(x=0,y=50)
    password1 = Entry ( root, width= 20 , borderwidth=5)
    password1.grid(row=11, column=1 ,columnspan=2, padx = 65 , pady = 10)

    password_again = Label(text = "Password again ", padx = 5, pady = 10  )
    password_again.place(x=0,y=50)
    password_again = Entry ( root, width= 20 , borderwidth=5)
    password_again.grid(row=12, column=1 ,columnspan=2, padx = 65 , pady = 10)




signin_button = Button(root, text ="Sign in",command = signin)
login_button = Button(root, text ="Log in ",command = root.quit())

signin_button.grid (row = 4, column=1)
login_button.grid (row = 4, column =3)




root.mainloop()