# *_*coding:utf-8 *_*
# author: hoicai

from bangumi.constants.table_constants import UNABLE
from bangumi.factory import strategy_factory
from bangumi.utils import common_util
from ..dao import user_spider_version_dao
from ..dto import user_spider_version_dto


def find_version(conn, svd: user_spider_version_dto.UserSpiderVersionDTO, limitNum=10):
    sql = "user_info_version != '{}' and status = '{}' and user_info_active_degree >= '{}' LIMIT 0,{}" \
        .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
    uids = user_spider_version_dao.user_spider_version_select(conn, sql)
    return uids


def find_by_user_friends_version(conn, svd: user_spider_version_dto.UserSpiderVersionDTO, limitNum=10):
    sql = "user_friends_version != '{}' and status = '{}' and user_friends_active_degree >= '{}' LIMIT 0,{}" \
        .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
    uids = user_spider_version_dao.user_spider_version_select(conn, sql)
    return uids


def unable_version(conn, TABLE_NAME, usvDTO: user_spider_version_dto.UserSpiderVersionDTO, version, log):

    columns_set = {
        "version": version,
        "fingerprint": "",
        "active_degree": ""
    }
    usvDTO = strategy_factory.spider_version_column_set(usvDTO, columns_set, TABLE_NAME)

    usvDTO.log = log
    usvDTO.status = UNABLE
    usvDTO.update_time = common_util.get_now_time()

    user_spider_version_dao.user_spider_version_update(conn, usvDTO)



def update_version(conn, usvDTO: user_spider_version_dto.UserSpiderVersionDTO):

    usvDTO.update_time = common_util.get_now_time()

    user_spider_version_dao.user_spider_version_update(conn, usvDTO)

