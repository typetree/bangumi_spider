# *_*coding:utf-8 *_*
# author: hoicai

import MySQLdb
import time

from bangumi.constants.db_constants import *


def get_connect():
    conn = MySQLdb.connect(
        host=HOST,
        user=USER, passwd=PASSWORD,
        db=DB, charset=CHARSET)

    return conn


def execute_sql(conn, sql, params):
    cursor = conn.cursor()

    flag = True
    retry_num = 5
    while flag:
        if retry_num <= 0:
            return False
        try:
            cursor.execute(sql, params)
            conn.commit()

            # print("操作成功,sql:{},params:{}", sql, params)
            flag = False
        except Exception as e:
            print("操作出错，重试中...sql:{},params:{},e:{}", sql, params, e)
            retry_num -= 1
            time.sleep(1)

    return True


def execute_select_sql(conn, sql):
    cursor = conn.cursor()

    flag = True
    retry_num = 5

    while flag:
        if retry_num <= 0:
            return False
        try:
            cursor.execute(sql)
            conn.commit()

            # print("操作成功,sql:{},params:{}", sql)
            flag = False
        except Exception as e:
            print("操作出错，重试中...sql:{},params:{},e:{}", sql, e)
            retry_num -= 1
            time.sleep(1)

    return cursor.fetchall()
