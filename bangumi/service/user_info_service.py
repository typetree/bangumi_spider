# *_*coding:utf-8 *_*
# author: hoicai
import traceback

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


def spider_update(conn, uid: user_info_dto.UserInfoDTO, uid_update:user_info_dto.UserInfoDTO):
    flag = False
    
    uid.name = uid_update.name
    uid.profile_photo = uid_update.profile_photo
    uid.bangumi_user_id = uid_update.bangumi_user_id
    uid.join_time = uid_update.join_time
    uid.intro = uid_update.intro
    uid.anime_do = uid_update.anime_do
    uid.anime_collect = uid_update.anime_collect
    uid.anime_wish = uid_update.anime_wish
    uid.anime_on_hold = uid_update.anime_on_hold
    uid.anime_dropped = uid_update.anime_dropped

    uid.game_do = uid_update.game_do
    uid.game_collect = uid_update.anime_collect
    uid.game_wish = uid_update.game_wish
    uid.game_on_hold = uid_update.game_on_hold
    uid.game_dropped = uid_update.game_dropped
    
    uid.book_do = uid_update.book_do
    uid.book_collect = uid_update.anime_collect
    uid.book_wish = uid_update.book_wish
    uid.book_on_hold = uid_update.book_on_hold
    uid.book_dropped = uid_update.book_dropped
    
    uid.real_do = uid_update.real_do
    uid.real_collect = uid_update.anime_collect
    uid.real_wish = uid_update.real_wish
    uid.real_on_hold = uid_update.real_on_hold
    uid.real_dropped = uid_update.real_dropped


    uid.update_time = common_util.get_now_time()
    while not flag:
        try:
            flag = user_info_dao.user_info_update(conn, uid)
        except Exception:
            print(traceback.format_exc())


def reduce_active_degree(conn, uid: user_info_dto.UserInfoDTO):
    flag = False
    if uid.active_degree > 0:
        uid.active_degree = uid.active_degree - 1
    while not flag:
        try:
            flag = user_info_dao.user_info_update(conn, uid)
        except Exception:
            print(traceback.format_exc())