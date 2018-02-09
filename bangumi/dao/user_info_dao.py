# *_*coding:utf-8 *_*
# author: hoicai
from ..client import mysql_client
from ..dto import user_info_dto


def user_info_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, code, name, join_time, 
		homepage, bangumi_user_id, profile_photo, status, hash_value, 
		spider_version, active_degree, friends_num, last_active_time, intro, 
		anime_do, anime_collect, anime_wish, anime_on_hold, anime_dropped, 
		game_do, game_collect, game_wish, game_on_hold, game_dropped, 
		book_do, book_collect, book_wish, book_on_hold, book_dropped, 
		real_do, real_collect, real_wish, real_on_hold, real_dropped, 
		group_num, create_time, update_time
		from user_info where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = user_info_dto.UserInfoDTO(row)
        uids.append(uid)
    return uids


def user_info_insert(conn, dto: user_info_dto.UserInfoDTO):
    insert_sql = """ insert into user_info(
		optimistic, code, name, join_time, homepage, 
		bangumi_user_id, profile_photo, status, hash_value, spider_version, 
		active_degree, friends_num, last_active_time, intro, anime_do, 
		anime_collect, anime_wish, anime_on_hold, anime_dropped, game_do, 
		game_collect, game_wish, game_on_hold, game_dropped, book_do, 
		book_collect, book_wish, book_on_hold, book_dropped, real_do, 
		real_collect, real_wish, real_on_hold, real_dropped, group_num, 
		create_time, update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s, %s, %s, %s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.code, dto.name, dto.join_time, dto.homepage,
        dto.bangumi_user_id, dto.profile_photo, dto.status, dto.hash_value, dto.spider_version,
        dto.active_degree, dto.friends_num, dto.last_active_time, dto.intro, dto.anime_do,
        dto.anime_collect, dto.anime_wish, dto.anime_on_hold, dto.anime_dropped, dto.game_do,
        dto.game_collect, dto.game_wish, dto.game_on_hold, dto.game_dropped, dto.book_do,
        dto.book_collect, dto.book_wish, dto.book_on_hold, dto.book_dropped, dto.real_do,
        dto.real_collect, dto.real_wish, dto.real_on_hold, dto.real_dropped, dto.group_num,
        dto.create_time, dto.update_time
    )
    id = mysql_client.execute_sql(conn, insert_sql, params)
    return id


def user_info_update(conn, dto: user_info_dto.UserInfoDTO):
    update_sql = """
		update user_info set optimistic = optimistic + 1,
		code= %s, name= %s, join_time= %s, homepage= %s, bangumi_user_id= %s, 
		profile_photo= %s, status= %s, hash_value= %s, spider_version= %s, active_degree= %s, 
		friends_num= %s, last_active_time= %s, intro= %s, anime_do= %s, anime_collect= %s, 
		anime_wish= %s, anime_on_hold= %s, anime_dropped= %s, game_do= %s, game_collect= %s, 
		game_wish= %s, game_on_hold= %s, game_dropped= %s, book_do= %s, book_collect= %s, 
		book_wish= %s, book_on_hold= %s, book_dropped= %s, real_do= %s, real_collect= %s, 
		real_wish= %s, real_on_hold= %s, real_dropped= %s, group_num= %s, create_time= %s, 
		update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.code, dto.name, dto.join_time, dto.homepage, dto.bangumi_user_id,
        dto.profile_photo, dto.status, dto.hash_value, dto.spider_version, dto.active_degree,
        dto.friends_num, dto.last_active_time, dto.intro, dto.anime_do, dto.anime_collect,
        dto.anime_wish, dto.anime_on_hold, dto.anime_dropped, dto.game_do, dto.game_collect,
        dto.game_wish, dto.game_on_hold, dto.game_dropped, dto.book_do, dto.book_collect,
        dto.book_wish, dto.book_on_hold, dto.book_dropped, dto.real_do, dto.real_collect,
        dto.real_wish, dto.real_on_hold, dto.real_dropped, dto.group_num, dto.create_time,
        dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag