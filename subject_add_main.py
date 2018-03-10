# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from multiprocessing import Process, Queue

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


def get_dto_soup_queue(subject_soup_queue, subject_message_queue, id_queue,
                       subject_profession_person_queue, category_professions, max_thread_num=4):
    for i in range(0, max_thread_num):
        threading.Thread(target=get_dto_queue,
                         args=(subject_soup_queue, subject_message_queue,
                               id_queue, subject_profession_person_queue, category_professions,)).start()


def get_dto_queue(subject_dto_queue:Queue, subject_message_queue:Queue,
                  id_queue:Queue, subject_profession_person_queue:Queue, category_professions):
    try:
        while True:
            if id_queue.empty() or subject_message_queue.full():
                continue
            start_id = id_queue.get()
            soup = subject_info_spider.get_subject_soup(start_id)
            data = subject_info_spider.get_message_by_soup(soup)
            if data is None:
                start_id += 1
                continue

            category = data['category']
            if category != 'GAME':
                start_id += 1
                continue

            target_method = subject_strategy_factory.get_subject_detail_spider_by_category(category)
            if target_method is None:
                start_id += 1
                continue

            dto = target_method(soup, data, subject_profession_person_queue, category_professions[category])
            subject_message_queue.put(data)
            subject_dto_queue.put(dto)
            start_id += 1
    except Exception:
        print(traceback.format_exc())


def get_subject_soup_id(subject_soup_queue:Queue, start_id):
    pass


def get_subject_data(subject_soup_queue:Queue, subject_data_queue):
    pass


def insert_db(subject_message_queue:Queue):

    conn = mysql_client.get_connect()
    while True:
        if subject_message_queue.empty():
            continue
        data = subject_message_queue.get()

        dto = subject_info_service.insert_by_spider(conn, data)

    pass


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
        threading.Thread(target=get_id_queue, args=(id_queue, start_id,)).start()

        subject_dto_queue = Queue(maxsize=30)
        subject_message_queue = Queue(maxsize=30)
        subject_profession_person_queue = Queue()

        for i in range(0, 3):
            Process(target=get_dto_soup_queue,
                    args=(subject_dto_queue, subject_message_queue, id_queue,
                          subject_profession_person_queue, category_professions, 4,)).start()

        while True:
            if subject_dto_queue.empty():
                continue
            subject_dto = subject_dto_queue.get()
            print(common_util.object_to_json(subject_dto))
            # if subject_message_queue.empty():
            #     continue
            # subject_message = subject_message_queue.get()
            # print(subject_message)


        # subject_data_queue = Queue()
        # subject_soup_queue = Queue()

        # start_id = 1

        # threading.Thread(target=get_subject_soup_id, args=(subject_soup_queue, start_id)).start()
        #
        # for i in range(0,4):
        #     threading.Thread(target=get_subject_data, args=(subject_soup_queue, subject_data_queue)).start()
        #
        # threading.Thread(target=write_db, args=(subject_data_queue)).start()
    except Exception:
        print(traceback.format_exc())