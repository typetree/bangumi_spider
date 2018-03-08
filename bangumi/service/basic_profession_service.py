# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.dao import basic_profession_dao


def find_dict_by_category(conn, category):

    sql = "category = '{}'".format(category)
    dtos = basic_profession_dao.basic_profession_select(conn, sql)
    profession_dicts = dict([(dto.name, dto.id) for dto in dtos])
    return profession_dicts