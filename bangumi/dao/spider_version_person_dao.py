# *_*coding:utf-8 *_*
# author: hoicai
from ..client import mysql_client
from ..dto import spider_version_person_dto


def spider_version_person_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, person_id, bangumi_person_id, person_name, 
		basic_person_version, basic_person_fingerprint, basic_person_active_degree, log, status, 
		create_time, update_time
		from spider_version_person where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = spider_version_person_dto.SpiderVersionPersonDTO(row)
        uids.append(uid)
    return uids


def spider_version_person_insert(conn, dto: spider_version_person_dto.SpiderVersionPersonDTO):
    insert_sql = """ insert into spider_version_person(
		optimistic, person_id, bangumi_person_id, person_name, basic_person_version, 
		basic_person_fingerprint, basic_person_active_degree, log, status, create_time, 
		update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s) """

    params = (
        dto.optimistic, dto.person_id, dto.bangumi_person_id, dto.person_name, dto.basic_person_version,
        dto.basic_person_fingerprint, dto.basic_person_active_degree, dto.log, dto.status, dto.create_time,
        dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def spider_version_person_update(conn, dto: spider_version_person_dto.SpiderVersionPersonDTO):
    update_sql = """
		update spider_version_person set optimistic = optimistic + 1,
		person_id= %s, bangumi_person_id= %s, person_name= %s, basic_person_version= %s, basic_person_fingerprint= %s, 
		basic_person_active_degree= %s, log= %s, status= %s, create_time= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.person_id, dto.bangumi_person_id, dto.person_name, dto.basic_person_version, dto.basic_person_fingerprint,
        dto.basic_person_active_degree, dto.log, dto.status, dto.create_time, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag