# *_*coding:utf-8 *_*
# author: hoicai
import threading

from bangumi.service import user_info_service
from bangumi.spider import user_friends_spider
from bangumi.client import mysql_client
from bangumi.constants import table_constants
from bangumi.service import spider_version_service


def all_user_spider(svd):
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
                print("find users' friends, uid:{}".format(uid.code))
                # 查找好友页面，获取好友用户信
                friends = user_friends_spider.find_friends(uid.code)
                for friend in friends:
                    ones = user_info_service.find_by_code(conn, friend.code)
                    if ones is None or len(ones) == 0:
                        print("insert user,user_code:{}".format(friend.code))
                        user_info_service.create(conn, friend)
                user_info_service.update_spider_version(conn, uid, svd)
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":

    try:
        conn = mysql_client.get_connect()

        spider_version_data = spider_version_service.get_spider_version(
            conn, 'user_info', table_constants.SPIDER_VERSION_STATUS_DOING)
        conn.close()

        svd = spider_version_data[0]

        threading.Thread(target=all_user_spider, args=(svd,)).start()

    except Exception as e:
        conn.close()
        print(e)

