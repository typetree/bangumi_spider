# *_*coding:utf-8 *_*
# author: hoicai
import random
import traceback
import time
import requests
from bs4 import BeautifulSoup
from bangumi.constants import url_constants
from bangumi.dto import basic_person_dto
from bangumi.constants import table_constants
from bangumi.utils import common_util


def get_person_soup(bangumi_person_id):
    person_url = url_constants.get_person_url(bangumi_person_id)
    headers = url_constants.get_user_headers()

    time.sleep(random.uniform(0.2, 0.5))
    Flag = True
    while Flag:
        try:
            Flag = False
            response = requests.get(person_url, headers=headers)
        except Exception:
            print(traceback.format_exc())
            Flag = True

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    return soup


def get_person(bangumi_person_id):

    person_dto = basic_person_dto.BasicPersonDTO()
    soup = get_person_soup(bangumi_person_id)

    name = soup.select("#headerSubject > h1 > a")[0].get_text()
    person_dto.name = name

    contents = soup.select("#infobox > li")
    for content in contents:
        con = content.get_text().split(":")
        # print(con)
        column = con[0]
        data = con[1].replace(' ', '')
        if column == "简体中文名":
            person_dto.chinese_name = data
        elif column == "别名":
            person_dto.alias = data if person_dto.alias == None else person_dto.alias+"|"+data
        elif column == "性别":
            if data == '男':
                person_dto.sex = table_constants.MALE
            elif data == '女':
                person_dto.sex = table_constants.FEMALE
            else:
                person_dto.sex = table_constants.UNKNOW
        elif column == "生日":
            person_dto.birthday = common_util.format_YYMMDD(data)
        elif column == '血型':
            person_dto.blood_type = data
        elif column == '身高':
            person_dto.height = int(data.replace('cm', ''))
        elif column == '出生地':
            person_dto.homeplace = data
        elif column == '教育程度':
            person_dto.education = data
        elif column == '星座':
            person_dto.constellation = data
        elif column == '兴趣':
            person_dto.interest = data
        elif column == '特技':
            person_dto.special_skill = data
        elif column == '家人':
            person_dto.family = data
        elif column == '公认荣誉':
            person_dto.recognized_honor = data
        else:
            if person_dto.extends is None:
                person_dto.extends = column+"="+data
            else:
                person_dto.extends = person_dto.extends + "|"+column+"="+data

    return person_dto

if __name__ == "__main__":
    person_dto = get_person(1)
    print(person_dto)

