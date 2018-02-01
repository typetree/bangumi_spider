# *_*coding:utf-8 *_*
# author: hoicai
import threading
import traceback

from bangumi.client import mysql_client
from bangumi.constants import table_constants
from bangumi.dto import user_info_dto
from bangumi.service import spider_version_service, user_info_service
from bangumi.spider import user_info_spider
from bangumi.utils import common_util


def update_user_info(conn, uid: user_info_dto.UserInfoDTO):
    uid_update = user_info_spider.get_user_info(uid)
    user_info_fingerprint = common_util.hashlib_md5(uid_update)
    if uid.hash_value != user_info_fingerprint:

    print(uid)

def all_user_info(svd):
    try:
        conn = mysql_client.get_connect()
        FLAG = True
        while FLAG:
            # 从用户表中取出非该时间戳,且活跃度大于等于需求的用户信息
            uids = user_info_service.find_by_spider_version(conn, svd, 10)

            # 如果找不到，更新爬虫版本状态为完成，结束循环
            if uids is None or len(uids) == 0:
                spider_version_service.finish_spider_version(conn, svd)
                FLAG = False

            for uid in uids:
                update_user_info(conn, uid)
            user_info_service.update_spider_version(conn, uid, svd)

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == "__main__":

    try:
        conn = mysql_client.get_connect()

        update_user_info(conn,"zisudaki")

        spider_version_data = spider_version_service.get_spider_version(
            conn, 'user_info', table_constants.SPIDER_VERSION_STATUS_DOING)
        conn.close()

        svd = spider_version_data[0]

        threading.Thread(target=all_user_info, args=(svd,)).start()

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()
