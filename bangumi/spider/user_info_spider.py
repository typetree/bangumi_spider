# *_*coding:utf-8 *_*
# author: hoicai
import random
import time
import traceback

from bs4 import BeautifulSoup
import requests

from ..dto import user_info_dto
from ..utils import my_exception
from ..constants import url_constants


def get_user_soup(UserCode):
    user_url = url_constants.get_user_url(UserCode)
    headers = url_constants.get_user_headers()

    time.sleep(random.uniform(0.2, 0.5))
    Flag = True
    while Flag:
        try:
            Flag = False
            response = requests.get(user_url, headers=headers)
        except Exception:
            print(traceback.format_exc())
            Flag = True

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    return soup


def get_user_info(bangumi_user_id):
    soup = get_user_soup(bangumi_user_id)
    user_name_list = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > a')

    if len(user_name_list) == 0:
        raise my_exception.BreakException("user_info is not found, bangumi_user_id:{}".format(bangumi_user_id))

    user_name = user_name_list[0].get_text()
    user_code = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > small')[
                    0].get_text()[1:]

    photo_style = soup.select("#headerProfile > div > div.headerContainer > h1 > div.headerAvatar > a > span")[0]\
        .get("style")
    user_profile_photo = photo_style[photo_style.find("'")+1: photo_style.rfind("'")]

    # user_bangumi_user_id = user_profile_photo[user_profile_photo.rfind("/")+1: user_profile_photo.rfind(".")]
    # if user_bangumi_user_id == 'icon':
    #     user_bangumi_user_id = UserCode

    # 改名用户不抛异常。
    # if user_code != UserCode and user_bangumi_user_id != UserCode:
    #     raise my_exception.MyException("spider user homepage is fail,user_code({}) != UserCode({})"
    #                                    .format(user_code, UserCode))

    user_join_time = soup.select('span.tip')[0].get_text().split(' ')[0]

    user_intro_content = soup.select('div.bio')
    user_intro = ""
    if len(user_intro_content) != 0:
        user_intro = user_intro_content[0].get_text()

    user_anime = soup.select('#anime > div.horizontalOptions.clearit > ul > li')

    user_anime_do = 0
    user_anime_collect = 0
    user_anime_wish = 0
    user_anime_on_hold = 0
    user_anime_dropped = 0

    for user_anime_list in user_anime:
        if user_anime_list == user_anime[0]:
            continue
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

    user_game_do = 0
    user_game_collect = 0
    user_game_wish = 0
    user_game_on_hold = 0
    user_game_dropped = 0

    user_game = soup.select('#game > div.horizontalOptions.clearit > ul > li')
    for user_game_list in user_game:
        if user_game_list == user_game[0]:
            continue
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

    user_book_do = 0
    user_book_collect = 0
    user_book_wish = 0
    user_book_on_hold = 0
    user_book_dropped = 0

    user_book = soup.select('#book > div.horizontalOptions.clearit > ul > li')
    for user_book_list in user_book:
        if user_book_list == user_book[0]:
            continue
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

    user_real_do = 0
    user_real_collect = 0
    user_real_wish = 0
    user_real_on_hold = 0
    user_real_dropped = 0

    user_real = soup.select('#real > div.horizontalOptions.clearit > ul > li')
    for user_real_list in user_real:
        if user_real_list == user_real[0]:
            continue
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
        temp = group_num_content[0].get_text().split(user_name)[1]
        if len(temp) >= 7:
            group_num = int(temp[7:-1])

    uid = user_info_dto.UserInfoDTO()
    
    uid.name = user_name
    uid.code = user_code
    uid.profile_photo = user_profile_photo
    # uid.bangumi_user_id = user_bangumi_user_id
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