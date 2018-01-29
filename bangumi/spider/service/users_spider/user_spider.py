# *_*coding:utf-8 *_*
# author: hoicai

from bangumi.client.mysql_client import get_connect
from bangumi.constants.table_constants import USER_INFO_STATUS_DOING
from bangumi.spider.dao.user_info_dao import *
from bangumi.spider.service.spider_version.spider_version import get_spider_version
from bangumi.utils.MyException import MyException

if __name__ == "__main__":

    try:
        conn = get_connect()

        spider_version_data = get_spider_version(conn, 'user_info', USER_INFO_STATUS_DOING)

        if spider_version_data == None or spider_version_data == "":
            raise MyException("select spider_version_data is none ")

        sql_find_by_spider_version = "spider_version != '{}' and status == '{}' and active_degree >= '{}'"\
            .format(spider_version_data[0]['spider_version'], 'ENABLE', spider_version_data[0]['active_degree'])
        data = user_info_select(conn, sql_find_by_spider_version)
        print(data)


    except Exception as e:
        print(e)
    finally:
        conn.close()
