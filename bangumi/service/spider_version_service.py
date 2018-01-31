# *_*coding:utf-8 *_*
# author: hoicai
from ..client import mysql_client
from ..constants import table_constants
from ..dao import spider_version_dao

from ..dto import spider_version_dto
from ..utils import my_exception
from ..utils import common_util


def get_spider_version(conn, version, status):
    where_sql = "version = '{}' and status = '{}'".format(version, status)
    spider_version_data = spider_version_dao.spider_version_select(conn, where_sql)

    if spider_version_data == None or len(spider_version_data) == 0:
        raise my_exception.MyException("select spider_version_data is none ")

    return spider_version_data


def finish_spider_version(conn, svd: spider_version_dto.SpiderVersionDTO):
    flag = False
    svd.status = table_constants.SPIDER_VERSION_STATUS_FINISH
    svd.update_time = common_util.get_now_time()
    while not flag:
        flag = spider_version_dao.spider_version_update(conn, svd)


if __name__ == "__main__":
    table_name = 'user_info'

    conn = mysql_client.get_connect()

    time = common_util.get_now_time()

    active_degree = 100

    data = {
        'optimistic': 0,
        'version': table_name,
        'spider_version': time + "_" + table_name + "_" + str(active_degree),
        'active_degree': 50,
        'log': '',
        'status': table_constants.SPIDER_VERSION_STATUS_DOING,
        "create_time": time,
        "update_time": time
    }

    spider_version_dao.spider_version_insert(conn, data)

    conn.close()
