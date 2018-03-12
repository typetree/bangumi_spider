# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from multiprocessing import Process, Queue

import time

from bangumi.client import mysql_client
from bangumi.constants import table_constants
from bangumi.factory import subject_strategy_factory
from bangumi.service import subject_info_service, basic_profession_service
from bangumi.spider import subject_info_spider
from bangumi.utils import common_util

global id_flag


def get_id_queue(id_queue:Queue, start_id):

    id_flag = True
    while id_flag:
        if id_queue.full():
            continue
        id_queue.put(start_id)
        start_id += 1


def get_dto_soup_queue(subject_soup_queue, id_queue,
                       subject_profession_person_queue, category_professions, max_thread_num=4):
    for i in range(0, max_thread_num):
        threading.Thread(target=get_dto_queue,
                         args=(subject_soup_queue,
                               id_queue, subject_profession_person_queue, category_professions,)).start()


def get_dto_queue(subject_dto_queue:Queue,
                  id_queue:Queue, subject_profession_person_queue:Queue, category_professions):
    try:
        while True:
            if id_queue.empty()  or subject_dto_queue.full() or subject_profession_person_queue.full():
                print("queue is full")
                time.sleep(1)
                continue
            start_id = id_queue.get()
            print("作品id:{}，开始爬取数据".format(start_id))
            soup = subject_info_spider.get_subject_soup(start_id)
            data = subject_info_spider.get_message_by_soup(soup)
            if data is None:
                start_id += 1
                continue

            category = data['category']

            target_method = subject_strategy_factory.get_subject_detail_spider_by_category(category)
            if target_method is None:
                start_id += 1
                continue

            dto = target_method(soup, data, subject_profession_person_queue, category_professions[category])
            subject_dto_queue.put(dto)
            start_id += 1
    except Exception:
        print(traceback.format_exc())


def write_subject_profession_person(subject_profession_person_queue:Queue):

    while True:
        if subject_profession_person_queue.empty():
            continue
        sppd = subject_profession_person_queue.get()
        print("subject_profession_person数据插入, person_id:{}, person_name:{}, profession_id:{}, profession_name:{}"
              .format(sppd.person_id, sppd.person_name, sppd.profession_id, sppd.profession_name))



def write_db(subject_dto_queue:Queue):

    while True:
        if subject_dto_queue.empty():
            continue
        dto = subject_dto_queue.get()
        print("subject_info插入数据, bangumi_subject_id:{}, name:{}".format(dto.bangumi_subject_id, dto.name))



if __name__ == "__main__":

    try:
        conn = mysql_client.get_connect()
        start_id = subject_info_service.find_max_bangumi_id(conn)
        # start_id = 50
        categorys = table_constants.get_categorys()
        category_professions = {}
        for category in categorys.values():
            dicts = basic_profession_service.find_dict_by_category(conn, category)
            category_professions[category] = dicts
        conn.close()

        id_queue = Queue(maxsize=30)
        subject_dto_queue = Queue(maxsize=30)
        subject_profession_person_queue = Queue(maxsize=30)

        threading.Thread(target=get_id_queue, args=(id_queue, start_id,)).start()

        for i in range(0, 2):
            Process(target=get_dto_soup_queue,
                    args=(subject_dto_queue, id_queue,
                          subject_profession_person_queue, category_professions, 2,)).start()

        for i in range(0, 2):
            threading.Thread(target=write_subject_profession_person, args=(subject_profession_person_queue,)).start()

        threading.Thread(target=write_db, args=(subject_dto_queue,)).start()


    except Exception:
        print(traceback.format_exc())