# *_*coding:utf-8 *_*
# author: hoicai

class UserInfoDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.code = None
            self.name = None
            self.join_time = None
            self.homepage = None
            self.bangumi_user_id = None
            self.profile_photo = None
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
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.code = row[2]
            self.name = row[3]
            self.join_time = row[4]
            self.homepage = row[5]
            self.bangumi_user_id = row[6]
            self.profile_photo = row[7]
            self.status = row[8]
            self.hash_value = row[9]
            self.spider_version = row[10]
            self.active_degree = row[11]
            self.friends_num = row[12]
            self.last_active_time = row[13]
            self.intro = row[14]
            self.anime_do = row[15]
            self.anime_collect = row[16]
            self.anime_wish = row[17]
            self.anime_on_hold = row[18]
            self.anime_dropped = row[19]
            self.game_do = row[20]
            self.game_collect = row[21]
            self.game_wish = row[22]
            self.game_on_hold = row[23]
            self.game_dropped = row[24]
            self.book_do = row[25]
            self.book_collect = row[26]
            self.book_wish = row[27]
            self.book_on_hold = row[28]
            self.book_dropped = row[29]
            self.real_do = row[30]
            self.real_collect = row[31]
            self.real_wish = row[32]
            self.real_on_hold = row[33]
            self.real_dropped = row[34]
            self.group_num = row[35]
            self.create_time = row[36]
            self.update_time = row[37]
