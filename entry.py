from tkinter import *

root = Tk()

e = Entry(root , width= 50 , borderwidth = 5)
e.pack()
#get function gets everything whatever you typed
#e.get()
e.insert(0, "Enter Your Stock Quote: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root , text= hello)
    myLabel.pack()

#state = DISABLED can be used to keep the button inactive
#we can change the size of the button using padx for x axis and pady for y axis
#we can use command for executing function when we click a button
myButton = Button(root , text="Enter Your Name" , padx=50 , command=myClick , fg="blue" , bg="#000000")
myButton.pack()
root.mainloop()

