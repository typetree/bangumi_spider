# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants import table_constants
from bangumi.spider import subject_detail_anime_spider, subject_detail_book_spider, \
    subject_detail_music_spider, subject_detail_game_spider, subject_detail_real_spider


def get_subject_detail_spider_by_category(category):
    if category == table_constants.ANIME:
        return subject_detail_anime_spider.get_anime_dto_by_soup
    elif category == table_constants.BOOK:
        return subject_detail_book_spider.get_book_dto_by_soup
    elif category == table_constants.MUSIC:
        return subject_detail_music_spider.get_music_dto_by_soup
    elif category == table_constants.GAME:
        return subject_detail_game_spider.get_game_dto_by_soup
    elif category == table_constants.REAL:
        return subject_detail_real_spider.get_real_dto_by_soup
    else:
        return None