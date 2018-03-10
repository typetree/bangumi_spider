# *_*coding:utf-8 *_*
# author: hoicai

from ..client import mysql_client
from ..dto import subject_detail_music_dto


def subject_detail_music_select(conn, where_sql):
    select_sql = """ select
            id, optimistic, subject_id, bangumi_subject_id, name, 
            type, picture, chinese_name, alias, version_feature, 
            sale_date, price, time_length, discs_num, extends, 
            intro, topic_list_id, comment_box_id, system_score_id, system_tag_id, 
            do, collect, wish, on_hold, dropped, 
            remark, status, creator, create_time, updater, 
            update_time
            from subject_detail_music where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = subject_detail_music_dto.SubjectDetailMusicDTO(row)
        uids.append(uid)
    return uids


def subject_detail_music_insert(conn, dto: subject_detail_music_dto.SubjectDetailMusicDTO):
    insert_sql = """ insert into subject_detail_music(
		optimistic, subject_id, bangumi_subject_id, name, type, 
		picture, chinese_name, alias, version_feature, sale_date, 
		price, time_length, discs_num, extends, intro, 
		topic_list_id, comment_box_id, system_score_id, system_tag_id, do, 
		collect, wish, on_hold, dropped, remark, 
		status, creator, create_time, updater, update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """


    params = (
        dto.optimistic, dto.subject_id, dto.bangumi_subject_id, dto.name, dto.type,
        dto.picture, dto.chinese_name, dto.alias, dto.version_feature, dto.sale_date,
        dto.price, dto.time_length, dto.discs_num, dto.extends, dto.intro,
        dto.topic_list_id, dto.comment_box_id, dto.system_score_id, dto.system_tag_id, dto.do,
        dto.collect, dto.wish, dto.on_hold, dto.dropped, dto.remark,
        dto.status, dto.creator, dto.create_time, dto.updater, dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def subject_detail_music_update(conn, dto: subject_detail_music_dto.SubjectDetailMusicDTO):
    update_sql = """
		update subject_detail_music set optimistic = optimistic + 1,
		subject_id= %s, bangumi_subject_id= %s, name= %s, type= %s, picture= %s, 
		chinese_name= %s, alias= %s, version_feature= %s, sale_date= %s, price= %s, 
		time_length= %s, discs_num= %s, extends= %s, intro= %s, topic_list_id= %s, 
		comment_box_id= %s, system_score_id= %s, system_tag_id= %s, do= %s, collect= %s, 
		wish= %s, on_hold= %s, dropped= %s, remark= %s, status= %s, 
		creator= %s, create_time= %s, updater= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.subject_id, dto.bangumi_subject_id, dto.name, dto.type, dto.picture,
        dto.chinese_name, dto.alias, dto.version_feature, dto.sale_date, dto.price,
        dto.time_length, dto.discs_num, dto.extends, dto.intro, dto.topic_list_id,
        dto.comment_box_id, dto.system_score_id, dto.system_tag_id, dto.do, dto.collect,
        dto.wish, dto.on_hold, dto.dropped, dto.remark, dto.status,
        dto.creator, dto.create_time, dto.updater, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag
