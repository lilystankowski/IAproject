import tkinter
from tkinter import *
from tkinter import  filedialog

import PIL.ImageOps
import self as self
# use pil to size imates
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageDraw
import shutil

from PIL import Image

import os

shoes_pat = "image_s"
shoes_list = os.listdir(shoes_pat)
print(shoes_list)
shoes_index_counter = 0

pant_pat = "image_p"
pant_list = os.listdir(pant_pat)
print(pant_list)
pant_index_counter = 0

top_pat = "image_t"
top_list = os.listdir(top_pat)
print(top_list)
top_index_counter = 0




x_size= 2000
y_size = 2000
a_size = 200
b_size = 200

root = Tk()  # create a root widget
root.title("outfit help")
root.configure(background="black")
root.minsize(200, 200)  # width, height
root.maxsize(x_size, y_size)
root.geometry("800x800+50+50")  # width x height + x + y

# this is the image stuff
# size it to look nice use pil
load = Image.open("image_t/tassel summer shirt.png")
load = load.resize((a_size, b_size), Image.LANCZOS)

load2 = Image.open("image_p/valpant.png")
load2 = load2.resize((a_size, b_size), Image.LANCZOS)

load3 = Image.open("image_s/shoes.png")
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
img3.pack()


def BTL_fun():
    global top_index_counter
    if top_index_counter > 0:
        top_index_counter = top_index_counter - 1
    load = Image.open("image_t/" + top_list[top_index_counter])
    print(top_list[top_index_counter])
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300, y=0)

def BTR_fun():
    global top_index_counter
    if top_index_counter < len(top_list) - 1:
        top_index_counter = top_index_counter + 1
    load = Image.open("image_t/" + top_list[top_index_counter])
    print(top_list[top_index_counter])
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300, y=0)


def BML_fun():
    global pant_index_counter
    if pant_index_counter > 0:
        pant_index_counter = pant_index_counter - 1
    print(pant_index_counter)
    load2 = Image.open("image_p/" + pant_list[pant_index_counter])
    load2 = load2.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load2)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300, y=205)

def BMR_fun():
    global pant_index_counter
    if pant_index_counter < len(pant_list) - 1:
        pant_index_counter = pant_index_counter + 1
    print(pant_index_counter)
    load2 = Image.open("image_p/" + pant_list[pant_index_counter])
    load2 = load2.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load2)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=205)

def BBL_fun():
    global shoes_index_counter
    if shoes_index_counter > 0:
        shoes_index_counter = shoes_index_counter -1
    load = Image.open("image_s/" + shoes_list[shoes_index_counter])
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=450)

def BBR_fun():
    global shoes_index_counter
    if shoes_index_counter < len(shoes_list)-1:
        shoes_index_counter = shoes_index_counter + 1
    load = Image.open("image_s/" + shoes_list[shoes_index_counter])
    load = load.resize((a_size, b_size), Image.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=300,y=450)

def save_image():
    print("save_image")
    image2 = Image.open('image_p/'+pant_list[pant_index_counter])
    #image1.show()
    image3 = Image.open('image_s/'+shoes_list[shoes_index_counter])
    #image2.show()
    image1 = Image.open('image_t/'+top_list[top_index_counter])
    # resize, first image
    image1 = image1.resize((300, 300))
    image2 = image2.resize((300, 300))
    image3 = image3.resize((300, 300))

    image1_size = image1.size
    image2_size = image2.size
    image3_size = image3.size


    new_image = Image.new('RGB', ( image1_size[0], 3*image1_size[1]), (250, 250, 250))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, 300))
    new_image.paste(image3, (0, 600))
    new_image.save("merged_image.jpg", "JPEG")
    new_image.show()

def add_tops():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        files = os.listdir(folder_selected)
        for file in files:
            full_file_path = os.path.join(folder_selected, file)
            if os.path.isfile(full_file_path):
                shutil.copy(full_file_path,"image_t")

def add_shoes():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        files = os.listdir(folder_selected)
        for file in files:
            full_file_path = os.path.join(folder_selected, file)
            if os.path.isfile(full_file_path):
                shutil.copy(full_file_path,"image_s")

def add_pants():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        files = os.listdir(folder_selected)
        for file in files:
            full_file_path = os.path.join(folder_selected, file)
            if os.path.isfile(full_file_path):
                shutil.copy(full_file_path,"image_p")



button_top_left = Button(root, text="---->",command= BTL_fun)#top
button_top_left.place(x = 510, y = 100)

button_top_right = Button(root, text="<----", command = BTR_fun)#top
button_top_right.place(x= 200, y= 100)

button_middle_right  = Button(root, text="<----", command = BMR_fun)#middle
button_middle_right.place(x= 200, y= 300)

button_middle_left = Button(root, text="---->", command = BML_fun)#middle
button_middle_left.place(x= 510, y= 300)

button_bottom_right = Button(root, text="<----", command = BBR_fun)#bottom
button_bottom_right.place(x= 200, y= 500)

button_bottom_left = Button(root, text="---->", command = BBL_fun)#bottom
button_bottom_left.place(x= 510, y= 500)

button_bottom_left = Button(root, text="save look", command = save_image)#bottom
button_bottom_left.place(x= 650, y= 750)

button_new_tops = Button(root, text="new_tops", command = add_tops)#new tops
button_new_tops.place(x= 50, y= 650)

button_new_shoes = Button(root, text="new_bottoms", command = add_shoes)#new shoes
button_new_shoes.place(x= 50, y= 700)

button_new_shoes = Button(root, text="new_shoes", command = add_shoes)#new shoes
button_new_shoes.place(x= 50, y= 750)



list_im = ['.jpg','Test2.jpg','Test3.jpg']








root.mainloop()