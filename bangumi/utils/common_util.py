import time


def print_line(line_name):
    print("=============================={}================================".format(line_name))


def get_now_time():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

