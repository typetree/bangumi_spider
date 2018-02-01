# *_*coding:utf-8 *_*
# author: hoicai
from ..constants import table_constants
from ..constants import url_constants
from ..dao import user_info_dao
from ..dto import spider_version_dto
from ..dto import user_info_dto
from ..utils import common_util


def find_by_spider_version(conn, svd: spider_version_dto.SpiderVersionDTO, limitNum=10):
    sql_find_by_spider_version = "spider_version != '{}' and status = '{}' and active_degree >= '{}' LIMIT 0,{}" \
        .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
    uids = user_info_dao.user_info_select(conn, sql_find_by_spider_version)
    return uids


def find_by_code(conn, code):
    sql_find_by_code = "code = '{}' and status = '{}'".format(code, table_constants.ENABLE)
    uids = user_info_dao.user_info_select(conn, sql_find_by_code)
    return uids


def create(conn, uid: user_info_dto.UserInfoDTO):
    flag = False
    uid.optimistic = 0
    uid.homepage = url_constants.USER_INDEX + uid.code
    uid.status = table_constants.ENABLE
    uid.spider_version = '0'
    uid.active_degree = 100
    uid.update_time = common_util.get_now_time()
    uid.create_time = common_util.get_now_time()
    while not flag:
        flag = user_info_dao.user_info_insert(conn, uid)


def update_spider_version(conn, uid: user_info_dto.UserInfoDTO, svd: spider_version_dto.SpiderVersionDTO):
    flag = False

    uid.spider_version = svd.spider_version
    while not flag:
        flag = user_info_dao.user_info_update(conn, uid)


