# *_*coding:utf-8 *_*
# author: hoicai
import time
from bs4 import BeautifulSoup
import requests

from bangumi.constants import url_constants

user_code = 'zisudaki'


def find_friends(USER_CODE):
    user_url = url_constants.get_user_url(USER_CODE, url_constants.CHANNEL_FRIENDS)
    user_hearders = url_constants.get_user_headers(USER_CODE)

    time.sleep(0.2)
    response = requests.get(user_url, headers=user_hearders)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    owner_name = soup.select('#headerProfile > div > div.headerContainer > h1 > div.inner > a')

    user_names = soup.select('#memberUserList > li > div > strong > a')
    user_codes = soup.select('#memberUserList > li > div > strong > a')

    data = [];
    for user_code, user_name in zip(user_codes, user_names):
        info = {
            'user_code': user_code.get('href')[6:],
            'user_name': user_name.get_text().split(" ")[1]
        }
        data.append(info)
    return data

if __name__ == '__main__':

    user_list = []
    def find(USER_CODE):
        friends = find_friends(USER_CODE)
        # user_list.extend(friends)
        owner = [user['user_name'] for user in user_list if USER_CODE == user['user_code']]
        print('用户:{},好友数:{},好友列表:{}'.format(
            owner[0],
            len(friends),
            [friend['user_name'] for friend in friends if friend ]))
        return [friend['user_code'] for friend in friends if friend ]

    def infinity(USER_CODE):
        user_codes = [user['user_code'] for user in user_list if user ]
        if USER_CODE in user_codes:
            return False
        else:
            user_list.append(USER_CODE)
        user_codes = find(USER_CODE)
        for user_code in user_codes:
            flag = infinity(user_code)
            if flag:
                continue


    infinity('zisudaki')
