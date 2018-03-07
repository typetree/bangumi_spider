# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants import table_constants
from bangumi.dao import spider_version_person_dao
from bangumi.dto import basic_person_dto, spider_version_person_dto
from bangumi.utils import common_util


def find_max_bangumi_person_id(conn):
    sql = "1=1 order by bangumi_person_id desc limit 1"

    svpds = spider_version_person_dao.spider_version_person_select(conn, sql)

    if svpds is None or len(svpds) == 0:
        return 1
    svpd = svpds[0]
    return svpd.bangumi_person_id+1


def create_by_bangumi_person_id(conn, bangumi_person_id):
    svpd = spider_version_person_dto.SpiderVersionPersonDTO()
    svpd.optimistic = 0
    svpd.person_id = 0
    svpd.bangumi_person_id = bangumi_person_id
    svpd.person_name = ''
    svpd.basic_person_active_degree = 100
    svpd.log = ''
    svpd.status = table_constants.ENABLE
    time = common_util.get_now_time()
    svpd.update_time = time
    svpd.create_time = time

    id = spider_version_person_dao.spider_version_person_insert(conn, svpd)
    svpd.id = id
    return svpd


def update_by_person_dto(conn, svpd:spider_version_person_dto.SpiderVersionPersonDTO,
                         person_dto:basic_person_dto.BasicPersonDTO, version):
    svpd.person_id = person_dto.id
    svpd.person_name = person_dto.name
    svpd.basic_person_version = version
    svpd.basic_person_fingerprint = common_util.hashlib_md5([person_dto])
    svpd.basic_person_active_degree = 100
    svpd.update_time = common_util.get_now_time()
    spider_version_person_dao.spider_version_person_update(conn, svpd)


def unable_version(conn, svpd:spider_version_person_dto.SpiderVersionPersonDTO, version, log):
    svpd.log = log + ", version:{}".format(version)
    svpd.status = table_constants.UNABLE
    svpd.update_time = common_util.get_now_time()
    spider_version_person_dao.spider_version_person_update(conn, svpd)