# *_*coding:utf-8 *_*
# author: hoicai
import random

import time
import traceback

import requests
from bs4 import BeautifulSoup

from bangumi.constants import url_constants, table_constants
from bangumi.dto import subject_info_dto


def get_subject_soup(subject_id):
    subject_url = url_constants.get_subject_url(subject_id)
    headers = url_constants.get_user_headers()
    
    time.sleep(random.uniform(0.2, 0.5))
    Flag = True
    while Flag:
        try:
            Flag = False
            response = requests.get(subject_url, headers=headers)
        except Exception:
            print(traceback.format_exc())
            Flag = True

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    return soup


def get_bangumi_id_by_soup(soup):
    ids = soup.select("#headerSubject > h1 > a")
    if len(ids) == 0:
        return None
    id = ids[0].get('href')
    id = id[id.rfind('/')+1:]
    return id


def get_category_by_soup(soup):

    categorys = soup.select("#siteSearchSelect > option")
    # print(categorys)
    for category in categorys:
        if category.get('selected'):
            category = category.get_text()
            category_list = table_constants.get_categorys()
            if category in category_list:
                category = category_list[category]
            return category
    pass


def get_type_by_soup(category, soup):
    types = soup.select("#headerSubject > h1 > small")
    if len(types) == 0:
        return ''
    type = types[0].get_text()
    type_list = table_constants.get_types_by_category(category)
    if type in type_list:
        type = type_list[type]
    return type


def get_name_by_soup(soup):
    names = soup.select("#headerSubject > h1 > a")
    if len(names) == 0:
        return None
    name = names[0].get_text()
    if name == '坟场':
        return None
    return name


def get_picture_by_soup(soup):
    pictures = soup.select("#bangumiInfo > div > div > a > img")
    if len(pictures) == 0:
        return ''
    picture = pictures[0].get("src")
    return picture


def get_message_by_soup(soup):
    id = get_bangumi_id_by_soup(soup)
    if id is None:
        return None
    name = get_name_by_soup(soup)
    if name is None:
        return None
    category = get_category_by_soup(soup)
    type = get_type_by_soup(category, soup)
    # print(id, category, type, name)
    data = {
        "bangumi_subject_id": id,
        "name": name,
        "category": category,
        "type": type
    }
    return data


def get_dto_by_soup(soup):
    dto = subject_info_dto.SubjectInfoDTO()

    soup.select("")


if __name__ == "__main__":

    for i in range(1, 10000):
        soup = get_subject_soup(i)
        get_picture_by_soup(soup)
        # data = get_message_by_soup(soup)
        # if data is None:
        #     continue
        # print(data)

