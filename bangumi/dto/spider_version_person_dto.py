# *_*coding:utf-8 *_*
# author: hoicai

class SpiderVersionPersonDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.person_id = None
            self.bangumi_person_id = None
            self.person_name = None
            self.basic_person_version = ''
            self.basic_person_fingerprint = ''
            self.basic_person_active_degree = ''
            self.log = None
            self.status = None
            self.create_time = None
            self.update_time = None
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.person_id = row[2]
            self.bangumi_person_id = row[3]
            self.person_name = row[4]
            self.basic_person_version = row[5]
            self.basic_person_fingerprint = row[6]
            self.basic_person_active_degree = row[7]
            self.log = row[8]
            self.status = row[9]
            self.create_time = row[10]
            self.update_time = row[11]