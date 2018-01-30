# *_*coding:utf-8 *_*
# author: hoicai



class SpiderVersionDTO(object):

    def __init__(self):
        self.id = None
        self.optimistic = None
        self.version = None
        self.spider_version = None
        self.active_degree = None
        self.log = None
        self.status = None
        self.create_time = None
        self.update_time = None

    def __init__(self, row):
        self.id = row[0]
        self.optimistic = row[1]
        self.version = row[2]
        self.spider_version = row[3]
        self.active_degree = row[4]
        self.log = row[5]
        self.status = row[6]
        self.create_time = row[7]
        self.update_time = row[8]



