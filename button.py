from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root , text="Your Click was success")
    myLabel.pack()

#state = DISABLED can be used to keep the button inactive
#we can change the size of the button using padx for x axis and pady for y axis
#we can use command for executing function when we click a button
myButton = Button(root , text="Click Me!" , padx=50 , command=myClick , fg="blue" , bg="#000000")
myButton.pack()
root.mainloop()

