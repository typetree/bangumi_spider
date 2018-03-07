# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants import table_constants
from bangumi.dao import subject_info_dao
from bangumi.dto import subject_info_dto
from bangumi.utils import common_util


def find_max_bangumi_id(conn):
    sql = '1=1 order by bangumi_subject_id desc limit 1'
    sids = subject_info_dao.subject_info_select(conn,sql)

    if sids is None or len(sids) == 0:
        return 1
    dto = sids[0]
    return dto.bangumi_subject_id+1


def insert_by_spider(conn, data):
    dto = subject_info_dto.SubjectInfoDTO()
    dto.bangumi_subject_id = data['bangumi_subject_id']
    dto.name = data['name']
    dto.category = data['category']
    dto.type = data['type']
    dto = insert(conn, dto)
    return dto


def insert(conn, dto: subject_info_dto.SubjectInfoDTO):
    time = common_util.get_now_time()
    dto.optimistic = 0
    dto.status = table_constants.ENABLE
    dto.creator = table_constants.SPIDER_SYSTEM
    dto.updater = table_constants.SPIDER_SYSTEM
    dto.update_time = time
    dto.create_time = time
    id = subject_info_dao.subject_info_insert(conn, dto)
    dto.id = id
    return dto