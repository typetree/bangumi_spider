import datetime
import hashlib
import json
import time


def print_line(line_name):
    print("=============================={}================================".format(line_name))


def get_now_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def object_to_json(dto):
    dto_json = json.dumps(dto, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
    return dto_json


def hashlib_md5(list):
    str = ""
    for dto in list:
        str += object_to_json(dto)
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    fingerprint = m.hexdigest()
    return fingerprint


def format_YYMMDD(date: str):
    date = date.replace('年', '-')
    date = date.replace('月', '-')
    date = date.replace('日', '')
    fmt = '%Y-%m-%d'
    time_tuple = time.strptime(date, fmt)
    year, month, day = time_tuple[:3]
    a_date = datetime.datetime(year, month, day, 0, 0)
    return a_date

