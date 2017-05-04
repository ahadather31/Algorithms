import tkinter


app = tkinter.Tk()
app.configure(background = "#00ffd0")
app.wm_iconbitmap("favicon.ico")
app.title("Rainbow")


myarray = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]

for i in myarray:
	btn = tkinter.Button(text = i, bg = i)
	btn.pack(fill = tkinter.X)


app.mainloop()
