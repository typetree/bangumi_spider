# *_*coding:utf-8 *_*
# author: hoicai
import traceback

from bangumi.dto import subject_detail_book_dto
from bangumi.spider import subject_info_spider


def set_subject_book_dto(left_part, right_part, book_dto:subject_detail_book_dto):
    if left_part == '中文名':
        book_dto.chinese_name = right_part if book_dto.chinese_name is None else book_dto.chinese_name +"|"+right_part
    elif left_part == '别名':
        book_dto.alias = right_part if book_dto.alias is None else book_dto.alias +"|"+right_part
    elif left_part == '价格':
        book_dto.price = right_part if book_dto.price is None else book_dto.price +"|"+right_part
    elif left_part == '发售日':
        book_dto.sale_date = right_part if book_dto.sale_date is None else book_dto.sale_date +"|"+right_part
    elif left_part == '页数':
        book_dto.page_num = right_part if book_dto.page_num is None else book_dto.page_num +"|"+right_part
    elif left_part == '话数':
        book_dto.topic_num = right_part if book_dto.topic_num is None else book_dto.topic_num +"|"+right_part
    elif left_part == 'ISBN':
        book_dto.ISBN = right_part if book_dto.ISBN is None else book_dto.ISBN +"|"+right_part
    else:
        book_dto.extends = left_part+"="+right_part if book_dto.extends is None else book_dto.extends +"|"+left_part+"="+right_part
    return book_dto


def get_book_dto_by_soup(soup, data, subject_profession_person_queue, profession_dicts):

    bangumi_subject_id = data['bangumi_subject_id']
    name = data['name']
    category = data['category']
    type = data['type']

    picture = subject_info_spider.get_picture_by_soup(soup)
    intro = subject_info_spider.get_intro_by_soup(soup)

    try:
        book_dto = subject_info_spider.get_detail_dto_by_category(category, soup, subject_profession_person_queue, profession_dicts)
    except Exception:
        traceback.format_exc()

    book_dto.bangumi_subject_id = bangumi_subject_id
    book_dto.name = name
    book_dto.type = type
    book_dto.picture = picture
    book_dto.intro = intro

    return book_dto