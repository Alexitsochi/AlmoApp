#!/usr/bin/env python3
"""
Автор Александр Говорухин, @alexitsochi
Этот скрипт создает визуальный интерфейс и содержит главную функцию
"""

import tkinter
from tkinter import *
from PIL import Image, ImageTk
from threading import Timer
import datetime
import Almoping
import GetData
import CreateImg
import CreateZipAndBase64
import CreateSendXML

window = tkinter.Tk()
window.title("Вывод информации на ТПИ")
window.geometry("525x400")

podl = ImageTk.PhotoImage(Image.open("images\\podl.bmp"))

# image 1
park_label = Label(window, text="Парковки", fg="blue").place(x=10, y=10)
img_label_park = Label(window, image=podl)
img_label_park.image = podl
img_label_park.place(x=10, y=30)
# image 2
sky_label = Label(window, text="Скайпасы", fg="blue").place(x=200, y=10)
img_label_skipass = Label(window, image=podl)
img_label_skipass.image = podl
img_label_skipass.place(x=200, y=30)


def change_img():
    image_1 = ImageTk.PhotoImage(Image.open("images\\image_1_0.png"))
    img_label_park["image"] = image_1
    img_label_park.image = image_1

    image_2 = ImageTk.PhotoImage(Image.open("images\\image_1_1.png"))
    img_label_skipass["image"] = image_2
    img_label_skipass.image = image_2


def click():
    # date_time
    get_time = datetime.datetime.now()
    get_time_h = get_time.strftime("%H:%M")

#    almo = Almoping.ping_almo()
#    text.insert(1.0, get_time_h + " " + almo + "\n")

    get_polyana = GetData.get_data_polyana()
    text.insert(2.0, get_time_h + " " + get_polyana + "\n")

    get_rosahutor = GetData.get_data_rosa_hutor_up()
    text.insert(3.0, get_time_h + " " + get_rosahutor + "\n")

    get_rosahutor = GetData.get_data_rosa_hutor_down()
    text.insert(4.0, get_time_h + " " + get_rosahutor + "\n")

    get_rosahutor = GetData.get_data_rosa_hutor_ski()
    text.insert(5.0, get_time_h + " " + get_rosahutor + "\n")

    get_gasprom = GetData.get_data_gasprom()
    text.insert(6.0, get_time_h + " " + get_gasprom + "\n")

    GetData.write_data()

    create_img = CreateImg.create_img()
    text.insert(7.0, get_time_h + " " + create_img + "\n")

    change_img()

    create_zip = CreateZipAndBase64.create_zip()
    text.insert(8.0, get_time_h + " " + create_zip + "\n")

    save_xml = CreateSendXML.save_xml()
    text.insert(9.0, get_time_h + " " + save_xml + "\n")

#    send_xml = CreateSendXML.send_xml()
#    text.insert(10.0, get_time_h + " " + send_xml + "\n")

    text.insert(11.0, "#"*60 + "\n")

    time_timer = 60 * int('{}'.format(entry_timer.get()))
    timer = Timer(time_timer, click)
    timer.start()


# timer
label_timer = Label(window, text="Таймер в минутах", fg="blue").place(x=380, y=65)
entry_timer = Entry(window, width=10)
entry_timer.place(x=400, y=85)
# btn
btn = Button(text="Запустить", bg="red", fg="black", command=click).place(x=400, y=30)
# textarea
text = Text(width=62, height=15)
text.place(x=10, y=130)


if __name__ == "__main__":
    change_img()
    click()
    window.mainloop()
