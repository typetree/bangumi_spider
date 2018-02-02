# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from bangumi.client import mysql_client
from bangumi.constants import table_constants
from bangumi.dto import user_info_dto, user_spider_version_dto
from bangumi.service import spider_version_service, user_info_service, user_spider_version_service
from bangumi.spider import user_info_spider
from bangumi.utils import common_util


def update_user_info(conn, uid: user_info_dto.UserInfoDTO,
                     usvd: user_spider_version_dto.UserSpiderVersionDTO, svd):
    uid_update = user_info_spider.get_user_info(uid.code)
    user_info_fingerprint = common_util.hashlib_md5([uid_update])

    active_degree = usvd.user_info_active_degree
    if usvd.user_info_fingerprint != user_info_fingerprint:
        print("{}:{} update".format(uid.code, uid_update.name))
        user_info_service.spider_update(conn, uid, uid_update)
        active_degree = uid.active_degree + 1
    elif uid.active_degree > 0:
        active_degree = uid.active_degree - 1

    usvd.user_info_version = svd
    usvd.user_info_fingerprint = active_degree
    usvd.bangumi_user_id = uid_update.bangumi_user_id
    print("{}:{} finish, version:{}".format(uid.code, uid_update.name, svd))
    user_spider_version_service.update_version(conn, usvd)


def all_user_info(svd):
    try:
        conn = mysql_client.get_connect()
        FLAG = True
        while FLAG:
            # 从用户表中取出非该时间戳,且活跃度大于等于需求的用户信息
            user_spider_version_dtos = user_spider_version_service.find_by_user_info_version(conn, svd, 10)

            # 如果找不到，更新爬虫版本状态为完成，结束循环
            if user_spider_version_dtos is None or len(user_spider_version_dtos) == 0:
                spider_version_service.finish_spider_version(conn, svd)
                FLAG = False

            for usvDto in user_spider_version_dtos:
                uids = user_info_service.find_by_code(conn, usvDto.user_code)
                if uids is None or len(uids)==0:
                    log = "version:{}, user:{} is not existed in user_info".format(svd.spider_version, usvDto.user_code)
                    print(log)
                    user_spider_version_service.unable_user_info_version(conn, usvDto, svd.spider_version, log)
                    continue
                elif len(uids) > 1:
                    log = "version:{}, user:{} is more than 1 in user_info".format(svd.spider_version, usvDto.user_code)
                    print(log)
                    user_spider_version_service.unable_user_info_version(conn, usvDto, svd.spider_version, log)
                    continue

                update_user_info(conn, uids[0], usvDto, svd.spider_version)

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == "__main__":

    try:
        conn = mysql_client.get_connect()

        spider_version_data = spider_version_service.get_spider_version(
            conn, 'user_info', table_constants.SPIDER_VERSION_STATUS_DOING)
        conn.close()

        svd = spider_version_data[0]

        threading.Thread(target=all_user_info, args=(svd,)).start()

    except Exception:
        print(traceback.format_exc())
        conn.close()
    # finally:
