# *_*coding:utf-8 *_*
# author: hoicai
import traceback

from bangumi.dto import subject_detail_game_dto
from bangumi.spider import subject_info_spider


def set_subject_game_dto(left_part, right_part, game_dto:subject_detail_game_dto):
    if left_part == '中文名':
        game_dto.chinese_name = right_part if game_dto.chinese_name is None else game_dto.chinese_name +"|"+right_part
    elif left_part == '别名':
        game_dto.alias = right_part if game_dto.alias is None else game_dto.alias +"|"+right_part
    elif left_part == '平台':
        game_dto.platform = right_part if game_dto.platform is None else game_dto.platform +"|"+right_part
    elif left_part == '游戏类型':
        game_dto.game_type = right_part if game_dto.game_type is None else game_dto.game_type +"|"+right_part
    elif left_part == '游戏引擎':
        game_dto.game_engine = right_part if game_dto.game_engine is None else game_dto.game_engine +"|"+right_part
    elif left_part == '游玩人数':
        game_dto.player_num = right_part if game_dto.player_num is None else game_dto.player_num +"|"+right_part
    elif left_part == '发行日期':
        game_dto.sale_date = right_part if game_dto.sale_date is None else game_dto.sale_date +"|"+right_part
    elif left_part == '售价':
        game_dto.price = right_part if game_dto.price is None else game_dto.price +"|"+right_part
    elif left_part == 'website':
        game_dto.website = right_part if game_dto.website is None else game_dto.website +"|"+right_part
    else:
        game_dto.extends = left_part+"="+right_part if game_dto.extends is None else game_dto.extends +"|"+left_part+"="+right_part
    return game_dto


def get_game_dto_by_soup(soup, data, subject_profession_person_queue, profession_dicts):

    bangumi_subject_id = data['bangumi_subject_id']
    name = data['name']
    category = data['category']
    type = data['type']

    picture = subject_info_spider.get_picture_by_soup(soup)
    intro = subject_info_spider.get_intro_by_soup(soup)

    game_dto = subject_info_spider.get_detail_dto_by_category(category, soup, subject_profession_person_queue, profession_dicts)

    game_dto.bangumi_subject_id = bangumi_subject_id
    game_dto.name = name
    game_dto.type = type
    game_dto.picture = picture
    game_dto.intro = intro

    return game_dto