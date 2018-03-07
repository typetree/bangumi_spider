# *_*coding:utf-8 *_*
# author: hoicai

from ..client import mysql_client
from ..dto import subject_info_dto


def subject_info_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, name, chinese_name, category, 
		type, picture, bangumi_subject_id, subject_detail_id, topic_list_id, 
		comment_box_id, system_score_id, system_tag_id, remark, status, 
		creator, create_time, updater, update_time
		from subject_info where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = subject_info_dto.SubjectInfoDTO(row)
        uids.append(uid)
    return uids


def subject_info_insert(conn, dto: subject_info_dto.SubjectInfoDTO):
    insert_sql = """ insert into subject_info(
		optimistic, name, chinese_name, category, type, 
		picture, bangumi_subject_id, subject_detail_id, topic_list_id, comment_box_id, 
		system_score_id, system_tag_id, remark, status, creator, 
		create_time, updater, update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.name, dto.chinese_name, dto.category, dto.type,
        dto.picture, dto.bangumi_subject_id, dto.subject_detail_id, dto.topic_list_id, dto.comment_box_id,
        dto.system_score_id, dto.system_tag_id, dto.remark, dto.status, dto.creator,
        dto.create_time, dto.updater, dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def subject_info_update(conn, dto: subject_info_dto.SubjectInfoDTO):
    update_sql = """
		update subject_info set optimistic = optimistic + 1,
		name= %s, chinese_name= %s, category= %s, type= %s, picture= %s, 
		bangumi_subject_id= %s, subject_detail_id= %s, topic_list_id= %s, comment_box_id= %s, system_score_id= %s, 
		system_tag_id= %s, remark= %s, status= %s, creator= %s, create_time= %s, 
		updater= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.name, dto.chinese_name, dto.category, dto.type, dto.picture,
        dto.bangumi_subject_id, dto.subject_detail_id, dto.topic_list_id, dto.comment_box_id, dto.system_score_id,
        dto.system_tag_id, dto.remark, dto.status, dto.creator, dto.create_time,
        dto.updater, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag