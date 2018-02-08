# *_*coding:utf-8 *_*
# author: hoicai
from ..dto import spider_version_dto
from ..client import mysql_client


def spider_version_select(conn, where_sql):
    select_sql = """
        select id, optimistic, version, spider_version, active_degree, 
        log, status, create_time, update_time from spider_version
        where {}
    """.format(where_sql)

    rows = mysql_client.execute_select_sql(conn, select_sql)
    svds = []
    for row in rows:
        svd = spider_version_dto.SpiderVersionDTO(row)
        svds.append(svd)
    return svds


def spider_version_insert(conn, svd: spider_version_dto):
    insert_sql = """
        insert into spider_version (
        optimistic, version, spider_version, active_degree, 
        log, status, create_time, update_time )
        values (
        %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        svd.optimistic, svd.version, svd.spider_version, svd.active_degree,
        svd.log, svd.status, svd.create_time, svd.update_time
    )
    id = mysql_client.execute_sql(conn, insert_sql, params)
    return id


def spider_version_update(conn, svd: spider_version_dto):
    update_sql = """
        update spider_version set
        optimistic = optimistic + 1, version = %s, spider_version = %s, active_degree = %s, 
        log = %s, status = %s, create_time = %s, update_time = %s
        where id = %s and optimistic = %s
    """
    params = (
        svd.version, svd.spider_version, svd.active_degree,
        svd.log, svd.status, svd.create_time, svd.update_time,
        svd.id, svd.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag
