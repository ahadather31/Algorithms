import tkinter

import random

#names:
names = ['Joe','Bob','Bob-Joe','George','Phil','Squid','SpongeBob','Crab','ChickenMan','Me']

def pickName():
    nameLabel.configure(text = random.choice(names))


root = tkinter.Tk()

root.title("Name Picker")

root.geometry("500x400")

nameLabel = tkinter.Label(root, text = "", font = ('Cursive', 32))
nameLabel.pack()


pickButton = tkinter.Button(text = "Pick!", command = pickName)
pickButton.pack()

root.mainloop()
