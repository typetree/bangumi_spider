# *_*coding:utf-8 *_*
# author: hoicai
from ..client import mysql_client
from ..dto import user_info_dto


def user_info_select(conn, where_sql):
    select_sql = """ 
        select id, optimistic, code, name, join_time, 
        homepage, bangumi_user_id, status, hash_value, spider_version,
        active_degree, friends_num, last_active_time, intro, anime_do, 
        anime_collect, anime_wish, anime_on_hold, anime_dropped, game_do,
        game_collect, game_wish, game_on_hold, game_dropped, book_do, 
        book_collect, book_wish, book_on_hold, book_dropped, real_do,
        real_collect, real_wish, real_on_hold, real_dropped, group_num,
        create_time, update_time from user_info
        where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = user_info_dto.UserInfoDTO(row)
        uids.append(uid)
    return uids


def user_info_insert(conn, uid: user_info_dto.UserInfoDTO):
    insert_sql = """
        insert into user_info (
        optimistic, code, name, join_time, 
        homepage, bangumi_user_id, status, hash_value, spider_version,
        active_degree, friends_num, last_active_time, intro, 
        anime_do, anime_collect, anime_wish, anime_on_hold, anime_dropped, 
        game_do, game_collect, game_wish, game_on_hold, game_dropped, 
        book_do, book_collect, book_wish, book_on_hold, book_dropped, 
        real_do, real_collect, real_wish, real_on_hold, real_dropped, 
        group_num, create_time, update_time)
        values (
        %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        uid.optimistic, uid.code, uid.name, uid.join_time,
        uid.homepage, uid.bangumi_user_id, uid.status, uid.hash_value, uid.spider_version,
        uid.active_degree, uid.friends_num, uid.last_active_time, uid.intro,
        uid.anime_do, uid.anime_collect, uid.anime_wish, uid.anime_on_hold, uid.anime_dropped,
        uid.game_do, uid.game_collect, uid.game_wish, uid.game_on_hold, uid.game_dropped,
        uid.book_do, uid.book_collect, uid.book_wish, uid.book_on_hold, uid.book_dropped,
        uid.real_do, uid.real_collect, uid.real_wish, uid.real_on_hold, uid.real_dropped,
        uid.group_num, uid.create_time, uid.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def user_info_update(conn, uid: user_info_dto.UserInfoDTO):
    update_sql = """
        update user_info set
        optimistic = optimistic + 1, code = %s, name = %s, join_time = %s, 
        homepage = %s, bangumi_user_id = %s, status = %s, hash_value = %s, spider_version = %s,
        active_degree = %s, friends_num = %s, last_active_time = %s, intro = %s, 
        anime_do = %s, anime_collect = %s, anime_wish = %s, anime_on_hold = %s, anime_dropped = %s, 
        game_do = %s, game_collect = %s, game_wish = %s, game_on_hold = %s, game_on_hold = %s, 
        book_do = %s, book_collect = %s, book_wish = %s, book_on_hold = %s, book_dropped = %s, 
        real_do = %s, real_collect = %s, real_wish = %s, real_on_hold = %s, real_dropped = %s, 
        group_num = %s, create_time = %s, update_time = %s
        where id = %s and optimistic = %s
    """
    params = (
        uid.code, uid.name, uid.join_time,
        uid.homepage, uid.bangumi_user_id, uid.status, uid.hash_value, uid.spider_version,
        uid.active_degree, uid.friends_num, uid.last_active_time, uid.intro,
        uid.anime_do, uid.anime_collect, uid.anime_wish, uid.anime_on_hold, uid.anime_dropped,
        uid.game_do, uid.game_collect, uid.game_wish, uid.game_on_hold, uid.game_dropped,
        uid.book_do, uid.book_collect, uid.book_wish, uid.book_on_hold, uid.book_dropped,
        uid.real_do, uid.real_collect, uid.real_wish, uid.real_on_hold, uid.real_dropped,
        uid.group_num, uid.create_time, uid.update_time,
        uid.id, uid.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag
