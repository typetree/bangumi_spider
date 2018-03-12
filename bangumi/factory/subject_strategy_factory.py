# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.dto import subject_detail_anime_dto, subject_detail_book_dto, subject_detail_music_dto, \
    subject_detail_game_dto, subject_detail_real_dto
from bangumi.spider import subject_detail_anime_spider, subject_detail_book_spider, \
    subject_detail_music_spider, subject_detail_game_spider, subject_detail_real_spider


def get_subject_detail_spider_by_category(category):
    if category == 'ANIME':
        return subject_detail_anime_spider.get_anime_dto_by_soup
    elif category == 'BOOK':
        return subject_detail_book_spider.get_book_dto_by_soup
    elif category == 'MUSIC':
        return subject_detail_music_spider.get_music_dto_by_soup
    elif category == 'GAME':
        return subject_detail_game_spider.get_game_dto_by_soup
    elif category == 'REAL':
        return subject_detail_real_spider.get_real_dto_by_soup
    else:
        return None


def get_subject_dto_by_category(category):
    if category == 'ANIME':
        return subject_detail_anime_dto.SubjectDetailAnimeDTO()
    if category == 'BOOK':
        return subject_detail_book_dto.SubjectDetailBookDTO()
    if category == 'MUSIC':
        return subject_detail_music_dto.SubjectDetailMusicDTO()
    if category == 'GAME':
        return subject_detail_game_dto.SubjectDetailGameDTO()
    if category == 'REAL':
        return subject_detail_real_dto.SubjectDetailRealDTO()
    else:
        return None


def set_subject_dto_by_category(category):
    if category == 'ANIME':
        return subject_detail_anime_spider.set_subject_anime_dto
    if category == 'BOOK':
        return subject_detail_book_spider.set_subject_book_dto
    if category == 'GAME':
        return subject_detail_game_spider.set_subject_game_dto
    if category == 'MUSIC':
        return subject_detail_music_spider.set_subject_music_dto
    if category == 'REAL':
        return subject_detail_real_spider.set_subject_real_dto
    return None