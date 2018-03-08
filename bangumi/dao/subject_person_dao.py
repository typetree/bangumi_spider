# *_*coding:utf-8 *_*
# author: hoicai

from ..client import mysql_client
from ..dto import subject_profession_person_dto


def subject_profession_person_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, subject_id, subject_detail_id, category, 
		name, type, profession_id, profession_name, person_id, 
		bangumi_person_id, person_name, person_chinese_name, remark, status, 
		create_time, update_time
		from subject_profession_person where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = subject_profession_person_dto.SubjectProfessionPersonDTO(row)
        uids.append(uid)
    return uids


def subject_profession_person_insert(conn, dto: subject_profession_person_dto.SubjectProfessionPersonDTO):
    insert_sql = """ insert into subject_profession_person(
		optimistic, subject_id, subject_detail_id, category, name, 
		type, profession_id, profession_name, person_id, bangumi_person_id, 
		person_name, person_chinese_name, remark, status, create_time, 
		update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.subject_id, dto.subject_detail_id, dto.category, dto.name,
        dto.type, dto.profession_id, dto.profession_name, dto.person_id, dto.bangumi_person_id,
        dto.person_name, dto.person_chinese_name, dto.remark, dto.status, dto.create_time,
        dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def subject_profession_person_update(conn, dto: subject_profession_person_dto.SubjectProfessionPersonDTO):
    update_sql = """
		update subject_profession_person set optimistic = optimistic + 1,
		subject_id= %s, subject_detail_id= %s, category= %s, name= %s, type= %s, 
		profession_id= %s, profession_name= %s, person_id= %s, bangumi_person_id= %s, person_name= %s, 
		person_chinese_name= %s, remark= %s, status= %s, create_time= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.subject_id, dto.subject_detail_id, dto.category, dto.name, dto.type,
        dto.profession_id, dto.profession_name, dto.person_id, dto.bangumi_person_id, dto.person_name,
        dto.person_chinese_name, dto.remark, dto.status, dto.create_time, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag