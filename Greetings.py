import random
from tkinter import *

root = Tk()
root.title("Greetings__")
root.minsize(400,500)

# defining a function to generate random phrase

def generator():
    phrases = ["Hello, welcome ", "Wow, welcome mate ", "How are you doing today? "]
    name = str(input1.get())
    return phrases[random.randint(0,3)] + name

def display():
    display_msg = generator()
    display1 = Text(master=root, height=10, width=30)
    display1.grid(column=0, row=3)
    display1.insert(root.END, display_msg)


label1 = Label(root, text="Welcome to my fist interactive app", fg="RED")
label1.grid(column=1, row=0)

label2 = Label(root, text="What is your name???", fg="RED")
label2.grid(column=0, row=1)
input1 = Entry(root)
input1.grid(column=1, row=1)

button1 = Button(root, text="Click Here", background="blue", command=generator)
button1.grid(column=0, row=2)

root .mainloop()