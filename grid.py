from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root , text = "Hello World!")
myLabel2 = Label(root , text="My name is Karthik")
#showing it onto the screen
#pack , grid

myLabel1.grid(row=0 , column=0)
myLabel2.grid(row=1 , column=5)


root.mainloop()