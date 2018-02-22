# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from bangumi.dto import user_spider_version_dto
from bangumi.factory import strategy_factory
from ..client import mysql_client
from ..constants import table_constants
from ..service import spider_version_service
from ..utils import common_util
from ..utils.my_exception import MyException


def spider_version_threading(CATEGORY, TABLE_NAME, TARGET_METHOD, UPDATE_METHOD):
    try:
        conn = mysql_client.get_connect()

        spider_version_data = spider_version_service.get_spider_version(
            conn, TABLE_NAME, table_constants.SPIDER_VERSION_STATUS_DOING)
        conn.close()

        svd = spider_version_data[0]
        spider_do(CATEGORY, TABLE_NAME, svd, TARGET_METHOD, UPDATE_METHOD)
    except MyException as e:
        print(e.message)
    except Exception:
        print(traceback.format_exc())
        conn.close()


def spider_do(CATEGORY, TABLE_NAME, svd, TARGET_METHOD, UPDATE_METHOD):
    try:
        conn = mysql_client.get_connect()

        FLAG = True
        while FLAG:
            # 从用户表中取出非该时间戳,且活跃度大于等于需求的用户信息
            category_spider_version_dtos = strategy_factory.find_category_spider_version_method(CATEGORY)(conn,TABLE_NAME, svd, 10)

            # 如果找不到，更新爬虫版本状态为完成，结束循环
            if category_spider_version_dtos is None or len(category_spider_version_dtos) == 0:
                spider_version_service.finish_spider_version(conn, svd)
                FLAG = False

            thread_list = []
            for csvDto in category_spider_version_dtos:
                t = threading.Thread(
                    target=threading_process,
                    args=(CATEGORY, TARGET_METHOD, UPDATE_METHOD, TABLE_NAME, csvDto, svd.spider_version,))
                thread_list.append(t)

            for t in thread_list:
                t.start()
            for t in thread_list:
                t.join()

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


def threading_process(CATEGORY, TARGET_METHOD, UPDATE_METHOD, TABLE_NAME, csvDto, spider_version):
    try:
        conn = mysql_client.get_connect()
        csvd = strategy_factory.proxy_target_method(CATEGORY, TARGET_METHOD, UPDATE_METHOD,
                                                    conn, TABLE_NAME, csvDto, spider_version)

        strategy_factory.update_category_spider_version_method(CATEGORY)(conn, csvd)
    except MyException as e:
        strategy_factory.unable_category_spider_version_method(CATEGORY)(conn, TABLE_NAME, csvDto, spider_version, e.message)
    except Exception:
        log = traceback.format_exc()
        print(log)
        strategy_factory.unable_category_spider_version_method(CATEGORY)(conn, TABLE_NAME, csvDto, spider_version, log)
    finally:
        conn.close()


def fingerprint_compare(old_fingerprint, update_value):
    update_fingerprint = common_util.hashlib_md5([update_value])
    if old_fingerprint != update_fingerprint:
        return update_fingerprint
    else:
        return None


def compare_and_update(usvd: user_spider_version_dto.UserSpiderVersionDTO, TABLE_NAME, svd,
                       conn, dto, update_data, UPDATE_METHOD):

    columns = strategy_factory.spider_version_column_get(usvd, TABLE_NAME)

    fingerprint = columns['fingerprint']
    active_degree = columns['active_degree']

    update_fingerprint = fingerprint_compare(fingerprint, update_data)

    if update_fingerprint is not None:

        UPDATE_METHOD(conn, dto, update_data)
        active_degree = active_degree + 1
        fingerprint = update_fingerprint
    elif active_degree > 0:

        active_degree = active_degree - 1

    columns_set = {
        "version": svd,
        "fingerprint": fingerprint,
        "active_degree": active_degree
    }

    usvd = strategy_factory.spider_version_column_set(usvd, columns_set, TABLE_NAME)
    return usvd