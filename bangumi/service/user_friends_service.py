# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants.table_constants import ENABLE
from bangumi.dao import user_friends_dao
from bangumi.dto import user_friends_dto, user_info_dto
from bangumi.service import user_info_service
from bangumi.utils import common_util, my_exception


def find_friends_by_user_id(conn, user_id):
    sql = "user_id = '{}' and status = '{}' ".format(user_id, ENABLE)
    user_friends_dtos = user_friends_dao.user_friends_select(conn, sql)
    return user_friends_dtos


def create_by_user_and_friend(conn, uid: user_info_dto.UserInfoDTO, friend: user_info_dto.UserInfoDTO):
    print("create_friends user:{} friend:{}".format(uid.code, friend.code))
    ufd = user_friends_dto.UserFriendsDTO()
    ufd.optimistic = 0
    ufd.user_id = uid.id
    ufd.user_code = uid.code
    ufd.user_name = uid.name
    ufd.friend_user_id = friend.id
    ufd.friend_user_code = friend.code
    ufd.friend_user_name = friend.name
    ufd.status = ENABLE
    ufd.create_time = common_util.get_now_time()
    ufd.update_time = common_util.get_now_time()
    user_friends_dao.user_friends_insert(conn, ufd)


def unable_by_ids(conn, friend_user_ids):
    ids = ",".join(friend_user_ids)
    time = common_util.get_now_time()
    user_friends_dao.unable_by_ids(conn, time, ids)


def spider_update(conn, uid: user_info_dto.UserInfoDTO, friends_update: user_info_dto.UserInfoDTO):

    # 找到已有的好友
    user_friends_dtos = find_friends_by_user_id(conn, uid.id)
    map = dict([(user_friends_dto.friend_user_code, user_friends_dto.friend_user_id) for user_friends_dto in user_friends_dtos])

    for friend in friends_update:
        # 已经是好友，剔除dict
        if friend.code in map:
            map.pop(friend.code)
        else:
            try:
                friend_dto = user_info_service.find_by_code(conn, friend.code)
            except my_exception.MyException as e:
                if e.message.find("not existed"):
                    user_info_service.create(conn, friend)

            friend.id = friend_dto.id
            create_by_user_and_friend(conn, uid, friend)

    if len(map) != 0:
        friend_user_ids = []
        for v in map.items():
            friend_user_ids.append(v)

        unable_by_ids(conn, friend_user_ids)

    uid.friends_num = len(friends_update)
    user_info_service.update_spider_version(conn, uid)