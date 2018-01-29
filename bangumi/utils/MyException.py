# *_*coding:utf-8 *_*
# author: hoicai

class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message