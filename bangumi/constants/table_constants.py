# *_*coding:utf-8 *_*
# author: hoicai

# 用户
SPIDER_SYSTEM = 'SPIDER_SYSTEM'

# 状态    爬虫中=DOING ,完成=FINISH

SPIDER_VERSION_STATUS_DOING = 'DOING'
SPIDER_VERSION_STATUS_FINISH = 'FINISH'


# ENABLE=可用,UNABLE=不可用
ENABLE = 'ENABLE'
UNABLE = 'UNABLE'


# 分类
CATEGORY_USER = 'USER'

# 表名
TABLE_SPIDER_VERSION = 'spider_version'
TABLE_USER_FRIENDS = 'user_friends'
TABLE_USER_INFO = 'user_info'
TABLE_USER_SPIDER_VERSION = 'user_spider_version'


# 人物
# 性别

UNKNOW = 'UNKNOW'
FEMALE = 'FEMALE'
MALE = 'MALE'


# 项目
# category
MUSIC = '音乐'
BOOK = '书籍'
GAME = '游戏'
ANIME = '动画'
REAL = '三次元'

BOOK_NOVEL = '小说'
BOOK_ALBUM = '画集'
BOOK_CARTOON = '漫画'

ANIME_MOVIE = '剧场版'
ANIME_TV = '番剧'
ANIME_OVA = 'OVA'


def get_categorys():
    data = {
        MUSIC: 'MUSIC',
        BOOK: 'BOOK',
        GAME: 'GAME',
        ANIME: 'ANIME',
        REAL: 'REAL'
    }
    return data


def get_book_types():
    data = {
        BOOK_NOVEL: 'BOOK_NOVEL',
        BOOK_ALBUM: 'BOOK_ALBUM',
        BOOK_CARTOON: 'BOOK_CARTOON'
    }
    return data


def get_anime_types():
    data = {
        ANIME_MOVIE: 'ANIME_MOVIE',
        ANIME_TV: 'ANIME_TV',
        ANIME_OVA: 'ANIME_OVA'
    }
    return data


def get_types_by_category(category):
    if category == 'BOOK':
        return get_book_types()
    elif category == 'ANIME':
        return get_anime_types()
    else:
        return None
    pass