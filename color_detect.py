import tkinter
import os
from tkinter import *
from tkinter import filedialog

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
from colorthief import ColorThief
from numpy import asarray

root = Tk()
root.title('color')
root.geometry('1000x700+100+100')
root.configure(bg='white')
root.resizable(False, False)


# declaring global variables (are used later on)

def openNewWindow():
    gry_img = img.convert('L')
    print(gry_img)
    gry_img.save('C:/Users/Admin/PycharmProjects/pythonProject/abc.jpg')
    print('abc')

    a = img
    path = 'C:/Users/Admin/PycharmProjects/pythonProject/*'
    rotate = a.rotate(90, expand=True)
    rotate.save('__rotate.png')

    flt_arr = img_arr.ravel()
    plt.hist(flt_arr, bins=256, color='gray')
    plt.show()

    hist, bins = np.histogram(img_arr.flatten(), bins=256)

    # Create pie chart
    fig, ax = plt.subplots()
    img_arr2 = np.sum(img_arr, axis=0)
    ax.pie(hist, labels=bins[:-1], startangle=90, counterclock=False, wedgeprops={'edgecolor': 'gray'},
           autopct='%500.1f%%')
    # ax.set_aspect('equal')
    ax.set_title('Pixel Intensity Distribution')
    plt.show()
    print(img_arr2)

    # -------------------------------------------------------------------------------------------------------------------------

    global file
    global img1
    global csv
    global clicked
    global b
    global g
    global r
    global xpos
    global ypos

    clicked = False
    img1 = cv2.imread(file)
    img1 = cv2.resize(img1, (500, 500))
    # Reading csv file with pandas and giving names to each column
    index = ["color", "color_name", "hex", "R", "G", "B"]
    csv = pd.read_csv("color.csv", names=index, header=None)

    # function to get x,y coordinates of mouse double click

    def draw_function(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            clicked = True
            xpos = x
            ypos = y
            b, g, r = img1[y, x]
            b = int(b)
            g = int(g)
            r = int(r)
            print(r, g, b)
            cv2.rectangle(img1, (20, 20), (750, 60), (b, g, r), -1)
            text = ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
            cv2.putText(img1, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            if (r + g + b >= 600):
                cv2.putText(img1, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    def getColorName(r, g, b):
        minimum = 10000
        print("xyz")
        for i in range(len(csv)):
            d = abs(r - int(csv.loc[i, "R"])) + abs(g - int(csv.loc[i, "G"])) + abs(b - int(csv.loc[i, "B"]))
            print(d)
            if (d <= minimum):
                minimum = d
                cname = csv.loc[i, "color_name"]
                print(cname)
        return cname

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_function, 0)

    # function to calculate minimum distance from all colors and get the most matching color

    clicked = False
    while (1):
        cv2.imshow("image", img1)
        if (clicked):
            print("xyz")
            # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            cv2.rectangle(img1, (20, 20), (750, 60), (b, g, r), -1)

            # Creating text string to display( Color name and RGB values )
            text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

            # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv2.putText(img1, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

            # For very light colours we will display text in black colour
            if (r + g + b >= 600):
                cv2.putText(img1, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            print('llllll')
            clicked = False

        # Break the loop when user hits 'esc' key

        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


def img():
    global file
    global img_arr
    global img
    file = filedialog.askopenfilename(initialdir=os.getcwd()
                                      , title='Select Img',
                                      filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'), ('All file', '*.txt'),
                                                 ('Avif file', '*.avif')))
    img = Image.open(file)
    resize_image = img.resize((450, 400))
    resize_image = ImageTk.PhotoImage(resize_image)
    lbl.configure(image=resize_image, width=460, height=400)
    lbl.image = resize_image
    img_arr = asarray(img)


def dect_color():
    ct = ColorThief(file)
    plt = ct.get_palette(color_count=11)

    rgb1 = plt[0]
    rgb2 = plt[1]
    rgb3 = plt[2]
    rgb4 = plt[3]
    rgb5 = plt[4]
    rgb6 = plt[5]
    rgb7 = plt[6]
    rgb8 = plt[7]
    rgb9 = plt[8]
    rgb10 = plt[9]

    colors1 = f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    colors21 = f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    colors3 = f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    colors4 = f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    colors5 = f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    colors6 = f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    colors7 = f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    colors8 = f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    colors9 = f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    colors10 = f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"

    colors.itemconfig(id1, fill=colors1)
    colors.itemconfig(id2, fill=colors21)
    colors.itemconfig(id3, fill=colors3)
    colors.itemconfig(id4, fill=colors4)
    colors.itemconfig(id5, fill=colors5)

    colors2.itemconfig(id6, fill=colors6)
    colors2.itemconfig(id7, fill=colors7)
    colors2.itemconfig(id8, fill=colors8)
    colors2.itemconfig(id9, fill=colors9)
    colors2.itemconfig(id10, fill=colors10)

    h1.config(text=f"R:{rgb1[0]} G:{rgb1[1]} B:{rgb1[2]}")
    h2.config(text=f"R:{rgb2[0]} G:{rgb2[1]} B:{rgb2[2]}")
    h3.config(text=f"R:{rgb3[0]} G:{rgb3[1]} B:{rgb3[2]}")
    h4.config(text=f"R:{rgb4[0]} G:{rgb4[1]} B:{rgb4[2]}")
    h5.config(text=f"R:{rgb5[0]} G:{rgb5[1]} B:{rgb5[2]}")
    h6.config(text=f"R:{rgb6[0]} G:{rgb6[1]} B:{rgb6[2]}")
    h7.config(text=f"R:{rgb7[0]} G:{rgb7[1]} B:{rgb7[2]}")
    h8.config(text=f"R:{rgb8[0]} G:{rgb8[1]} B:{rgb8[2]}")
    h9.config(text=f"R:{rgb9[0]} G:{rgb9[1]} B:{rgb9[2]}")
    h10.config(text=f"R:{rgb10[0]} G:{rgb10[1]} B:{rgb10[2]}")


# icon = PhotoImage(file='icon.png')
# root.iconphoto(False, icon)

Label(root, width=300, height=15, bg='#4272f9').pack()

frame = Frame(root, width=900, height=550, bg='white')
frame.place(x=50, y=60)

logo = PhotoImage(file='logo.png')
Label(frame, image=logo, bg='#fff').place(x=20, y=15)
Label(frame, text='Color detection', font='arial 12 bold', bg='white').place(x=100, y=25)

colors = Canvas(frame, bg='silver', width=400, height=490, bd=10)
colors.place(x=20, y=90)
id1 = colors.create_rectangle((20, 50, 100, 120), fill='#b8255f')
id2 = colors.create_rectangle((100, 200, 20, 100), fill='#db4035')
id3 = colors.create_rectangle((100, 300, 20, 150), fill='#ff9933')
id4 = colors.create_rectangle((100, 400, 20, 200), fill='#fad000')
id5 = colors.create_rectangle((100, 200, 20, 250), fill='#afb83b')

# clr_1
h1 = Label(colors, text='#b8255f', fg='#000', font='arial 8 bold', bg='white')
h1.place(x=103, y=65)

h2 = Label(colors, text='#db4035', fg='#000', font='arial 8 bold', bg='white')
h2.place(x=103, y=115)

h3 = Label(colors, text='#ff9933', fg='#000', font='arial 8 bold', bg='white')
h3.place(x=103, y=165)

h4 = Label(colors, text='#fad000', fg='#000', font='arial 8 bold', bg='white')
h4.place(x=103, y=215)

h5 = Label(colors, text='#afb83b', fg='#000', font='arial 8 bold', bg='white')
h5.place(x=103, y=265)

# clr_2
colors2 = Canvas(frame, bg='silver', width=400, height=490, bd=10)
colors2.place(x=220, y=90)

id6 = colors2.create_rectangle((100, 100, 20, 50), fill='#7ecc49')
id7 = colors2.create_rectangle((100, 200, 20, 100), fill='#299438')
id8 = colors2.create_rectangle((100, 300, 20, 150), fill='#6accbc')
id9 = colors2.create_rectangle((100, 400, 20, 200), fill='#158fad')
id10 = colors2.create_rectangle((100, 200, 20, 250), fill='#14aaf5')

h6 = Label(colors2, text='#7ecc49', fg='#000', font='arial 8 bold', bg='white')
h6.place(x=110, y=65)

h7 = Label(colors2, text='#299438', fg='#000', font='arial 8 bold', bg='white')
h7.place(x=110, y=115)

h8 = Label(colors2, text='#6accbc', fg='#000', font='arial 8 bold', bg='white')
h8.place(x=110, y=165)

h9 = Label(colors2, text='#158fad', fg='#000', font='arial 8 bold', bg='white')
h9.place(x=110, y=215)

h10 = Label(colors2, text='#14aaf5', fg='#000', font='arial 8 bold', bg='white')
h10.place(x=110, y=265)

# slct img

select_img = Frame(frame, width=490, height=490, bg='black')
select_img.place(x=430, y=90)

fr = Frame(select_img, bd=5, bg='black', width=460, height=400, relief=GROOVE)
fr.place(x=5, y=5)

lbl = Label(fr, bg='black')
lbl.place(x=-5, y=0)

Button(select_img, text='Select img', width=12, height=1, font="arial 14 bold", command=img).place(x=60, y=420)
Button(select_img, text='Detect color', width=12, height=1, font="arial 14 bold", command=dect_color).place(x=250,
                                                                                                            y=420)
push = Button(frame, text='Info', width=12, height=1, font='arial 14 bold', command=openNewWindow).place(x=150, y=510)

root.mainloop()

# -------------------------------------------------------------------------------------------------------------
