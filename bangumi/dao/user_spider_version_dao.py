# *_*coding:utf-8 *_*
# author: hoicai


from ..client import mysql_client
from ..dto import user_spider_version_dto


def user_spider_version_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, user_id, user_code, bangumi_user_id, 
		user_info_version, user_info_fingerprint, user_info_active_degree, user_friends_version, user_friends_fingerprint, 
		user_friends_active_degree, user_anime_version, user_anime_fingerprint, user_anime_active_degree, user_game_version, 
		user_game_fingerprint, user_game_active_degree, user_book_version, user_book_fingerprint, user_book_active_degree, 
		user_real_version, user_real_fingerprint, user_real_active_degree, user_mono_character_version, user_mono_character_fingerprint, 
		user_mono_character_active_degree, user_mono_person_version, user_mono_person_fingerprint, user_mono_person_active_degree, user_group_version, 
		user_group_fingerprint, user_group_active_degree, log, status, create_time, 
		update_time
		from user_spider_version where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = user_spider_version_dto.UserSpiderVersion(row)
        uids.append(uid)
    return uids


def user_spider_version_insert(conn, dto: user_spider_version_dto.UserSpiderVersion):
    insert_sql = """ insert into user_spider_version(
		optimistic, user_id, user_code, bangumi_user_id, user_info_version, 
		user_info_fingerprint, user_info_active_degree, user_friends_version, user_friends_fingerprint, user_friends_active_degree, 
		user_anime_version, user_anime_fingerprint, user_anime_active_degree, user_game_version, user_game_fingerprint, 
		user_game_active_degree, user_book_version, user_book_fingerprint, user_book_active_degree, user_real_version, 
		user_real_fingerprint, user_real_active_degree, user_mono_character_version, user_mono_character_fingerprint, user_mono_character_active_degree, 
		user_mono_person_version, user_mono_person_fingerprint, user_mono_person_active_degree, user_group_version, user_group_fingerprint, 
		user_group_active_degree, log, status, create_time, update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.user_id, dto.user_code, dto.bangumi_user_id, dto.user_info_version,
        dto.user_info_fingerprint, dto.user_info_active_degree, dto.user_friends_version, dto.user_friends_fingerprint, dto.user_friends_active_degree,
        dto.user_anime_version, dto.user_anime_fingerprint, dto.user_anime_active_degree, dto.user_game_version, dto.user_game_fingerprint,
        dto.user_game_active_degree, dto.user_book_version, dto.user_book_fingerprint, dto.user_book_active_degree, dto.user_real_version,
        dto.user_real_fingerprint, dto.user_real_active_degree, dto.user_mono_character_version, dto.user_mono_character_fingerprint, dto.user_mono_character_active_degree,
        dto.user_mono_person_version, dto.user_mono_person_fingerprint, dto.user_mono_person_active_degree, dto.user_group_version, dto.user_group_fingerprint,
        dto.user_group_active_degree, dto.log, dto.status, dto.create_time, dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def user_spider_version_update(conn, dto: user_spider_version_dto.UserSpiderVersion):
    update_sql = """
		update user_spider_version set optimistic = optimistic + 1,
		user_id= %s, user_code= %s, bangumi_user_id= %s, user_info_version= %s, user_info_fingerprint= %s, 
		user_info_active_degree= %s, user_friends_version= %s, user_friends_fingerprint= %s, user_friends_active_degree= %s, user_anime_version= %s, 
		user_anime_fingerprint= %s, user_anime_active_degree= %s, user_game_version= %s, user_game_fingerprint= %s, user_game_active_degree= %s, 
		user_book_version= %s, user_book_fingerprint= %s, user_book_active_degree= %s, user_real_version= %s, user_real_fingerprint= %s, 
		user_real_active_degree= %s, user_mono_character_version= %s, user_mono_character_fingerprint= %s, user_mono_character_active_degree= %s, user_mono_person_version= %s, 
		user_mono_person_fingerprint= %s, user_mono_person_active_degree= %s, user_group_version= %s, user_group_fingerprint= %s, user_group_active_degree= %s, 
		log= %s, status= %s, create_time= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.user_id, dto.user_code, dto.bangumi_user_id, dto.user_info_version, dto.user_info_fingerprint,
        dto.user_info_active_degree, dto.user_friends_version, dto.user_friends_fingerprint, dto.user_friends_active_degree, dto.user_anime_version,
        dto.user_anime_fingerprint, dto.user_anime_active_degree, dto.user_game_version, dto.user_game_fingerprint, dto.user_game_active_degree,
        dto.user_book_version, dto.user_book_fingerprint, dto.user_book_active_degree, dto.user_real_version, dto.user_real_fingerprint,
        dto.user_real_active_degree, dto.user_mono_character_version, dto.user_mono_character_fingerprint, dto.user_mono_character_active_degree, dto.user_mono_person_version,
        dto.user_mono_person_fingerprint, dto.user_mono_person_active_degree, dto.user_group_version, dto.user_group_fingerprint, dto.user_group_active_degree,
        dto.log, dto.status, dto.create_time, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag