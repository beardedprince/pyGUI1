import random
from tkinter import *

root = Tk()
root.title("Greetings__")
root.minsize(400,500)

label1 = Label(root, text="Welcome to my fist interactive app", fg="RED")
label1.grid(column=1, row=0)

label2 = Label(root, text="What is your name???", fg="RED")
label2.grid(column=0, row=1)
input1 = Entry(root)
input1.grid(column=1, row=1)

button1 = Button(root, text="Click Here", background="blue")
button1.grid(columnspan=2)

root.mainloop()