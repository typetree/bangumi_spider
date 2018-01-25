# *_*coding:utf-8 *_*
# author: hoicai
from bs4 import BeautifulSoup
import requests
from bangumi.constants.url_constants import get_user_url, get_user_headers

user_url = get_user_url('gmxcmm')
headers = get_user_headers()

response = requests.get(user_url, headers = headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
print(soup)

user_name = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > a')[0].get_text()
user_code = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > small')[0].get_text()[1:]
user_join_time = soup.select('span.tip')[0].get_text().split(' ')[0]

user_intro = soup.select('div.bio')[0].get_text()

user_anime = soup.select('#anime > div.horizontalOptions.clearit > ul > li')
for user_anime_list in user_anime:
    user_name_message = user_anime_list.get_text()

    user_anime_do = user_name_message.split("部")[0] if '在看' in user_name_message else None

    user_anime_collect = user_name_message.split("部")[0] if '看过' in user_name_message else None

    user_anime_wish = user_name_message.split("部")[0] if '想看' in user_name_message else None

    user_anime_on_hold = user_name_message.split("部")[0] if '搁置' in user_name_message else None

    user_anime_dropped = user_name_message.split("部")[0] if '抛弃' in user_name_message else None


user_game = soup.select('#game > div.horizontalOptions.clearit > ul > li')
for user_game_list in user_game:
    user_name_message = user_game_list.get_text()
    if '在玩' in user_name_message:
        user_game_do = user_name_message.split("部")[0]
    if '玩过' in user_name_message:
        user_game_collect = user_name_message.split("部")[0]
    if '想玩' in user_name_message:
        user_game_wish = user_name_message.split("部")[0]
    if '搁置' in user_name_message:
        user_game_on_hold = user_name_message.split("部")[0]
    if '抛弃' in user_name_message:
        user_game_dropped = user_name_message.split("部")[0]

print(user_name,user_code,user_join_time,user_intro)
print(user_anime_do,user_anime_collect,user_anime_wish,user_anime_on_hold,user_anime_dropped)
print(user_game_do,user_game_collect,user_game_wish,user_game_on_hold,user_game_dropped)

