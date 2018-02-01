# *_*coding:utf-8 *_*
# author: hoicai


from ..client import mysql_client
from ..dto import user_spider_version_dto


def user_spider_version_select(conn, where_sql):
    select_sql = """ select
		id,optimistic,user_id,user_code,bangumi_user_id,user_info_version,
		user_info_fingerprint,user_info_active_degree,user_friends_version,user_friends_fingerprint,user_friends_active_degree,
		user_anime_version,user_anime_fingerprint,user_anime_active_degree,user_game_version,user_game_fingerprint,
		user_game_active_degree,user_book_version,user_book_fingerprint,user_book_active_degree,user_real_version,
		user_real_fingerprint,user_real_active_degree,user_mono_character_version,user_mono_character_fingerprint,user_mono_character_active_degree,
		user_mono_person_version,user_mono_person_fingerprint,user_mono_person_active_degree,user_group_version,user_group_fingerprint,
		user_group_active_degree,create_time,update_time
		from user_spider_version where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = user_spider_version_dto.UserSpiderVersion(row)
        uids.append(uid)
    return uids