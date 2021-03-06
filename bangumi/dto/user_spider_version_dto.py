# *_*coding:utf-8 *_*
# author: hoicai
class UserSpiderVersionDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.user_id = None
            self.user_code = None
            self.bangumi_user_id = None
            self.user_info_version = ''
            self.user_info_fingerprint = ''
            self.user_info_active_degree = 100
            self.user_friends_version = ''
            self.user_friends_fingerprint = ''
            self.user_friends_active_degree = 100
            self.user_anime_version = ''
            self.user_anime_fingerprint = ''
            self.user_anime_active_degree = 100
            self.user_game_version = ''
            self.user_game_fingerprint = ''
            self.user_game_active_degree = 100
            self.user_book_version = ''
            self.user_book_fingerprint = ''
            self.user_book_active_degree = 100
            self.user_real_version = ''
            self.user_real_fingerprint = ''
            self.user_real_active_degree = 100
            self.user_mono_character_version = ''
            self.user_mono_character_fingerprint = ''
            self.user_mono_character_active_degree = 100
            self.user_mono_person_version = ''
            self.user_mono_person_fingerprint = ''
            self.user_mono_person_active_degree = 100
            self.user_group_version = ''
            self.user_group_fingerprint = ''
            self.user_group_active_degree = 100
            self.log = None
            self.status = None
            self.create_time = None
            self.update_time = None
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.user_id = row[2]
            self.user_code = row[3]
            self.bangumi_user_id = row[4]
            self.user_info_version = row[5]
            self.user_info_fingerprint = row[6]
            self.user_info_active_degree = row[7]
            self.user_friends_version = row[8]
            self.user_friends_fingerprint = row[9]
            self.user_friends_active_degree = row[10]
            self.user_anime_version = row[11]
            self.user_anime_fingerprint = row[12]
            self.user_anime_active_degree = row[13]
            self.user_game_version = row[14]
            self.user_game_fingerprint = row[15]
            self.user_game_active_degree = row[16]
            self.user_book_version = row[17]
            self.user_book_fingerprint = row[18]
            self.user_book_active_degree = row[19]
            self.user_real_version = row[20]
            self.user_real_fingerprint = row[21]
            self.user_real_active_degree = row[22]
            self.user_mono_character_version = row[23]
            self.user_mono_character_fingerprint = row[24]
            self.user_mono_character_active_degree = row[25]
            self.user_mono_person_version = row[26]
            self.user_mono_person_fingerprint = row[27]
            self.user_mono_person_active_degree = row[28]
            self.user_group_version = row[29]
            self.user_group_fingerprint = row[30]
            self.user_group_active_degree = row[31]
            self.log = row[32]
            self.status = row[33]
            self.create_time = row[34]
            self.update_time = row[35]
