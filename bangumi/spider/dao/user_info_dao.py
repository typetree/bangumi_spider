# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.client.mysql_client import execute_sql, execute_select_sql


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

    data = execute_select_sql(conn, select_sql)
    return data


def user_info_insert(conn, data):
    insert_sql = """
        insert into users_info (
        optimistic, code, name, join_time, 
        homepage, bangumi_user_id, status, hash_value, spider_version,
        active_degree, friends_num, last_active_time, intro, anime_do, 
        anime_collect, anime_wish, anime_on_hold, anime_dropped, game_do,
        game_collect, game_wish, game_on_hold, game_dropped, book_do, 
        book_collect, book_wish, book_on_hold, book_dropped, real_do,
        real_collect, real_wish, real_on_hold, real_dropped, group_num,
        create_time, update_time)
        values (
        %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        data['optimistic'], data['code'], data["name"], data['join_time'],
        data['homepage'], data['bangumi_user_id'], data["status"], data['hash_value'],
        data['spider_version'],
        data['active_degree'], data['friends_num'], data["last_active_time"], data['intro'],
        data['anime_do'],
        data['anime_collect'], data['anime_wish'], data["anime_on_hold"], data['anime_dropped'],
        data['game_do'],
        data['game_collect'], data['game_wish'], data["game_on_hold"], data['game_on_hold'],
        data['book_do'],
        data['book_collect'], data['book_wish'], data["book_on_hold"], data['book_dropped'],
        data['real_do'],
        data['real_collect'], data['real_wish'], data["real_on_hold"], data['real_dropped'],
        data['group_num'],
        data['create_time'], data['update_time']
    )
    flag = execute_sql(conn, insert_sql, params)
    return flag


def user_info_update(conn, data):
    update_sql = """
        update users_info set
        optimistic = optimistic + 1, code = %s, name = %s, join_time = %s, 
        homepage = %s, bangumi_user_id = %s, status = %s, hash_value = %s, spider_version = %s,
        active_degree = %s, friends_num = %s, last_active_time = %s, intro = %s, anime_do = %s,
        anime_collect = %s, anime_wish = %s, anime_on_hold = %s, anime_dropped = %s, game_do = %s,
        game_collect = %s, game_wish = %s, game_on_hold = %s, game_on_hold = %s, book_do = %s,
        book_collect = %s, book_wish = %s, book_on_hold = %s, book_dropped = %s, real_do = %s,
        real_collect = %s, real_wish = %s, real_on_hold = %s, real_dropped = %s, group_num = %s,
        create_time = %s, update_time = %s
        where id = %s, optimistic = %s
    """
    params = (
        data['code'], data["name"], data['join_time'],
        data['homepage'], data['bangumi_user_id'], data["status"], data['hash_value'],
        data['spider_version'],
        data['active_degree'], data['friends_num'], data["last_active_time"], data['intro'],
        data['anime_do'],
        data['anime_collect'], data['anime_wish'], data["anime_on_hold"], data['anime_dropped'],
        data['game_do'],
        data['game_collect'], data['game_wish'], data["game_on_hold"], data['game_on_hold'],
        data['book_do'],
        data['book_collect'], data['book_wish'], data["book_on_hold"], data['book_dropped'],
        data['real_do'],
        data['real_collect'], data['real_wish'], data["real_on_hold"], data['real_dropped'],
        data['group_num'],
        data['create_time'], data['update_time'],
        data['id'], data['optimistic']
    )
    flag = execute_sql(conn, update_sql, params)
    return flag
