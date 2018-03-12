# *_*coding:utf-8 *_*
# author: hoicai
import random

import time
import traceback

import requests
from bs4 import BeautifulSoup
from multiprocessing import Queue

from bangumi.constants import url_constants, table_constants
from bangumi.dto import subject_info_dto, subject_profession_person_dto
from bangumi.factory import subject_strategy_factory


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
        return None
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
        return None
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


def get_intro_by_soup(soup):
    intros = soup.select("#subject_summary")
    if len(intros) == 0:
        return None
    intro = intros[0].get_text()
    return intro


def get_detail_dto_by_category(category, soup, subject_profession_person_queue:Queue, profession_dicts):

    dto = subject_strategy_factory.get_subject_dto_by_category(category)

    infomations = soup.select("#infobox > li")
    type = get_type_by_soup(category, soup)

    for infomation in infomations:
        temp = infomation.get_text()
        left_part = temp[:temp.find(":")]
        right_part = temp[temp.find(":")+1:].strip()

        # 职业信息封装
        if left_part in profession_dicts:
            right_person_list = right_part.split("、")
            persons = infomation.select("a")

            temp_list = []
            for person in persons:
                person_href = person.get("href")
                bangumi_person_id = person_href[person_href.rfind('/')+1:]
                person_name = person.get_text()
                temp_list.append(person_name)

                sppd = subject_profession_person_dto.SubjectProfessionPersonDTO()
                sppd.profession_id = profession_dicts[left_part]
                sppd.profession_name = left_part
                sppd.bangumi_person_id = bangumi_person_id
                sppd.person_name = person_name
                subject_profession_person_queue.put(sppd)
                # print(sppd.profession_id,sppd.profession_name,sppd.bangumi_person_id,sppd.person_name)

            for right_person in right_person_list:
                if right_person not in temp_list:
                    sppd = subject_profession_person_dto.SubjectProfessionPersonDTO()
                    sppd.category = category
                    sppd.type = type
                    sppd.profession_id = profession_dicts[left_part]
                    sppd.profession_name = left_part
                    sppd.bangumi_person_id = None
                    sppd.person_name = right_person
                    subject_profession_person_queue.put(sppd)
                    # print(right_person)

        else:
            dto = subject_strategy_factory.set_subject_dto_by_category(category)(left_part, right_part, dto)

    return dto


if __name__ == "__main__":

    for i in range(1, 10000):
        soup = get_subject_soup(i)
        intro = get_intro_by_soup(soup)

        # get_picture_by_soup(soup)
        # data = get_message_by_soup(soup)
        # if data is None:
        #     continue
        # print(data)


