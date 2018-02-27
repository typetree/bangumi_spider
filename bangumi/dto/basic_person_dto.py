# *_*coding:utf-8 *_*
# author: hoicai


class BasicPersonDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
            self.bangumi_person_id = None
            self.name = None
            self.chinese_name = None
            self.profession = None
            self.alias = None
            self.picture = None
            self.sex = None
            self.birthday = None
            self.blood_type = None
            self.height = None
            self.homeplace = None
            self.education = None
            self.constellation = None
            self.interest = None
            self.special_skill = None
            self.family = None
            self.recognized_honor = None
            self.intro = None
            self.extends = None
            self.remark = None
            self.status = None
            self.create_time = None
            self.update_time = None
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.bangumi_person_id = row[2]
            self.name = row[3]
            self.chinese_name = row[4]
            self.profession = row[5]
            self.alias = row[6]
            self.picture = row[7]
            self.sex = row[8]
            self.birthday = row[9]
            self.blood_type = row[10]
            self.height = row[11]
            self.homeplace = row[12]
            self.education = row[13]
            self.constellation = row[14]
            self.interest = row[15]
            self.special_skill = row[16]
            self.family = row[17]
            self.recognized_honor = row[18]
            self.intro = row[19]
            self.extends = row[20]
            self.remark = row[21]
            self.status = row[22]
            self.create_time = row[23]
            self.update_time = row[24]
