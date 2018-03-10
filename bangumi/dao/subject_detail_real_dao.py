# *_*coding:utf-8 *_*
# author: hoicai

from ..client import mysql_client
from ..dto import subject_detail_real_dto


def subject_detail_real_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, subject_id, bangumi_subject_id, name, 
		type, picture, chinese_name, alias, topic_num, 
		send_out_week, release_date, end_date, real_type, region, 
		language, time_length, channel, tv_network, tv_station, 
		video_standard, audio_standard, premiere_country, premiere_region, taiwan_name, 
		hk_name, south_asia_name, website, imdb_id, tv_com_id, 
		extends, intro, topic_list_id, comment_box_id, system_score_id, 
		system_tag_id, do, collect, wish, on_hold, 
		dropped, remark, status, creator, create_time, 
		updater, update_time
		from subject_detail_real where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = subject_detail_real_dto.SubjectDetailRealDTO(row)
        uids.append(uid)
    return uids


def subject_detail_real_insert(conn, dto: subject_detail_real_dto.SubjectDetailRealDTO):
    insert_sql = """ insert into subject_detail_real(
		optimistic, subject_id, bangumi_subject_id, name, type, 
		picture, chinese_name, alias, topic_num, send_out_week, 
		release_date, end_date, real_type, region, language, 
		time_length, channel, tv_network, tv_station, video_standard, 
		audio_standard, premiere_country, premiere_region, taiwan_name, hk_name, 
		south_asia_name, website, imdb_id, tv_com_id, extends, 
		intro, topic_list_id, comment_box_id, system_score_id, system_tag_id, 
		do, collect, wish, on_hold, dropped, 
		remark, status, creator, create_time, updater, 
		update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.subject_id, dto.bangumi_subject_id, dto.name, dto.type,
        dto.picture, dto.chinese_name, dto.alias, dto.topic_num, dto.send_out_week,
        dto.release_date, dto.end_date, dto.real_type, dto.region, dto.language,
        dto.time_length, dto.channel, dto.tv_network, dto.tv_station, dto.video_standard,
        dto.audio_standard, dto.premiere_country, dto.premiere_region, dto.taiwan_name, dto.hk_name,
        dto.south_asia_name, dto.website, dto.imdb_id, dto.tv_com_id, dto.extends,
        dto.intro, dto.topic_list_id, dto.comment_box_id, dto.system_score_id, dto.system_tag_id,
        dto.do, dto.collect, dto.wish, dto.on_hold, dto.dropped,
        dto.remark, dto.status, dto.creator, dto.create_time, dto.updater,
        dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def subject_detail_real_update(conn, dto: subject_detail_real_dto.SubjectDetailRealDTO):
    update_sql = """
		update subject_detail_real set optimistic = optimistic + 1,
		subject_id= %s, bangumi_subject_id= %s, name= %s, type= %s, picture= %s, 
		chinese_name= %s, alias= %s, topic_num= %s, send_out_week= %s, release_date= %s, 
		end_date= %s, real_type= %s, region= %s, language= %s, time_length= %s, 
		channel= %s, tv_network= %s, tv_station= %s, video_standard= %s, audio_standard= %s, 
		premiere_country= %s, premiere_region= %s, taiwan_name= %s, hk_name= %s, south_asia_name= %s, 
		website= %s, imdb_id= %s, tv_com_id= %s, extends= %s, intro= %s, 
		topic_list_id= %s, comment_box_id= %s, system_score_id= %s, system_tag_id= %s, do= %s, 
		collect= %s, wish= %s, on_hold= %s, dropped= %s, remark= %s, 
		status= %s, creator= %s, create_time= %s, updater= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.subject_id, dto.bangumi_subject_id, dto.name, dto.type, dto.picture,
        dto.chinese_name, dto.alias, dto.topic_num, dto.send_out_week, dto.release_date,
        dto.end_date, dto.real_type, dto.region, dto.language, dto.time_length,
        dto.channel, dto.tv_network, dto.tv_station, dto.video_standard, dto.audio_standard,
        dto.premiere_country, dto.premiere_region, dto.taiwan_name, dto.hk_name, dto.south_asia_name,
        dto.website, dto.imdb_id, dto.tv_com_id, dto.extends, dto.intro,
        dto.topic_list_id, dto.comment_box_id, dto.system_score_id, dto.system_tag_id, dto.do,
        dto.collect, dto.wish, dto.on_hold, dto.dropped, dto.remark,
        dto.status, dto.creator, dto.create_time, dto.updater, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag