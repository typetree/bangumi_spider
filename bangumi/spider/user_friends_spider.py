# *_*coding:utf-8 *_*
# author: hoicai
import random
import time
from bs4 import BeautifulSoup
import requests

from ..constants import url_constants
from ..dto import user_info_dto


def find_friends(USER_CODE):
    user_url = url_constants.get_user_url(USER_CODE, url_constants.CHANNEL_FRIENDS)
    user_hearders = url_constants.get_friends_headers()

    time.sleep(random.uniform(0.2, 0.5))
    Flag = True
    while Flag:
        try:
            Flag = False
            response = requests.get(user_url, headers=user_hearders)
        except Exception as e:
            print(e)
            Flag = True

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)


    photo_styles = soup.select("#memberUserList > li > div > strong > a > span > img")

    user_names = soup.select('#memberUserList > li > div > strong > a')
    user_codes = soup.select('#memberUserList > li > div > strong > a')

    data = [];
    for user_code, user_name, photo_style in zip(user_codes, user_names, photo_styles):
        userInfoDTO = user_info_dto.UserInfoDTO()

        userInfoDTO.code = str(user_code.get('href')[6:])
        if userInfoDTO.code == '':
            continue

        userInfoDTO.name = user_name.get_text().split(" ")[1]

        photo_style = photo_style.get('src')
        user_profile_photo = photo_style[photo_style.find("'")+1: photo_style.rfind("'")]
        user_bangumi_user_id = user_profile_photo[user_profile_photo.rfind("/")+1: user_profile_photo.rfind(".")]
        if user_bangumi_user_id == 'icon':
            user_bangumi_user_id = userInfoDTO.code
        userInfoDTO.bangumi_user_id = user_bangumi_user_id

        data.append(userInfoDTO)
    return data


if __name__ == '__main__':

    user_found = []  # 记录已查找的用户code
    user_dict = {'zisudaki': '植树淡季'}  # 记录用户code,name


    def find(USER_CODE):

        friends = find_friends(USER_CODE)
        user_found.append(USER_CODE)
        for friend in friends:
            if friend['user_code'] not in user_dict:
                user_dict[friend['user_code']] = friend['user_name']

        print('用户:{},名称:{},好友数:{},好友列表:{}'.format(
            USER_CODE,
            user_dict[USER_CODE],
            len(friends),
            [friend['user_name'] for friend in friends if friend]))
        return [friend['user_code'] for friend in friends if friend]


    def infinity(USER_CODE):

        if USER_CODE in user_found:
            return False

        user_codes = find(USER_CODE)
        for user_code in user_codes:
            flag = infinity(user_code)
            if flag:
                continue


    infinity('zisudaki')
