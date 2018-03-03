# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback
from queue import Queue

import time

from bangumi.client import mysql_client
from bangumi.dto import basic_person_dto
from bangumi.service import basic_person_service, spider_version_person_service
from bangumi.spider import basic_person_spider
from bangumi.utils import my_exception


def get_bangumi_person_id(person_soup_queue:Queue, start_id=1):

    flag = True
    break_num = 0
    while flag:
        soup = basic_person_spider.get_person_soup(start_id)
        names = soup.select("#headerSubject > h1 > a")
        if names is None or len(names) <= 0:
            break_num += 1
            continue

        print("人物页面队列添加 id:{}, name:{}".format(start_id, names[0].get_text()))
        person_soup_queue.put({"id": start_id, "soup": soup})

        if break_num == 20:
            break
        start_id += 1


def get_person_data(person_soup_queue:Queue, person_data_queue:Queue):

    while True:
        if person_soup_queue.empty():
            time.sleep(1)
            continue
        try:
            soup_list = person_soup_queue.get()

            data = basic_person_spider.get_person_by_soup(soup_list['id'], soup_list['soup'])
            if data is None:
                continue
            print("人物数据队列添加 id:{}, name:{}".format(data.bangumi_person_id, data.name))
            person_data_queue.put(data)
        except Exception as e:
            print("报错重试", traceback.format_exc())
    pass


def write_database(person_data_queue:Queue):
    while True:
        if person_data_queue.empty():
            time.sleep(1)
            continue
        try:
            conn = mysql_client.get_connect()
            data = person_data_queue.get()
            svpd = spider_version_person_service.create_by_bangumi_person_id(conn, data.bangumi_person_id)

            person_dto = basic_person_service.spider_create(conn, data)
            spider_version_person_service.update_by_person_dto(conn, svpd, person_dto, 'basic_person_add_main')
        except my_exception.MyException as e:
            log = e.message
            spider_version_person_service.unable_version(conn, svpd, 'basic_person_add_main', log)
        except Exception :
            log = traceback.format_exc()
            print("报错重试", log)
            spider_version_person_service.unable_version(conn, svpd, 'basic_person_add_main', log)
        finally:
            conn.close()


if __name__ == "__main__":

    conn = mysql_client.get_connect()
    start_id = spider_version_person_service.find_max_bangumi_person_id(conn)

    person_soup_queue = Queue()
    person_data_queue = Queue()

    threading.Thread(target=get_bangumi_person_id, args=(person_soup_queue, start_id,)).start()

    for i in range(0, 4):
        threading.Thread(target=get_person_data, args=(person_soup_queue, person_data_queue)).start()

    threading.Thread(target=write_database, args=(person_data_queue,)).start()
    pass

    # conn = mysql_client.get_connect()
    # # start_id = spider_version_person_service.find_max_bangumi_person_id(conn)
    # start_id = 22
    #
    # soup = basic_person_spider.get_person_soup(start_id)
    #
    # data = basic_person_spider.get_person_by_soup(start_id, soup)
    #
    # svpd = spider_version_person_service.create_by_bangumi_person_id(conn, data.bangumi_person_id)
    #
    # person_dto = basic_person_service.spider_create(conn, data)
    # spider_version_person_service.update_by_person_dto(conn, svpd, person_dto, 'basic_person_add_main')