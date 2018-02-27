# *_*coding:utf-8 *_*
# author: hoicai


from ..client import mysql_client
from ..dto import basic_person_dto


def basic_person_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, bangumi_person_id, name, chinese_name, 
		profession, alias, picture, sex, birthday, 
		blood_type, height, homeplace, education, constellation, 
		interest, special_skill, family, recognized_honor, intro, 
		extends, remark, status, create_time, update_time
		from basic_person where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = basic_person_dto.BasicPersonDTO(row)
        uids.append(uid)
    return uids


def basic_person_insert(conn, dto: basic_person_dto.BasicPersonDTO):
    insert_sql = """ insert into basic_person(
		optimistic, bangumi_person_id, name, chinese_name, profession, 
		alias, picture, sex, birthday, blood_type, 
		height, homeplace, education, constellation, interest, 
		special_skill, family, recognized_honor, intro, extends, 
		remark, status, create_time, update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.bangumi_person_id, dto.name, dto.chinese_name, dto.profession,
        dto.alias, dto.picture, dto.sex, dto.birthday, dto.blood_type,
        dto.height, dto.homeplace, dto.education, dto.constellation, dto.interest,
        dto.special_skill, dto.family, dto.recognized_honor, dto.intro, dto.extends,
        dto.remark, dto.status, dto.create_time, dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def basic_person_update(conn, dto: basic_person_dto.BasicPersonDTO):
    update_sql = """
		update basic_person set optimistic = optimistic + 1,
		bangumi_person_id= %s, name= %s, chinese_name= %s, profession= %s, alias= %s, 
		picture= %s, sex= %s, birthday= %s, blood_type= %s, height= %s, 
		homeplace= %s, education= %s, constellation= %s, interest= %s, special_skill= %s, 
		family= %s, recognized_honor= %s, intro= %s, extends= %s, remark= %s, 
		status= %s, create_time= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.bangumi_person_id, dto.name, dto.chinese_name, dto.profession, dto.alias,
        dto.picture, dto.sex, dto.birthday, dto.blood_type, dto.height,
        dto.homeplace, dto.education, dto.constellation, dto.interest, dto.special_skill,
        dto.family, dto.recognized_honor, dto.intro, dto.extends, dto.remark,
        dto.status, dto.create_time, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag