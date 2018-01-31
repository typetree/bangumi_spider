# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants.table_constants import ENABLE
from bangumi.constants.url_constants import USER_INDEX
from bangumi.dao.user_info_dao import *
from bangumi.dto.SpiderVersionDTO import SpiderVersionDTO
from bangumi.dto.UserInfoDTO import UserInfoDTO
from bangumi.utils.common_util import get_now_time


class UserInfoService:
    def find_by_spider_version(self, conn, svd: SpiderVersionDTO ,limitNum =10):
        sql_find_by_spider_version = "spider_version != '{}' and status = '{}' and active_degree >= '{}' LIMIT 0,{}" \
            .format(svd.spider_version, 'ENABLE', str(svd.active_degree), limitNum)
        uids = user_info_select(conn, sql_find_by_spider_version)
        return uids

    def find_by_code(self, conn, code):
        sql_find_by_code = "code = '{}' and status = '{}'".format(code, ENABLE)
        uids = user_info_select(conn, sql_find_by_code)
        return uids

    def create(self, conn, uid: UserInfoDTO):
        flag = False
        uid.optimistic = 0
        uid.homepage = USER_INDEX+uid.code
        uid.status = ENABLE
        uid.spider_version = '0'
        uid.active_degree = 100
        uid.update_time = get_now_time()
        uid.create_time = get_now_time()
        while not flag:
            flag = user_info_insert(conn, uid)

    def update_spider_version(self, conn, uid: UserInfoDTO, svd: SpiderVersionDTO):
        flag = False

        uid.spider_version = svd.spider_version
        while not flag:
            flag = user_info_update(conn, uid)