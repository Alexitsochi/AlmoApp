#!/usr/bin/env python3
"""
Автор Александр Говорухин, @alexitsochi
Этот скрипт создает архив и шифрует его в строку base64
"""

import base64
import zipfile

arr_xml_str = []


def create_zip():
    zip_img = zipfile.ZipFile('zip\\image_1_0.zip', 'w')
    zip_img.write('images\\image_1_0.png', arcname='image_1_0.bmp')
    zip_img.close()

    zip_img = zipfile.ZipFile('zip\\image_1_1.zip', 'w')
    zip_img.write('images\\image_1_1.png', arcname='image_1_1.bmp')
    zip_img.close()

    with open("zip\\image_1_0.zip", "rb") as zfile:
        encoded_string1 = base64.b64encode(zfile.read())

    with open("zip\\image_1_1.zip", "rb") as zfile:
        encoded_string2 = base64.b64encode(zfile.read())

    arr_xml_str.append(encoded_string1.decode('utf-8'))
    arr_xml_str.append(encoded_string2.decode('utf-8'))

    response = "Zip файлы сформированы"

    return response

if __name__ == "__main__":
    create_zip()
