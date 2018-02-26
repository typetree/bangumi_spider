# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants import table_constants
from bangumi.dto import basic_person_dto
from bangumi.service import basic_person_service
from bangumi.utils import base_util


def spider_basic_person(person_dto:basic_person_dto.BasicPersonDTO):
    basic_person_spider.get_basic_person(uid.bangumi_user_id)
    pass


if __name__ == "__main__":

    base_util.spider_version_threading(
        table_constants.CATEGORY_USER, table_constants.TABLE_USER_INFO,
        spider_basic_person, basic_person_service.spider_update)

    exit()