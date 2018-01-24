# *_*coding:utf-8 *_*
# author: hoicai

def get_user_url(user_code):
    user_url = 'http://bangumi.tv/user/{}'.format(user_code)
    return user_url


def get_user_headers(user_code):
    headers = {
        'Referer': 'http://bangumi.tv/user/{}/groups'.format(user_code),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    return headers
