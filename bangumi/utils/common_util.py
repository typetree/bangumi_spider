import hashlib
import json
import time


def print_line(line_name):
    print("=============================={}================================".format(line_name))


def get_now_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def hashlib_md5(list):
    str = ""
    for dto in list:
        dto_json = json.dumps(dto, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        str += dto_json
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    fingerprint = m.hexdigest()
    return fingerprint
