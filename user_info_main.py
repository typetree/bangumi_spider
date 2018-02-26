# *_*coding:utf-8 *_*
# author: hoicai

from bangumi.constants import table_constants
from bangumi.dto import user_info_dto
from bangumi.service import user_info_service
from bangumi.spider import user_info_spider
from bangumi.utils import base_util


def update_user_info(uid: user_info_dto.UserInfoDTO):

    update_data = user_info_spider.get_user_info(uid.bangumi_user_id)

    return update_data


if __name__ == "__main__":

    base_util.spider_version_threading(
        table_constants.CATEGORY_USER, table_constants.TABLE_USER_INFO,
        update_user_info, user_info_service.spider_update)

    exit()