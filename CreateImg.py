import json
from PIL import Image, ImageFont, ImageDraw

with open("Data.json", "r") as Data:
    reader = json.load(Data)


def set_color_text(text_value="0"):
    # цвет текста в зависимости от значения
    color = "Black"
    try:
        if int(text_value) > 50:
            color = "Black"
        elif (int(text_value) <= 50) and (int(text_value) > 10):
            color = "Yellow"
        else:
            color = "Red"
    except Exception:
        pass

    return color


def set_width_text(text_value, width):
    # позиция цифр по x-оси в зависимости от их количества
    if len(text_value) == 4:
        text_coord_x = width - 24
    elif len(text_value) == 3:
        text_coord_x = width - 17
    elif len(text_value) == 2:
        text_coord_x = width - 12
    else:
        text_coord_x = width - 7

    return text_coord_x


def create_img():
    # create img 1
    image = Image.open('BackPark.bmp')
    width, height = image.size
    idraw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font\\test.ttf", 12, encoding="UTF-8")
    # text variables block
    text = "Количество"
    text2 = "Парковочных   мест"
    text_rhd = "Роза Хутор Низ"
    text_rhd_value = reader["RH_park_down"]
    text_rhu = "Роза Хутор Верх"
    text_rhu_value = reader["RH_park_up"]
    text_kp = "Крас . Поляна"
    text_kp_value = reader["KP_parking"]
    text_gp = "Газпром"
    text_gp_value = reader["GP_parking"]
    # add text 1
    idraw.text((28, 2), text, font=font, fill="Black")
    idraw.text((5, 15), text2, font=font, fill="Black")
    idraw.line((0, 29, 128, 29), width=1, fill="Black")
    # 1
    idraw.text((1, 30), text_rhd, font=font, fill=set_color_text(text_rhd_value))
    idraw.text((set_width_text(text_rhd_value, width), 30), text_rhd_value, font=font, fill=set_color_text(text_rhd_value))
    # 2
    idraw.text((1, 43), text_rhu, font=font, fill=set_color_text(text_rhu_value))
    idraw.text((set_width_text(text_rhu_value, width), 43), text_rhu_value, font=font, fill=set_color_text(text_rhu_value))
    # 3
    idraw.text((1, 56), text_kp, font=font, fill=set_color_text(text_kp_value))
    idraw.text((set_width_text(text_kp_value, width), 56), text_kp_value, font=font, fill=set_color_text(text_kp_value))
    # 4
    idraw.text((1, 69), text_gp, font=font, fill=set_color_text(text_gp_value))
    idraw.text((set_width_text(text_kp_value, width), 69), text_gp_value, font=font, fill=set_color_text(text_gp_value))
    # save img1
    image.save("images\\image_1_0.png")

    # create image 2
    image = Image.new("RGB", (128, 84), "white")
    idraw = ImageDraw.Draw(image)
    text2 = "Билетов    Skipass"
    text_rhs = "Роза Хутор"
    text_rhs_value = reader["RH_skipass"]
    text_kps = "Крас . Поляна"
    text_kps_value = reader["KP_skipass"]
    text_gp = "Газпром"
    text_gp_value = reader["GP_skipass"]
    # add text 2
    idraw.text((28, 2), text, font=font, fill="black")
    idraw.text((15, 15), text2, font=font, fill="black")
    idraw.line((0, 29, 128, 29), width=1, fill="black")
    # 1
    idraw.text((2, 33), text_rhs, font=font, fill=set_color_text(text_rhs_value))
    idraw.text((set_width_text(text_rhs_value, width), 33), text_rhs_value, font=font, fill=set_color_text(text_rhs_value))
    # 2
    idraw.text((2, 48), text_kps, font=font, fill=set_color_text(text_kps_value))
    idraw.text((set_width_text(text_kps_value, width), 48), text_kps_value, font=font, fill=set_color_text(text_kps_value))
    # 3
    idraw.text((2, 64), text_gp, font=font, fill=set_color_text(text_gp_value))
    idraw.text((set_width_text(text_gp_value, width), 64), text_gp_value, font=font, fill=set_color_text(text_gp_value))
    # save img 1
    image.save("images\\image_1_1.png")

    return "Изображения сформированы"

