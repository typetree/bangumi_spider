# *_*coding:utf-8 *_*
# author: hoicai


class SubjectProfessionPersonDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.subject_id = None
            self.subject_detail_id = None
            self.category = None
            self.name = None
            self.type = None
            self.profession_id = None
            self.profession_name = None
            self.person_id = None
            self.bangumi_person_id = None
            self.person_name = None
            self.person_chinese_name = None
            self.remark = None
            self.status = None
            self.create_time = None
            self.update_time = None
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.subject_id = row[2]
            self.subject_detail_id = row[3]
            self.category = row[4]
            self.name = row[5]
            self.type = row[6]
            self.profession_id = row[7]
            self.profession_name = row[8]
            self.person_id = row[9]
            self.bangumi_person_id = row[10]
            self.person_name = row[11]
            self.person_chinese_name = row[12]
            self.remark = row[13]
            self.status = row[14]
            self.create_time = row[15]
            self.update_time = row[16]