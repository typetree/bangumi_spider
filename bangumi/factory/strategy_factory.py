# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.dto import user_spider_version_dto
from bangumi.service import user_spider_version_service, user_info_service
from bangumi.constants import table_constants
from bangumi.utils import my_exception


def spider_version_unable_factory(TABLE_NAME):

    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        return user_spider_version_service.unable_user_info_version
    else:
        raise my_exception.MyException("user_spider_version_unable_factory no found")


def spider_version_column_get(usvd: user_spider_version_dto.UserSpiderVersionDTO, TABLE_NAME):

    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        columns = {
            "version": usvd.user_info_version,
            "fingerprint": usvd.user_info_fingerprint,
            "active_degree": usvd.user_info_active_degree
        }
        return columns
    else:
        raise my_exception.MyException("user_spider_version_column_get no found")


def spider_version_column_set(usvd: user_spider_version_dto.UserSpiderVersionDTO, columns, TABLE_NAME):
    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        usvd.user_info_version = columns['version']
        usvd.user_info_fingerprint = columns['fingerprint']
        usvd.user_info_active_degree = columns['active_degree']
        return usvd
    else:
        raise my_exception.MyException("user_spider_version_column_set no found")


def spider_update_method(TABLE_NAME):
    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        return user_info_service.spider_update
    else:
        raise my_exception.MyException("spider_update_method no found")


def find_category_spider_version_method(TABLE_NAME):
    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        return user_spider_version_service.find_by_user_info_version
    else:
        raise my_exception.MyException("find_category_spider_version_method no found")


def update_category_spider_version_method(TABLE_NAME):
    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        return user_spider_version_service.update_version
    else:
        raise my_exception.MyException("update_category_spider_version_method no found")