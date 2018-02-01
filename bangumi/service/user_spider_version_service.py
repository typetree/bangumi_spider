# *_*coding:utf-8 *_*
# author: hoicai
from ..utils import common_util
from ..spider import user_friends_spider


friends = user_friends_spider.find_friends('zisudaki')

user_friends_fingerprint = common_util.hashlib_md5(friends)
