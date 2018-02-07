# *_*coding:utf-8 *_*
# author: hoicai

from bangumi.dto import user_spider_version_dto, user_info_dto
from bangumi.service import user_spider_version_service, user_friends_service, user_info_service
from bangumi.spider import user_friends_spider
from bangumi.constants import table_constants
from bangumi.utils import common_util, base_util



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


def update_user_frinds(conn, TABLE_NAME, usvd: user_spider_version_dto.UserSpiderVersionDTO, svd):

    uid = user_info_service.find_by_code(conn, usvd.user_code)
    print("{}:{} update {} user_info".format(uid.code, uid.name, TABLE_NAME))

    update_data = user_info_spider.get_user_info(uid.code)

    usvd = base_util.compare_and_update(usvd, TABLE_NAME, svd, conn, uid, update_data)

    print("{}:{} update {} finish, version:{}".format(uid.code, update_data.name, TABLE_NAME, svd))
    return usvd


if __name__ == "__main__":

    base_util.spider_version_threading(
        table_constants.CATEGORY_USER, table_constants.TABLE_USER_FRIENDS, update_user_frinds)

