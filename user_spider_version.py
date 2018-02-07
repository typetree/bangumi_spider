# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from bangumi.client import mysql_client
from bangumi.service import user_info_service
from bangumi.spider import user_info_spider
from bangumi.utils import my_exception


def update_bangumi(bangumi_id):
    try:
        print("find start, bangumi_id:{}".format(bangumi_id))
        conn = mysql_client.get_connect()
        update_data = user_info_spider.get_user_info(str(bangumi_id))
        user_info_dto = user_info_service.find_by_code(conn, update_data.code)
        if user_info_dto.bangumi_user_id != bangumi_id:
            user_info_dto.bangumi_user_id = bangumi_id
            user_info_service.update_spider_version(conn, user_info_dto)
    except my_exception.MyException as e:
        if e.message.find("not existed"):
            user_info_service.create(conn, update_data)
        if e.message.find("spider user homepage is fail"):
            print("find end, bangumi_id:{}".format(bangumi_id))
    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()
        print("find end, bangumi_id:{}".format(bangumi_id))


if __name__ == "__main__":

    bangumi_id = 1
    target = bangumi_id + 10

    thread_list = []
    while True:
        t = threading.Thread(target=update_bangumi, args=(bangumi_id,))
        thread_list.append(t)
        bangumi_id += 1

        if bangumi_id == target:
            for t in thread_list:
                t.start()
            for t in thread_list:
                t.join()
            target = bangumi_id + 10
            thread_list = []
