# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants import table_constants
from bangumi.dao import basic_person_dao
from bangumi.dto import basic_person_dto
from bangumi.utils import common_util


def spider_create(conn, person_dto: basic_person_dto.BasicPersonDTO):

    person_dto.optimistic = 0
    person_dto.status = table_constants.ENABLE

    time = common_util.get_now_time()
    person_dto.create_time = time
    person_dto.update_time = time

    id = basic_person_dao.basic_person_insert(conn, person_dto)
    person_dto.id = id
    return person_dto