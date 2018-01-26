# *_*coding:utf-8 *_*
# author: hoicai
from bs4 import BeautifulSoup
import requests
from cryptography.hazmat.primitives.hashes import MD5

from bangumi.constants.url_constants import get_user_url, get_user_headers


def get_user_soup(UserCode):
    user_url = get_user_url(UserCode)
    headers = get_user_headers()

    response = requests.get(user_url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    return soup

soup = get_user_soup('venusxx')
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

group_num = soup.select("#group > div.horizontalOptions.clearit > ul > li.title > h2")[0].get_text().split(user_name)[1][7:-1]

user = {
    "name": user_name,
    "code": user_code,
    "join_time": user_join_time,
    "intro": user_intro,
    "anime_do": user_anime_do,
    "anime_collect": user_anime_collect,
    "anime_wish": user_anime_wish,
    "anime_on_hold": user_anime_on_hold,
    "anime_dropped": user_anime_dropped,
    "game_do": user_game_do,
    "game_collect": user_game_collect,
    "game_wish": user_game_wish,
    "game_on_hold": user_game_on_hold,
    "game_dropped": user_game_dropped,
    "book_do": user_book_do,
    "book_collect": user_book_collect,
    "book_wish": user_book_wish,
    "book_on_hold": user_book_on_hold,
    "book_dropped": user_book_dropped,
    "real_do": user_real_do,
    "real_collect": user_real_collect,
    "real_wish": user_real_wish,
    "real_on_hold": user_real_on_hold,
    "real_dropped": user_real_dropped,
    "group_num": group_num,
}

