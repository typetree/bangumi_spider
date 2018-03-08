# *_*coding:utf-8 *_*
# author: hoicai


class BasicProfessionDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.category = None
            self.order_name = None
            self.name = None
            self.remark = None
            self.status = None
            self.create_time = None
            self.update_time = None
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.category = row[2]
            self.order_name = row[3]
            self.name = row[4]
            self.remark = row[5]
            self.status = row[6]
            self.create_time = row[7]
            self.update_time = row[8]