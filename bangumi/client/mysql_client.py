# *_*coding:utf-8 *_*
# author: hoicai

import MySQLdb
import time

from bangumi.constants.db_constants import *
from bangumi.utils import my_exception


def get_connect():
    conn = MySQLdb.connect(
        host=HOST,
        user=USER, passwd=PASSWORD,
        db=DB, charset=CHARSET)

    return conn


def execute_sql(conn, sql, params=None):

    log = ''
    cursor = conn.cursor()

    flag = True
    retry_num = 5
    while flag:
        if retry_num <= 0:
            raise my_exception.MyException(log)
        try:
            cursor.execute(sql, params)
            id = int(conn.insert_id())
            conn.commit()

            # print("操作成功,sql:{},params:{}", sql, params)
            flag = False
        except Exception as e:
            log = "操作出错，重试中...sql:{},params:{},e:{}".format(sql, params, e)
            print(log)
            retry_num -= 1
            time.sleep(1)
    return id



def execute_select_sql(conn, sql):

    log = ''
    cursor = conn.cursor()

    flag = True
    retry_num = 5

    while flag:
        if retry_num <= 0:
            raise my_exception.MyException(log)
        try:
            cursor.execute(sql)
            conn.commit()

            # print("操作成功,sql:{},params:{}", sql)
            flag = False
        except Exception as e:
            log = "操作出错，重试中...sql:{},e:{}".format(sql, e)
            print(log)
            retry_num -= 1
            time.sleep(1)

    return cursor.fetchall()


