# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.dto import subject_detail_music_dto
from bangumi.spider import subject_info_spider


def set_subject_music_dto(left_part, right_part, music_dto:subject_detail_music_dto):
    if left_part == '中文名':
        music_dto.chinese_name = right_part if music_dto.chinese_name is None else music_dto.chinese_name +"|"+right_part
    elif left_part == '别名':
        music_dto.alias = right_part if music_dto.alias is None else music_dto.alias +"|"+right_part
    elif left_part == '版本特性':
        music_dto.version_feature = right_part if music_dto.version_feature is None else music_dto.version_feature +"|"+right_part
    elif left_part == '发售日期':
        music_dto.sale_date = right_part if music_dto.sale_date is None else music_dto.sale_date +"|"+right_part
    elif left_part == '价格':
        music_dto.price = right_part if music_dto.price is None else music_dto.price +"|"+right_part
    elif left_part == '播放时长':
        music_dto.time_length = right_part if music_dto.time_length is None else music_dto.time_length +"|"+right_part
    elif left_part == '碟片数量':
        music_dto.discs_num = right_part if music_dto.discs_num is None else music_dto.discs_num +"|"+right_part
    else:
        music_dto.extends = left_part+"="+right_part if music_dto.extends is None else music_dto.extends +"|"+left_part+"="+right_part
    return music_dto


def get_music_dto_by_soup(soup, data, subject_profession_person_queue, profession_dicts):

    bangumi_subject_id = data['bangumi_subject_id']
    name = data['name']
    category = data['category']
    type = data['type']

    picture = subject_info_spider.get_picture_by_soup(soup)
    intro = subject_info_spider.get_intro_by_soup(soup)

    music_dto = subject_info_spider.get_detail_dto_by_category(category, soup, subject_profession_person_queue, profession_dicts)

    music_dto.bangumi_subject_id = bangumi_subject_id
    music_dto.name = name
    music_dto.type = type
    music_dto.picture = picture
    music_dto.intro = intro

    return music_dto