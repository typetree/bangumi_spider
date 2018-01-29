# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants.table_constants import USER_INFO_STATUS_DOING
from bangumi.spider.dao.spider_version_dao import *
from bangumi.client.mysql_client import get_connect
from bangumi.utils.common_util import get_now_time


def get_spider_version(conn, version, status):

    where_sql = "version = '{}' and status = '{}'".format(version, status)
    spider_version_data = spider_version_select(conn, where_sql)
    return spider_version_data


if __name__ == "__main__":

    table_name = 'user_info'

    conn = get_connect()

    time = get_now_time()

    active_degree = 100

    data = {
        'optimistic': 0,
        'version': table_name,
        'spider_version': time+"_"+table_name+"_"+str(active_degree),
        'active_degree': 50,
        'log': '',
        'status': USER_INFO_STATUS_DOING,
        "create_time": time,
        "update_time": time
    }

    spider_version_insert(conn, data)

    conn.close()