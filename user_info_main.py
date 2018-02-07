# *_*coding:utf-8 *_*
# author: hoicai

from bangumi.constants import table_constants
from bangumi.dto import user_spider_version_dto
from bangumi.service import user_info_service
from bangumi.spider import user_info_spider
from bangumi.utils import base_util


def update_user_info(conn, TABLE_NAME, usvd: user_spider_version_dto.UserSpiderVersionDTO, svd):

    uid = user_info_service.find_by_code(conn, usvd.user_code)
    print("{}:{} update user_info".format(uid.code, uid.name))

    update_data = user_info_spider.get_user_info(uid.code)

    usvd = base_util.compare_and_update(usvd, TABLE_NAME, svd, conn, uid, update_data)

    print("{}:{} update {} finish, version:{}".format(uid.code, update_data.name, TABLE_NAME, svd))
    return usvd



if __name__ == "__main__":

    base_util.spider_version_threading(table_constants.TABLE_USER_INFO, update_user_info)

