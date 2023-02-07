#!/usr/bin/env python3
"""
Автор Александр Говорухин, @alexitsochi
Этот скрипт собирает данные с курортов
"""

import ftplib
import requests
import json
import re
from requests.exceptions import HTTPError

ftp = ftplib.FTP()

with open("Sites.json", "r") as sites:
    Sites = json.load(sites)

with open("Sites_log_pass.json", "r") as log_pass:
    LoginPass = json.load(log_pass)

data = {
    "KP_parking": "",
    "KP_skipass": "",
    "RH_park_up": "",
    "RH_park_down": "",
    "RH_skipass": "",
    "GP_parking": "",
    "GP_skipass": ""
}


def get_data_polyana():
    try:
        ftp.connect(Sites['kp_Host'], Sites['kp_Port'])
        ftp.login(LoginPass['kp_login'], LoginPass['kp_pass'])

        ftp.cwd('/parking/')

        def find_digit_csv(data_csv):
            data_str = str(data_csv)
            digit_str = re.sub("\D", " ", data_str).strip()
            digit_str_split = digit_str.split(" ")
            data['KP_parking'] = digit_str_split[0]
            data['KP_skipass'] = digit_str_split[1]

        ftp.retrbinary('RETR ' + 'parking.csv', find_digit_csv)
        ftp.quit()

        response = "Данные от Красной Поляны получены"

    except ftplib.all_errors as fe:
        print(fe)
        response = "Данные от Красной Поляны не получены. Ошибка FTP"

    except Exception:
        response = "Данные от Красной Поляны не получены"

    return response


def set_data(dates, name_data):
    for line in dates.split(";"):
        try:
            int(line)
            if len(line) > 0:
                data[name_data] = line.strip()
                break
        except ValueError:
            continue


def get_data_rosa_hutor_up():
    try:
        ftp.connect(Sites['rh_Host'], Sites['rh_Port'])
        ftp.login(LoginPass['rh_login'], LoginPass['rh_pass'])

        def get_data_ftp(data_csv):
            d = str((data_csv.decode("utf-16")))
            set_data(d, "RH_park_up")

        ftp.retrbinary('RETR PARKING2.csv', get_data_ftp)
        ftp.quit()

        response = "Данные от Роза Хутор верх. парковка получены"
        
    except ftplib.all_errors as fe:
        print(fe)
        response = "Данные от Роза Хутор верх. парковка не получены. Ошибка FTP"

    except Exception:
        response = "Данные от Роза Хутор верх. парковка не получены."

    return response


def get_data_rosa_hutor_down():
    try:
        ftp.connect(Sites['rh_Host'], Sites['rh_Port'])
        ftp.login(LoginPass['rh_login'], LoginPass['rh_pass'])

        def get_data_ftp(data_csv):
            d = str((data_csv.decode("utf-16")))
            set_data(d, "RH_park_down")

        ftp.retrbinary('RETR PARKING1.csv', get_data_ftp)
        ftp.quit()

        response = "Данные от Роза Хутор ниж. парковка получены"

    except ftplib.all_errors as fe:
        print(fe)
        response = "Данные от Роза Хутор ниж. парковка не получены. Ошибка FTP"

    except Exception:
        response = "Данные от Роза Хутор ниж. парковка не получены."

    return response


def get_data_rosa_hutor_ski():
    try:
        ftp.connect(Sites['rh_Host'], Sites['rh_Port'])
        ftp.login(LoginPass['rh_login'], LoginPass['rh_pass'])

        def get_data_ftp(data_csv):
            d = str((data_csv.decode("cp1251")))
            set_data(d, "RH_skipass")

        ftp.retrbinary('RETR SKIPASSES.csv', get_data_ftp)
        ftp.quit()

        response = "Данные от Роза Хутор скайпасы получены"

    except ftplib.all_errors as fe:
        print(fe)
        response = "Данные от Роза Хутор скайпасы не получены. Ошибка FTP"

    except Exception:
        response = "Данные от Роза Хутор скайпасы не получены."

    return response


def get_data_gasprom():
    try:
        r = requests.get(Sites['GP_site'])
        r = r.json()
    
        data['GP_skipass'] = str(r.get('skipass_avail'))
        data['GP_parking'] = str(r.get('park_nskd_avail') + r.get('park_msa_avail') + r.get('park_alpik_avail'))
    
        response = "Данные от Газпрома получены"

    except HTTPError as he:
        print(he)
        response = "Данные от Газпрома не получены. Ошибка на сайте"

    except Exception:
        response = "Данные от Газпрома не получены."

    return response


def write_data():
    with open("Data.json", "w") as data_json:
        json.dump(data, data_json)


if __name__ == "__main__":
    get_data_polyana()
    set_data(dates, name_data)
    get_data_rosa_hutor_up()
    get_data_rosa_hutor_down()
    get_data_rosa_hutor_ski()
    get_data_gasprom()
    write_data()
