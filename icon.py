from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Karthik')
root.iconbitmap('C:/Users/maxwh/Desktop/Tkinter Course/images/icon.ico')

my_img = ImageTk.PhotoImage(Image.open('images/asprin.png'))
my_label = Label(image=my_img)
my_label.pack()






button_quit = Button(root, text="Exit Program" ,command=root.quit)
button_quit.pack()



root.mainloop()