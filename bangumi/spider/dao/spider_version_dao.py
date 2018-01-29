# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.client.mysql_client import execute_sql, execute_select_sql


def spider_version_select(conn, where_sql):
    select_sql = """
        select id, optimistic, version, spider_version, active_degree, 
        log, create_time, update_time from spider_version
        where {}
    """.format(where_sql)

    data = execute_select_sql(conn, select_sql)
    return data

def spider_version_insert(conn,data):
    insert_sql = """
        insert into spider_version (
        optimistic, version, spider_version, active_degree, 
        log, status, create_time, update_time )
        values (
        %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        data['optimistic'], data['version'], data["spider_version"], data['active_degree'],
        data['log'], data['status'], data['create_time'], data["update_time"]
    )
    flag = execute_sql(conn, insert_sql, params)
    return flag

def spider_version_update(conn,data):
    update_sql = """
        update spider_version set
        optimistic = optimistic + 1, version = %s, spider_version = %s, active_degree = %s, 
        log = %s, create_time = %s, update_time = %s, status = %s
        where id = %s, optimistic = %s
    """
    params = (
        data['version'], data['spider_version'], data["active_degree"],
        data['log'], data['create_time'], data["update_time"], data["status"],
        data['id'], data['optimistic']
    )
    flag = execute_sql(conn, update_sql, params)
    return flag


