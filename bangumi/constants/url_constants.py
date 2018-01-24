# *_*coding:utf-8 *_*
# author: hoicai

# 收藏的角色
CHANNEL_MONO_CHARACTER = '/mono/character'
# 收藏的人物
CHANNEL_MONO_PERSN = '/mono/person'
# 人物
CHANNEL_MONO = '/mono'
# 日志
CHANNEL_BLOG = '/blog'
# 目录
CHANNEL_INDEX = '/index'
# 时间胶囊
CHANNEL_TIMELINE = '/timeline'
# 小组
CHANNEL_GROUPS = '/groups'
# 好友
CHANNEL_FRIENDS = '/friends'
# 维基
CHANNEL_WIKI = '/wiki'
# 天窗
CHANNEL_DOUJIN = '/doujin'



def get_user_url(user_code, channel=""):
    user_url = 'http://bangumi.tv/user/{}{}'.format(user_code,channel)
    return user_url


def get_user_headers(user_code):
    headers = {
        'Referer': 'http://bangumi.tv/user/{}/groups'.format(user_code),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    return headers
