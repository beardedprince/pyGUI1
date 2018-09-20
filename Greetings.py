import random
from tkinter import *
import time

root = Tk()
root.title("Greetings__")
root.minsize(150,250)

# defining a function to generate random phrase

def generator():
    phrases = ["Hello, welcome ", "Wow, welcome mate ", "How are you doing today? "]
    name = str(input1.get())
    return phrases[random.randint(0,3)] + name

def display():
    display_msg = generator()
    display1 = Text(master=root, height=10, width=30)
    display1.grid(column=0, row=3)
    display1.insert(END, display_msg)


label1 = Label(root, text="Welcome to my fist interactive app", fg="RED")
label1.grid(row=0, column=0)

label2 = Label(root, text="What is your name???", fg="RED")
label2.grid(row=1, column=0)
input1 = Entry(root)
input1.grid(row=1, column=1)

button1 = Button(root, text="Click Here", background="blue", command=display)
button1.grid(row=3, columnspan=2)

time_string = time.strftime('%H:%M:%S')
status = Label(root, text=time_string, relief=SUNKEN)
status.grid(row=12, sticky=N)
root.mainloop()