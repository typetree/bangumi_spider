# *_*coding:utf-8 *_*
# author: hoicai
from bangumi.constants import table_constants


class BasicPersonDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = None
            self.optimistic = None
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
            self.name = row[2]
            self.chinese_name = row[3]
            self.profession = row[4]
            self.alias = row[5]
            self.picture = row[6]
            self.sex = row[7]
            self.birthday = row[8]
            self.blood_type = row[9]
            self.height = row[10]
            self.homeplace = row[11]
            self.education = row[12]
            self.constellation = row[13]
            self.interest = row[14]
            self.special_skill = row[15]
            self.family = row[16]
            self.recognized_honor = row[17]
            self.intro = row[18]
            self.extends = row[19]
            self.remark = row[20]
            self.status = row[21]
            self.create_time = row[22]
            self.update_time = row[23]
