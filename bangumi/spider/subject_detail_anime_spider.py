# *_*coding:utf-8 *_*
# author: hoicai
import traceback
from multiprocessing import Queue

from bangumi.client import mysql_client
from bangumi.dto import subject_detail_anime_dto, subject_profession_person_dto
from bangumi.service import basic_profession_service
from bangumi.spider import subject_info_spider
from bangumi.utils import common_util



def set_subject_anime_dto(left_part, right_part, anime_dto:subject_detail_anime_dto):
    if left_part == '中文名':
        anime_dto.chinese_name = right_part if anime_dto.chinese_name is None else anime_dto.chinese_name +"|"+right_part
    elif left_part == '别名':
        anime_dto.alias = right_part if anime_dto.alias is None else anime_dto.alias +"|"+right_part
    elif left_part == '上映年度':
        anime_dto.release_date = right_part if anime_dto.release_date is None else anime_dto.release_date +"|"+right_part
    elif left_part == '片长':
        anime_dto.time_length = right_part if anime_dto.time_length is None else anime_dto.time_length +"|"+right_part
    elif left_part == '官方网站':
        anime_dto.official_website = right_part if anime_dto.official_website is None else anime_dto.official_website +"|"+right_part
    elif left_part == 'Copyright':
        anime_dto.copyright = right_part if anime_dto.copyright is None else anime_dto.copyright +"|"+right_part
    elif left_part == '话数':
        anime_dto.topic_length = right_part
    elif left_part == '放送开始':
        anime_dto.release_date = right_part if anime_dto.release_date is None else anime_dto.release_date +"|"+right_part
    elif left_part == '放送星期':
        anime_dto.send_out_week = right_part if anime_dto.send_out_week is None else anime_dto.send_out_week +"|"+right_part
    elif left_part == '播放电视台':
        anime_dto.TV_station = right_part if anime_dto.TV_station is None else anime_dto.TV_station +"|"+right_part
    elif left_part == '其他电视台':
        anime_dto.TV_station = right_part if anime_dto.TV_station is None else anime_dto.TV_station +"|"+right_part
    elif left_part == '播放结束':
        anime_dto.end_date = right_part if anime_dto.end_date is None else anime_dto.end_date +"|"+right_part
    elif left_part == '发售日':
        anime_dto.sale_date = right_part if anime_dto.sale_date is None else anime_dto.sale_date +"|"+right_part
    else:
        anime_dto.extends = left_part+"="+right_part if anime_dto.extends is None else anime_dto.extends +"|"+left_part+"="+right_part
    return anime_dto


def get_anime_dto_by_soup(soup, data, subject_profession_person_queue, profession_dicts):

    bangumi_subject_id = data['bangumi_subject_id']
    name = data['name']
    category = data['category']
    type = data['type']

    picture = subject_info_spider.get_picture_by_soup(soup)
    intro = subject_info_spider.get_intro_by_soup(soup)

    anime_dto = subject_info_spider.get_detail_dto_by_category(category, soup, subject_profession_person_queue, profession_dicts)

    anime_dto.bangumi_subject_id = bangumi_subject_id
    anime_dto.name = name
    anime_dto.type = type
    anime_dto.picture = picture
    anime_dto.intro = intro

    return anime_dto


if __name__ == '__main__':

    conn = mysql_client.get_connect()
    profession_dicts = basic_profession_service.find_dict_by_category(conn, 'ANIME')
    conn.close()

    bangumi_profession_person_queue = Queue()

    for i in range(50, 10000):
        soup = subject_info_spider.get_subject_soup(i)
        category = subject_info_spider.get_category_by_soup(soup)
        bangumi_subject_id = subject_info_spider.get_bangumi_id_by_soup(soup)
        if category == 'ANIME':
            anime_dto = get_infomation(soup, bangumi_profession_person_queue, profession_dicts)
            anime_dto.bangumi_subject_id = bangumi_subject_id
            print(common_util.object_to_json(anime_dto))
