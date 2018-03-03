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


def get_person_by_soup(id, soup):
    person_dto = basic_person_dto.BasicPersonDTO()

    names = soup.select("#headerSubject > h1 > a")
    name = names[0].get_text()
    if name is None or len(name) <= 0:
        return None
    person_dto.name = name
    person_dto.bangumi_person_id = id

    professions_temp = soup.select("#columnCrtB > div.clearit > h2")[0].get_text().split(":")[1].split(" ")
    professions = ''
    for profession in professions_temp:
        if profession == "" or profession == '\n':
            continue
        professions = profession if professions == '' else professions + "|"+profession
    person_dto.profession = professions

    picture_src = soup.select("#columnCrtA > div.infobox > div > a > img")
    if picture_src is not None and len(picture_src) > 0:
        person_dto.picture = picture_src[0].get("src")

    intros = soup.select("#columnCrtB > div.detail")
    if intros is not None and len(intros) > 0:
        person_dto.intro = intros[0].get_text()

    contents = soup.select("#infobox > li")
    for content in contents:
        con = content.get_text().split(":", 1)
        # print(con)
        column = con[0]
        data = con[1].replace(' ', '')
        if column == "简体中文名":
            person_dto.chinese_name = data
        elif column == "别名":
            person_dto.alias = data if person_dto.alias is None else person_dto.alias+"|"+data
        elif column == "性别":
            if data == '男':
                person_dto.sex = table_constants.MALE
            elif data == '女':
                person_dto.sex = table_constants.FEMALE

        elif column == "生日":
            # person_dto.birthday = str(common_util.format_YYMMDD(data))
            person_dto.birthday = data
        elif column == '血型':
            person_dto.blood_type = data
        elif column == '身高':
            person_dto.height = data[0:3]
        elif column == '出生地':
            person_dto.homeplace = data
        elif column == '教育程度':
            person_dto.education = data
        elif column == '星座':
            person_dto.constellation = data
        elif column == '兴趣':
            person_dto.interest = data
        elif '特技' in column:
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
    for x in range(1, 100000):
        person_soup = get_person_soup(x)
        person_dto = get_person_by_soup(person_soup)
        # dto_json = json.dumps(person_dto, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        if person_dto.extends is not None:
            print(x, person_dto.name, person_dto.profession, person_dto.extends)

