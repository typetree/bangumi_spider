# *_*coding:utf-8 *_*
# author: hoicai

from ..client import mysql_client
from ..dto import user_friends_dto


def user_friends_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, user_id, user_code, user_name, 
		friend_user_id, friend_user_code, friend_user_name, is_friend, status, 
		create_time, update_time
		from user_friends where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = user_friends_dto.UserFriendsDTO(row)
        uids.append(uid)
    return uids


def user_friends_insert(conn, dto: user_friends_dto.UserFriendsDTO):
    insert_sql = """ insert into user_friends(
		optimistic, user_id, user_code, user_name, friend_user_id, 
		friend_user_code, friend_user_name, is_friend, status, create_time, 
		update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
		%s) """

    params = (
        dto.optimistic, dto.user_id, dto.user_code, dto.user_name, dto.friend_user_id,
        dto.friend_user_code, dto.friend_user_name, dto.is_friend, dto.status, dto.create_time,
        dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def user_friends_update(conn, dto: user_friends_dto.UserFriendsDTO):
    update_sql = """
		update user_friends set optimistic = optimistic + 1,
		user_id= %s, user_code= %s, user_name= %s, friend_user_id= %s, friend_user_code= %s, 
		friend_user_name= %s, is_friend= %s, status= %s, create_time= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.user_id, dto.user_code, dto.user_name, dto.friend_user_id, dto.friend_user_code,
        dto.friend_user_name, dto.is_friend, dto.status, dto.create_time, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag


def unable_by_ids(conn, time, ids):
    sql = """
        update user_friends set optimistic = optimistic + 1, status = %s, update_time = '{}'
        where id in ({})
    """.format(time, ids)
    return mysql_client.execute_sql(conn, sql)