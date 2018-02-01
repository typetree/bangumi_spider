# *_*coding:utf-8 *_*
# author: hoicai
from bs4 import BeautifulSoup
import requests

from bangumi.dto import user_info_dto
from ..constants import url_constants


def get_user_soup(UserCode):
    user_url = url_constants.get_user_url(UserCode)
    headers = url_constants.get_user_headers()

    response = requests.get(user_url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    return soup


def get_user_info(UserCode):
    soup = get_user_soup(UserCode)
    user_name = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > a')[
        0].get_text()
    user_code = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > small')[
                    0].get_text()[1:]
    user_join_time = soup.select('span.tip')[0].get_text().split(' ')[0]

    user_intro = soup.select('div.bio')[0].get_text()

    user_anime = soup.select('#anime > div.horizontalOptions.clearit > ul > li')

    user_anime_do = None
    user_anime_collect = None
    user_anime_wish = None
    user_anime_on_hold = None
    user_anime_dropped = None

    for user_anime_list in user_anime:
        user_anime_message = user_anime_list.get_text()

        if '在看' in user_anime_message:
            user_anime_do = user_anime_message.split("部")[0]

        if '看过' in user_anime_message:
            user_anime_collect = user_anime_message.split("部")[0]

        if '想看' in user_anime_message:
            user_anime_wish = user_anime_message.split("部")[0]

        if '搁置' in user_anime_message:
            user_anime_on_hold = user_anime_message.split("部")[0]

        if '抛弃' in user_anime_message:
            user_anime_dropped = user_anime_message.split("部")[0]

    user_game_do = None
    user_game_collect = None
    user_game_wish = None
    user_game_on_hold = None
    user_game_dropped = None

    user_game = soup.select('#game > div.horizontalOptions.clearit > ul > li')
    for user_game_list in user_game:
        user_game_message = user_game_list.get_text()
        if '在玩' in user_game_message:
            user_game_do = user_game_message.split("部")[0]

        if '玩过' in user_game_message:
            user_game_collect = user_game_message.split("部")[0]

        if '想玩' in user_game_message:
            user_game_wish = user_game_message.split("部")[0]

        if '搁置' in user_game_message:
            user_game_on_hold = user_game_message.split("部")[0]

        if '抛弃' in user_game_message:
            user_game_dropped = user_game_message.split("部")[0]

    user_book_do = None
    user_book_collect = None
    user_book_wish = None
    user_book_on_hold = None
    user_book_dropped = None

    user_book = soup.select('#book > div.horizontalOptions.clearit > ul > li')
    for user_book_list in user_book:
        user_book_message = user_book_list.get_text()
        if '在读' in user_book_message:
            user_book_do = user_book_message.split("本")[0]

        if '读过' in user_book_message:
            user_book_collect = user_book_message.split("本")[0]

        if '想读' in user_book_message:
            user_book_wish = user_book_message.split("本")[0]

        if '搁置' in user_book_message:
            user_book_on_hold = user_book_message.split("本")[0]

        if '抛弃' in user_book_message:
            user_book_dropped = user_book_message.split("本")[0]

    user_real_do = None
    user_real_collect = None
    user_real_wish = None
    user_real_on_hold = None
    user_real_dropped = None

    user_real = soup.select('#real > div.horizontalOptions.clearit > ul > li')
    for user_real_list in user_real:
        user_real_message = user_real_list.get_text()
        if '在看' in user_real_message:
            user_real_do = user_real_message.split("部")[0]

        if '看过' in user_real_message:
            user_real_collect = user_real_message.split("部")[0]

        if '想看' in user_real_message:
            user_real_wish = user_real_message.split("部")[0]

        if '搁置' in user_real_message:
            user_real_on_hold = user_real_message.split("部")[0]

        if '抛弃' in user_real_message:
            user_real_dropped = user_real_message.split("部")[0]

    group_num_content = soup.select("#group > div.horizontalOptions.clearit > ul > li.title > h2")
    group_num = 0
    if len(group_num_content) != 0:
        group_num = int(group_num_content[0].get_text().split(user_name)[1][7:-1])

    uid = user_info_dto.UserInfoDTO()
    
    uid.name = user_name
    uid.code = user_code
    uid.join_time = user_join_time
    uid.intro = user_intro
    uid.anime_do = user_anime_do
    uid.anime_collect = user_anime_collect
    uid.anime_wish = user_anime_wish
    uid.anime_on_hold = user_anime_on_hold
    uid.anime_dropped = user_anime_dropped
    uid.game_do = user_game_do
    uid.game_collect = user_game_collect
    uid.game_wish = user_game_wish
    uid.game_on_hold = user_game_on_hold
    uid.game_dropped = user_game_dropped
    uid.book_do = user_book_do
    uid.book_collect = user_book_collect
    uid.book_wish = user_book_wish
    uid.book_on_hold = user_book_on_hold
    uid.book_dropped = user_book_dropped
    uid.real_do = user_real_do
    uid.real_collect = user_real_collect
    uid.real_wish = user_real_wish
    uid.real_on_hold = user_real_on_hold
    uid.real_dropped = user_real_dropped
    uid.group_num = group_num
 
    return uid