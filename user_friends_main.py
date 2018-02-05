# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from bangumi.dto import user_spider_version_dto, user_info_dto
from bangumi.service import user_info_service, user_spider_version_service, user_friends_service
from bangumi.spider import user_friends_spider
from bangumi.client import mysql_client
from bangumi.constants import table_constants
from bangumi.service import spider_version_service
from bangumi.utils import common_util
from bangumi.utils.my_exception import MyException


def all_friends_spider(svd):
    try:
        conn = mysql_client.get_connect()
        FLAG = True
        while FLAG:
            # 从用户表中取出非该时间戳,且活跃度大于等于需求的用户信息
            user_spider_version_dtos = user_spider_version_service.find_by_user_friends_version(conn, svd, 10)

            # 如果找不到，更新爬虫版本状态为完成，结束循环
            if user_spider_version_dtos is None or len(user_spider_version_dtos) == 0:
                spider_version_service.finish_spider_version(conn, svd)
                FLAG = False

            for usvDto in user_spider_version_dtos:
                try:
                    uid = user_info_service.find_by_code(conn, usvDto.user_code)
                    update_user_frinds(conn, uid, usvDto, svd.spider_version)
                except MyException as e:
                    log = e
                    user_spider_version_service.unable_user_friends_version(conn, usvDto, svd.spider_version, log)
                except Exception:
                    print(traceback.format_exc())
    except Exception as e:
        print(traceback.format_exc())
    finally:
        conn.close()


def update_user_frinds(conn, uid: user_info_dto.UserInfoDTO,
                       usvd: user_spider_version_dto.UserSpiderVersionDTO, svd):
    print("find users' friends, uid:{}".format(uid.code))
    # 查找好友页面，获取好友用户信
    friends_update = user_friends_spider.find_friends(uid.code)
    user_friends_fingerprint = common_util.hashlib_md5(friends_update)
    active_degree = usvd.user_friends_active_degree
    if usvd.user_friends_fingerprint != user_friends_fingerprint:
        print("{}:{} friends update start".format(uid.code, uid.name))
        user_friends_service.spider_update(conn, uid, friends_update)
        usvd.user_friends_fingerprint = user_friends_fingerprint
        active_degree = uid.active_degree + 1
    elif uid.active_degree > 0:
        active_degree = uid.active_degree - 1

    usvd.user_friends_version = svd
    usvd.user_friends_active_degree = active_degree
    print("{}:{} friends update finish, version:{}".format(uid.code, uid.name, svd))
    user_spider_version_service.update_version(conn, usvd)


if __name__ == "__main__":

    try:
        conn = mysql_client.get_connect()

        spider_version_data = spider_version_service.get_spider_version(
            conn, table_constants.TABLE_USER_FRIENDS, table_constants.SPIDER_VERSION_STATUS_DOING)
        conn.close()

        svd = spider_version_data[0]

        threading.Thread(target=all_friends_spider, args=(svd,)).start()

    except Exception as e:
        print(traceback.format_exc())
        conn.close()

