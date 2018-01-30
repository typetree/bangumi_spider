# *_*coding:utf-8 *_*
# author: hoicai


class UserInfoDTO(object):

    def __init__(self):
        self.id = None
        self.optimistic = None
        self.code = None
        self.name = None
        self.join_time = None
        self.homepage = None
        self.bangumi_user_id = None
        self.status = None
        self.hash_value = None
        self.spider_version = None
        self.active_degree = None
        self.friends_num = None
        self.last_active_time = None
        self.intro = None
        self.anime_do = None
        self.anime_collect = None
        self.anime_wish = None
        self.anime_on_hold = None
        self.anime_dropped = None
        self.game_do = None
        self.game_collect = None
        self.game_wish = None
        self.game_on_hold = None
        self.game_dropped = None
        self.book_do = None
        self.book_collect = None
        self.book_wish = None
        self.book_on_hold = None
        self.book_dropped = None
        self.real_do = None
        self.real_collect = None
        self.real_wish = None
        self.real_on_hold = None
        self.real_dropped = None
        self.group_num = None
        self.create_time = None
        self.update_time = None


    def __init__(self,row):
        self.id = row[0]
        self.optimistic = row[1]
        self.code = row[2]
        self.name = row[3]
        self.join_time = row[4]
        self.homepage = row[5]
        self.bangumi_user_id = row[6]
        self.status = row[7]
        self.hash_value = row[8]
        self.spider_version = row[9]
        self.active_degree = row[10]
        self.friends_num = row[11]
        self.last_active_time = row[12]
        self.intro = row[13]
        self.anime_do = row[14]
        self.anime_collect = row[15]
        self.anime_wish = row[16]
        self.anime_on_hold = row[17]
        self.anime_dropped = row[18]
        self.game_do = row[19]
        self.game_collect = row[20]
        self.game_wish = row[21]
        self.game_on_hold = row[22]
        self.game_dropped = row[23]
        self.book_do = row[24]
        self.book_collect = row[25]
        self.book_wish = row[26]
        self.book_on_hold = row[27]
        self.book_dropped = row[28]
        self.real_do = row[29]
        self.real_collect = row[30]
        self.real_wish = row[31]
        self.real_on_hold = row[32]
        self.real_dropped = row[33]
        self.group_num = row[34]
        self.create_time = row[35]
        self.update_time = row[36]
