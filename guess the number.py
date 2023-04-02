from tkinter import *
from random import randint
import tkinter.messagebox as mb

root  = Tk()
root.title('Guess the number')
root.geometry('250x200')
root.resizable(False, False)

secret = randint(1, 1000)
def prow():
    user = ent.get()
    user= int(user)
    if user > secret:
        mb.showwarning("smaller")
    elif user < secret:
        mb.showwarning("bigger")
    else:
        mb.showwarning("guessed right")

ent = Entry(root, width=25)
ent.place(x=20, y=25)

but = Button(root, text = 'check', width=25, command=prow)
but.place(x=20,y=65)

root.mainloop()

