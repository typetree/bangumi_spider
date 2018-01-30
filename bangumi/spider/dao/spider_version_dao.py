# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.client.mysql_client import execute_sql, execute_select_sql
from bangumi.spider.dto.SpiderVersionDTO import SpiderVersionDTO


def spider_version_select(conn, where_sql):
    select_sql = """
        select id, optimistic, version, spider_version, active_degree, 
        log, status, create_time, update_time from spider_version
        where {}
    """.format(where_sql)

    rows = execute_select_sql(conn, select_sql)
    svds = []
    for row in rows:
        svd = SpiderVersionDTO(row)
        svds.append(svd)
    return svds


def spider_version_insert(conn, svd: SpiderVersionDTO):
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
    flag = execute_sql(conn, insert_sql, params)
    return flag


def spider_version_update(conn, svd: SpiderVersionDTO):
    update_sql = """
        update spider_version set
        optimistic = optimistic + 1, version = %s, spider_version = %s, active_degree = %s, 
        log = %s, status = %s, create_time = %s, update_time = %s
        where id = %s, optimistic = %s
    """
    params = (
        svd.version, svd.spider_version, svd.active_degree,
        svd.log, svd.status, svd.create_time, svd.update_time,
        svd.id, svd.optimistic
    )
    flag = execute_sql(conn, update_sql, params)
    return flag
