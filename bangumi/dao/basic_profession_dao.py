# *_*coding:utf-8 *_*
# author: hoicai

from ..client import mysql_client
from ..dto import basic_profession_dto


def basic_profession_select(conn, where_sql):
    select_sql = """ select
		id, optimistic, category, order_name, name, 
		remark, status, create_time, update_time
		from basic_profession where """ + where_sql

    rows = mysql_client.execute_select_sql(conn, select_sql)
    uids =[]
    for row in rows:
        uid = basic_profession_dto.BasicProfessionDTO(row)
        uids.append(uid)
    return uids


def basic_profession_insert(conn, dto: basic_profession_dto.BasicProfessionDTO):
    insert_sql = """ insert into basic_profession(
		optimistic, category, order_name, name, remark, 
		status, create_time, update_time)
	values(
		%s, %s, %s, %s, %s, %s, %s, %s) """

    params = (
        dto.optimistic, dto.category, dto.order_name, dto.name, dto.remark,
        dto.status, dto.create_time, dto.update_time
    )
    flag = mysql_client.execute_sql(conn, insert_sql, params)
    return flag


def basic_profession_update(conn, dto: basic_profession_dto.BasicProfessionDTO):
    update_sql = """
		update basic_profession set optimistic = optimistic + 1,
		category= %s, order_name= %s, name= %s, remark= %s, status= %s, 
		create_time= %s, update_time= %s
		where id = %s and optimistic = %s """
    params = (
        dto.category, dto.order_name, dto.name, dto.remark, dto.status,
        dto.create_time, dto.update_time,
        dto.id, dto.optimistic
    )
    flag = mysql_client.execute_sql(conn, update_sql, params)
    return flag
