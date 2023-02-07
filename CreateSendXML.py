#!/usr/bin/env python3
"""
Автор Александр Говорухин, @alexitsochi
Этот скрипт создает xml-файл и отсылает его на сервер
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from CreateZipAndBase64 import *

with open("tpi.txt", "r") as tpi_txt:
    tpi_list = tpi_txt.read().split(";")


def create_xml(elem_tpi):

    create_zip()

    xml = (f"""<?xml version='1.0' encoding='utf-8' standalone='no'?>
        <soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
            <soap:Body>
            <signcmd xmlns='http://nissen.de/ilias'>
                <id>{elem_tpi}</id>
                <applicant>AdminConsole</applicant>
                <transaction>04040</transaction>
                <action>
                <cmd>led-new</cmd>
                <sign>
                    <id>1</id>
                    <selnumber>253</selnumber>
                    <picdef>
                    <pages>2</pages>
                    <page>
                        <time>3000</time>
                        <flash>false</flash>
                        <name>image_1_0.bmp</name>
                        <data>{arr_xml_str[0]}</data>
                    </page>
                    <page>
                        <time>3000</time>
                        <flash>false</flash>
                        <name>image_1_1.bmp</name>
                        <data>{arr_xml_str[1]}</data>
                    </page>
                    </picdef>
                </sign>
                </action>
            </signcmd>
            </soap:Body>
        </soap:Envelope>""")

    return xml


def save_xml():

    response = ""

    for elem_tpi in tpi_list:
        xml = create_xml(elem_tpi)
        f = open(f"xml\\Almo{elem_tpi}.xml", "w")
        f.write(xml)
        f.close()

        response = "XML сформированы"

    return response


def send_xml():

    response = ""

    options = Options()
    options.add_argument("--headless")  # режим без графики

    try:
        for elem_tpi in tpi_list:
            driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
            driver.get(f"http://172.16.160.53:8020/modem/cmd.jsp?id={elem_tpi}")

            textarea = driver.find_element_by_name("xml")
            textarea.clear()

            with open(f"xml\\Almo{elem_tpi}.xml", "r") as Xml:
                xml_text = Xml.read()

            textarea.send_keys(xml_text)
            driver.find_element_by_tag_name("input").click()
            driver.close()

            response = "Информация отправлена"

    except Exception:

            response = "Информация не отправлена"

    return response


if __name__ == "__main__":
    create_xml(elem_tpi)
    save_xml()
    send_xml()
