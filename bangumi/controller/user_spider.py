# *_*coding:utf-8 *_*
# author: hoicai
import threading

from bangumi.client.mysql_client import get_connect
from bangumi.constants.table_constants import SPIDER_VERSION_STATUS_DOING
from bangumi.service.spider_version.spider_version import SpiderVersionService
from bangumi.service.user_info.user_info import UserInfoService
from bangumi.spider.users_spider.user_friends import find_friends


def all_user_spider(svd):
    try:
        conn = get_connect()
        FLAG = True
        while FLAG:
            # 从用户表中取出非该时间戳,且活跃度大于等于需求的用户信息
            uids = userInfoService.find_by_spider_version(conn, svd, 10)

            # 如果找不到，更新爬虫版本状态为完成，结束循环
            if uids is None or len(uids) == 0:
                spiderVersionService.finish_spider_version(conn, svd)
                FLAG = False

            for uid in uids:
                print("find users' friends, uid:{}".format(uid.code))
                # 查找好友页面，获取好友用户信
                friends = find_friends(uid.code)
                for friend in friends:
                    ones = userInfoService.find_by_code(conn, friend.code)
                    if ones is None or len(ones) == 0:
                        print("insert user,user_code:{}".format(friend.code))
                        userInfoService.create(conn, friend)
                userInfoService.update_spider_version(conn, uid, svd)
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":

    try:
        conn = get_connect()
        userInfoService = UserInfoService();
        spiderVersionService = SpiderVersionService();

        spider_version_data = spiderVersionService.get_spider_version(conn, 'user_info',
                                                                      SPIDER_VERSION_STATUS_DOING)
        conn.close()

        svd = spider_version_data[0]

        threading.Thread(target=all_user_spider, args=(svd,)).start()

    except Exception as e:
        conn.close()
        print(e)

