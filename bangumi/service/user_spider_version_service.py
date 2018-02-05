# *_*coding:utf-8 *_*
# author: hoicai
import traceback

from bangumi.constants.table_constants import UNABLE
from bangumi.utils import common_util
from ..dao import user_spider_version_dao
from ..dto import user_spider_version_dto


def find_by_user_info_version(conn, svd: user_spider_version_dto.UserSpiderVersionDTO, limitNum=10):
    sql_find_by_user_info_version = "user_info_version != '{}' and status = '{}' and user_info_active_degree >= '{}' LIMIT 0,{}" \
        .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
    uids = user_spider_version_dao.user_spider_version_select(conn, sql_find_by_user_info_version)
    return uids


def unable_user_info_version(conn, usvDTO: user_spider_version_dto.UserSpiderVersionDTO, user_info_version, log):
    flag = False

    usvDTO.user_info_version = user_info_version
    usvDTO.log = log
    usvDTO.status = UNABLE
    usvDTO.update_time = common_util.get_now_time()

    while not flag:
        try:
            flag = user_spider_version_dao.user_spider_version_update(conn, usvDTO)
        except Exception:
            print(traceback.format_exc())

def find_by_user_friends_version(conn, svd: user_spider_version_dto.UserSpiderVersionDTO, limitNum=10):
    sql_find_by_user_friends_version = "user_friends_version != '{}' and status = '{}' and user_friends_active_degree >= '{}' LIMIT 0,{}" \
        .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
    uids = user_spider_version_dao.user_spider_version_select(conn, sql_find_by_user_friends_version)
    return uids


def update_version(conn, usvDTO: user_spider_version_dto.UserSpiderVersionDTO):
    flag = False

    usvDTO.update_time = common_util.get_now_time()

    while not flag:
        try:
            flag = user_spider_version_dao.user_spider_version_update(conn, usvDTO)
        except Exception:
            print(traceback.format_exc())
