# *_*coding:utf-8 *_*
# author: hoicai
import threading
from queue import Queue

from multiprocessing import Process

from bangumi.client import mysql_client
from bangumi.dto import subject_info_dto
from bangumi.service import subject_info_service
from bangumi.spider import subject_info_spider


global id_flag


def get_id_queue(id_queue:Queue, start_id):

    id_flag = True
    while id_flag:
        if id_queue.full():
            continue
        id_queue.put(start_id)
        start_id += 1


def get_message_soup_queue(subject_soup_queue, subject_message_queue, id_queue, max_thread_num=4):
    for i in range(0, max_thread_num):
        threading.Thread(target=get_message_queue,
                         args=(subject_soup_queue, subject_message_queue, id_queue,)).start()


def get_message_queue(subject_soup_queue:Queue, subject_message_queue:Queue, id_queue:Queue):
    while True:
        if id_queue.empty() or subject_message_queue.full():
            continue
        start_id = id_queue.get()
        soup = subject_info_spider.get_subject_soup(start_id)
        data = subject_info_spider.get_message_by_soup(soup)
        if data is None:
            start_id += 1
            continue
        subject_soup_queue.put(soup)
        subject_message_queue.put(data)
        start_id += 1


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

    conn = mysql_client.get_connect()
    start_id = subject_info_service.find_max_bangumi_id(conn)
    conn.close()

    id_queue = Queue(maxsize=30)
    threading.Thread(target=get_id_queue, args=(id_queue, start_id,)).start()

    subject_soup_queue = Queue(maxsize=30)
    subject_message_queue = Queue(maxsize=30)

    for i in range(0, 3):
        Process(target=get_message_soup_queue,
                args=(subject_soup_queue, subject_message_queue, id_queue, 4))




    # subject_data_queue = Queue()
    # subject_soup_queue = Queue()

    # start_id = 1

    # threading.Thread(target=get_subject_soup_id, args=(subject_soup_queue, start_id)).start()
    #
    # for i in range(0,4):
    #     threading.Thread(target=get_subject_data, args=(subject_soup_queue, subject_data_queue)).start()
    #
    # threading.Thread(target=write_db, args=(subject_data_queue)).start()