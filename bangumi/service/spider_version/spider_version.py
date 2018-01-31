# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.client.mysql_client import get_connect
from bangumi.constants.table_constants import *
from bangumi.dao.spider_version_dao import spider_version_update, spider_version_select, \
    spider_version_insert
from bangumi.dto.SpiderVersionDTO import SpiderVersionDTO
from bangumi.utils.MyException import MyException
from bangumi.utils.common_util import get_now_time


class SpiderVersionService:
    def get_spider_version(self, conn, version, status):
        where_sql = "version = '{}' and status = '{}'".format(version, status)
        spider_version_data = spider_version_select(conn, where_sql)

        if spider_version_data == None or len(spider_version_data) == 0:
            raise MyException("select spider_version_data is none ")

        return spider_version_data

    def finish_spider_version(self, conn, svd: SpiderVersionDTO):
        flag = False
        svd.status = SPIDER_VERSION_STATUS_FINISH
        svd.update_time = get_now_time()
        while not flag:
            flag = spider_version_update(conn, svd)


if __name__ == "__main__":
    table_name = 'user_info'

    conn = get_connect()

    time = get_now_time()

    active_degree = 100

    data = {
        'optimistic': 0,
        'version': table_name,
        'spider_version': time + "_" + table_name + "_" + str(active_degree),
        'active_degree': 50,
        'log': '',
        'status': SPIDER_VERSION_STATUS_DOING,
        "create_time": time,
        "update_time": time
    }

    spider_version_insert(conn, data)

    conn.close()
