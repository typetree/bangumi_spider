# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from bangumi.client import mysql_client
from bangumi.service import user_info_service, user_spider_version_service
from bangumi.spider import user_info_spider
from bangumi.utils import my_exception


class user_info_add_main:

    def __init__(self):
        self._result = None


    def get_result(self):
        return self._result


    def update_bangumi(self, bangumi_id):
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
                update_data.bangumi_user_id = bangumi_id
                user_info_service.create(conn, update_data)
                user_spider_version_service.create_by_user_info_dto(conn, user_info_dto)
            if e.message.find("spider user homepage is fail"):
                print("find end, bangumi_id:{}".format(bangumi_id))
        except my_exception.BreakException as e:
            print(e.message)
            self._result = False
        except Exception:
            print(traceback.format_exc())
        finally:
            conn.close()
            print("find end, bangumi_id:{}".format(bangumi_id))


if __name__ == "__main__":

    bangumi_id = 1
    target = bangumi_id + 15

    thread_list = []
    while True:
        task = user_info_add_main()
        t = threading.Thread(target=task.update_bangumi, args=(bangumi_id,))
        thread_list.append(t)
        bangumi_id += 1

        stop_point = 0
        if bangumi_id == target:
            for t in thread_list:
                t.start()
            for t in thread_list:
                t.join()
            target = bangumi_id + 15
            thread_list = []

            if task.get_result() == False:
                stop_point += 1

        if stop_point == 15:
            break