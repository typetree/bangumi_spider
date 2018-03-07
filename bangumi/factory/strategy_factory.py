# *_*coding:utf-8 *_*
# author: hoicai
from ..dto import user_spider_version_dto
from ..service import user_spider_version_service, user_info_service, user_friends_service
from ..constants import table_constants
from ..utils import my_exception, base_util

'''
根据分类，查找对应的爬虫版本控制
'''
def find_category_spider_version_method(CATEGORY):
    if CATEGORY == table_constants.CATEGORY_USER:
        return user_spider_version_service.find_version

    else:
        raise my_exception.MyException("find_category_spider_version_method no found")


'''
根据分类，更新对应的爬虫版本控制
'''
def update_category_spider_version_method(CATEGORY):
    if CATEGORY == table_constants.CATEGORY_USER:
        return user_spider_version_service.update_version

    else:
        raise my_exception.MyException("update_category_spider_version_method no found")


'''
根据分类，失效对应的爬虫版本控制
'''
def unable_category_spider_version_method(CATEGORY):

    if CATEGORY == table_constants.CATEGORY_USER:
        return user_spider_version_service.unable_version

    else:
        raise my_exception.MyException("user_spider_version_unable_factory no found")


'''
根据分类，目标方法，代理增强爬虫功能
'''
def proxy_target_method(CATEGORY, TARGET_METHOD, UPDATE_METHOD,
                        conn, TABLE_NAME, usvd: user_spider_version_dto.UserSpiderVersionDTO, svd):

    if CATEGORY == table_constants.CATEGORY_USER:
        uid = user_info_service.find_by_bangumi_id(conn, usvd.bangumi_user_id)
        print("{}:{} update user_info".format(uid.code, uid.name))

        update_data = TARGET_METHOD(uid)

        usvd = base_util.compare_and_update(usvd, TABLE_NAME, svd, conn, uid, update_data, UPDATE_METHOD)

        print("{}:{} update {} finish, version:{}".format(uid.code, uid.name, TABLE_NAME, svd))
        return usvd
    else:
        raise my_exception.MyException("proxy_target_method no found")


'''
获取用户类目下，不同表的爬虫版本信息
'''
def spider_version_column_get(usvd: user_spider_version_dto.UserSpiderVersionDTO, TABLE_NAME):

    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        columns = {
            "version": usvd.user_info_version,
            "fingerprint": usvd.user_info_fingerprint,
            "active_degree": usvd.user_info_active_degree
        }
        return columns
    elif TABLE_NAME == table_constants.TABLE_USER_FRIENDS:
        columns = {
            "version": usvd.user_friends_version,
            "fingerprint": usvd.user_friends_fingerprint,
            "active_degree": usvd.user_friends_active_degree
        }
        return columns
    else:
        raise my_exception.MyException("user_spider_version_column_get no found")


'''
设置用户类目下，不同表的爬虫版本信息
'''
def spider_version_column_set(usvd: user_spider_version_dto.UserSpiderVersionDTO, columns, TABLE_NAME):
    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        usvd.user_info_version = columns['version'] if columns['version'] != "" else usvd.user_info_version
        usvd.user_info_fingerprint = columns['fingerprint'] if columns['fingerprint'] != "" else usvd.user_info_fingerprint
        usvd.user_info_active_degree = columns['active_degree'] if columns['active_degree'] != "" else usvd.user_info_active_degree
        return usvd
    elif TABLE_NAME == table_constants.TABLE_USER_FRIENDS:
        usvd.user_friends_version = columns['version'] if columns['version'] != "" else usvd.user_friends_version
        usvd.user_friends_fingerprint = columns['fingerprint'] if columns['fingerprint'] != "" else usvd.user_friends_fingerprint
        usvd.user_friends_active_degree = columns['active_degree'] if columns['active_degree'] != "" else usvd.user_friends_active_degree
        return usvd
    else:
        raise my_exception.MyException("user_spider_version_column_set no found")


'''
根据表名，获取表的更新方法
def spider_update_method(TABLE_NAME):
    if TABLE_NAME == table_constants.TABLE_USER_INFO:
        return user_info_service.spider_update

    elif TABLE_NAME == table_constants.TABLE_USER_FRIENDS:
        return user_friends_service.spider_update

    else:
        raise my_exception.MyException("spider_update_method no found")
'''

