# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.dto import subject_detail_real_dto
from bangumi.spider import subject_info_spider


def set_subject_real_dto(left_part, right_part, real_dto:subject_detail_real_dto):
    if left_part == '中文名':
        real_dto.chinese_name = right_part if real_dto.chinese_name is None else real_dto.chinese_name +"|"+right_part
    elif left_part == '别名':
        real_dto.alias = right_part if real_dto.alias is None else real_dto.alias +"|"+right_part
    elif left_part == '集数':
        real_dto.topic_num = right_part if real_dto.topic_num is None else real_dto.topic_num +"|"+right_part
    elif left_part == '放送星期':
        real_dto.send_out_week = right_part if real_dto.send_out_week is None else real_dto.send_out_week +"|"+right_part
    elif left_part == '开始':
        real_dto.release_date = right_part if real_dto.release_date is None else real_dto.release_date +"|"+right_part
    elif left_part == '结束':
        real_dto.end_date = right_part if real_dto.end_date is None else real_dto.end_date +"|"+right_part
    elif left_part == '类型':
        real_dto.real_type = right_part if real_dto.real_type is None else real_dto.real_type +"|"+right_part
    elif left_part == '国家/地区':
        real_dto.region = right_part if real_dto.region is None else real_dto.region +"|"+right_part
    elif left_part == '语言':
        real_dto.language = right_part if real_dto.language is None else real_dto.language +"|"+right_part
    elif left_part == '每集长':
        real_dto.time_length = right_part if real_dto.time_length is None else real_dto.time_length +"|"+right_part
    elif left_part == '频道':
        real_dto.channel = right_part if real_dto.channel is None else real_dto.channel +"|"+right_part
    elif left_part == '电视网':
        real_dto.tv_network = right_part if real_dto.tv_network is None else real_dto.tv_network +"|"+right_part
    elif left_part == '电视台':
        real_dto.tv_station = right_part if real_dto.tv_station is None else real_dto.tv_station +"|"+right_part
    elif left_part == '视频制式':
        real_dto.discs_num = right_part if real_dto.discs_num is None else real_dto.discs_num +"|"+right_part
    elif left_part == '音频制式':
        real_dto.audio_standard = right_part if real_dto.audio_standard is None else real_dto.audio_standard +"|"+right_part
    elif left_part == '首播国家':
        real_dto.premiere_country = right_part if real_dto.premiere_country is None else real_dto.premiere_country +"|"+right_part
    elif left_part == '首播地区':
        real_dto.premiere_region = right_part if real_dto.premiere_region is None else real_dto.premiere_region +"|"+right_part
    elif left_part == '台湾名称':
        real_dto.taiwan_name = right_part if real_dto.taiwan_name is None else real_dto.taiwan_name +"|"+right_part
    elif left_part == '港澳名称':
        real_dto.hk_name = right_part if real_dto.hk_name is None else real_dto.hk_name +"|"+right_part
    elif left_part == '马新名称':
        real_dto.south_asia_name = right_part if real_dto.south_asia_name is None else real_dto.south_asia_name +"|"+right_part
    elif left_part == '官方网站':
        real_dto.website = right_part if real_dto.website is None else real_dto.website +"|"+right_part
    elif left_part == 'imdb_id':
        real_dto.imdb_id = right_part if real_dto.imdb_id is None else real_dto.imdb_id +"|"+right_part
    elif left_part == 'tv_com_id':
        real_dto.tv_com_id = right_part if real_dto.tv_com_id is None else real_dto.tv_com_id +"|"+right_part
    else:
        real_dto.extends = left_part+"="+right_part if real_dto.extends is None else real_dto.extends +"|"+left_part+"="+right_part
    return real_dto


def get_real_dto_by_soup(soup, data, subject_profession_person_queue, profession_dicts):

    bangumi_subject_id = data['bangumi_subject_id']
    name = data['name']
    category = data['category']
    type = data['type']

    picture = subject_info_spider.get_picture_by_soup(soup)
    intro = subject_info_spider.get_intro_by_soup(soup)

    real_dto = subject_info_spider.get_detail_dto_by_category(category, soup, subject_profession_person_queue, profession_dicts)

    real_dto.bangumi_subject_id = bangumi_subject_id
    real_dto.name = name
    real_dto.type = type
    real_dto.picture = picture
    real_dto.intro = intro

    return real_dto