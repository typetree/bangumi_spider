# *_*coding:utf-8 *_*
# author: hoicai

class UserFriendsDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.user_id = None
            self.user_code = None
            self.user_name = None
            self.friend_user_id = None
            self.friend_user_code = None
            self.friend_user_name = None
            self.is_friend = None
            self.status = None
            self.create_time = None
            self.update_time = None
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.user_id = row[2]
            self.user_code = row[3]
            self.user_name = row[4]
            self.friend_user_id = row[5]
            self.friend_user_code = row[6]
            self.friend_user_name = row[7]
            self.is_friend = row[8]
            self.status = row[9]
            self.create_time = row[10]
            self.update_time = row[11]