# *_*coding:utf-8 *_*
# author: hoicai

from bangumi.dto import user_info_dto
from bangumi.spider import user_friends_spider
from bangumi.constants import table_constants
from bangumi.utils import base_util




def update_user_frinds(uid: user_info_dto.UserInfoDTO):

    friends_update = user_friends_spider.find_friends(uid.code)
    return friends_update


if __name__ == "__main__":

    base_util.spider_version_threading(
        table_constants.CATEGORY_USER, table_constants.TABLE_USER_FRIENDS, update_user_frinds)

