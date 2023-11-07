import tkinter
from tkinter import *

import PIL.ImageOps
import self as self
# use pil to size imates
from PIL import Image, ImageTk

x_size= 2000
y_size = 2000
a_size = 200
b_size = 200

root = Tk()  # create a root widget
root.title("outfit help")
root.configure(background="pink")
root.minsize(200, 200)  # width, height
root.maxsize(x_size, y_size)
root.geometry("800x800+50+50")  # width x height + x + y

# this is the image stuff
# size it to look nice use pil
load = Image.open("images/fredshirt.png")
load = load.resize((a_size, b_size), Image.LANCZOS)

load2 = Image.open("images/boardshorts.png")
load2 = load2.resize((a_size, b_size), Image.LANCZOS)
load3 = Image.open("images/shoes.png")
load3 = load3.resize((a_size, b_size), Image.LANCZOS)

render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.pack()

render2 = ImageTk.PhotoImage(load2)
img2 = Label(root, image=render2)
img2.image = render2
img2.pack()

render3 = ImageTk.PhotoImage(load3)
img3 = Label(root, image=render3)
img3.image = render3
img3.place(x=300,y=450)


def BTL_fun():
    load = Image.open("images/shirt1.png")
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=0)
def BTR_fun():
    load = Image.open("images/littop.png")
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=0)

def BML_fun():
    load = Image.open("images/skirtt.png")
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=205)

def BMR_fun():
    load = Image.open("images/coul.png")
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=205)

def BBL_fun():
    load = Image.open("images/lightupshoes.png")
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=450)

def BBR_fun():
    load = Image.open("images/knitshoes.png")
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=450)


button_top_left = Button(root, text="-top--->",command= BTL_fun)
button_top_left.place(x = 510, y = 100)

button_top_right = Button(root, text="<--top--", command = BTR_fun)
button_top_right.place(x= 200, y= 100)

button_middle_right  = Button(root, text="<--mid--", command = BMR_fun)
button_middle_right.place(x= 200, y= 300)

button_middle_left = Button(root, text="--mid-->", command = BML_fun)
button_middle_left.place(x= 510, y= 300)

button_bottom_right = Button(root, text="<--bot--", command = BBR_fun)
button_bottom_right.place(x= 200, y= 500)

button_bottom_left = Button(root, text="--bot-->", command = BBL_fun)
button_bottom_left.place(x= 510, y= 500)




root.mainloop()