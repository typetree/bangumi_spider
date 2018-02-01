# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants.table_constants import UNABLE
from bangumi.utils import common_util
from ..dao import user_spider_version_dao
from ..dto import user_spider_version_dto


def find_by_user_info_version(conn, svd: user_spider_version_dto.SpiderVersionDTO, limitNum=10):
    sql_find_by_user_info_version = "user_info_version != '{}' and active_degree >= '{}' LIMIT 0,{}" \
        .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
    uids = user_spider_version_dao.user_spider_version_select(conn, sql_find_by_user_info_version)
    return uids


def unable_user_info_version(conn, usvDto: user_spider_version_dto.UserSpiderVersionDTO, user_info_version, log):
    flag = False

    usvDto.user_info_version = user_info_version
    usvDto.log = log
    usvDto.status = UNABLE
    usvDto.update_time = common_util.get_now_time()

    while not flag:
        flag = user_spider_version_dao.user_spider_version_update(conn, usvDto)
