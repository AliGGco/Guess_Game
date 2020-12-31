#imports
from tkinter import *
import random  #for getting random numbers
from tkinter import messagebox
#main root
root = Tk()
root.title("Guess Number")
root.geometry('275x50')
#labels
label = Label(root, text="The Number is")
label.grid(column=1, row=0)

label1 = Label(root, text="Enter your guess")
label1.grid(column=1, row=2)
#entery
Entr = StringVar()
Entry1 = Entry(root, textvariable=Entr, show="*", justify='right', state="readonly")
Entry1.grid(row=0, column=2)
Entr1 = StringVar()
Entr1.trace("w", lambda name, index, mode, Entr1=Entr1: callback(Entr1))
Entry2 = Entry(root, textvariable=Entr1, justify='right')
Entry2.grid(row=2, column=2)
Entr2 = StringVar()
label1 = Label(root, textvariable=Entr2)
label1.grid(column=3, row=2)

#function
def clicked():
    num = random.randint(1, 101)
    Entr.set(str(num))
def callback(Entr1):
    #conditions
    if (Entr1.get() < Entr.get()):
         Entr2.set("Try Higher")
    elif (Entr1.get() > Entr.get()):
         Entr2.set("Try Lower")
    else:
        messagebox.showinfo("", "You Got it!")
#button
button = Button(root, text="Generate", command=clicked)
button.grid(column=3, row=0)
#main loop
root.mainloop()
