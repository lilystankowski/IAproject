import tkinter
from tkinter import *

import PIL.ImageOps
import self as self
# use pil to size imates
from PIL import Image, ImageTk

x_size= 1000
y_size = 800

root = Tk()  # create a root widget
root.title("outfit help")
root.configure(background="pink")
root.minsize(200, 200)  # width, height
root.maxsize(x_size, y_size)
root.geometry("800x800+50+50")  # width x height + x + y

# this is the image stuff
# size it to look nice use pil
load = Image.open("images/fredshirt.png")

render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.pack()




b = Button(root, text="---->")
b.pack(side = LEFT)
b = Button(root, text="---->")
b.pack(side = LEFT)
b = Button(root, text="---->")
b.pack(side = LEFT)





root.mainloop()