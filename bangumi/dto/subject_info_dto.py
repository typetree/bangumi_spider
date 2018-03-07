# *_*coding:utf-8 *_*
# author: hoicai


class SubjectInfoDTO(object):
    def __init__(self, row=None):
        if row is None:
            self.id = 0
            self.optimistic = 0
            self.name = ''
            self.chinese_name = ''
            self.category = ''
            self.type = ''
            self.picture = ''
            self.bangumi_subject_id = 0
            self.topic_list_id = 0
            self.comment_box_id = 0
            self.system_score_id = 0
            self.system_tag_id = 0
            self.remark = ''
            self.status = ''
            self.creator = ''
            self.create_time = ''
            self.updater = ''
            self.update_time = ''
        else:
            self.id = row[0]
            self.optimistic = row[1]
            self.name = row[2]
            self.chinese_name = row[3]
            self.category = row[4]
            self.type = row[5]
            self.picture = row[6]
            self.bangumi_subject_id = row[7]
            self.topic_list_id = row[8]
            self.comment_box_id = row[9]
            self.system_score_id = row[10]
            self.system_tag_id = row[11]
            self.remark = row[12]
            self.status = row[13]
            self.creator = row[14]
            self.create_time = row[15]
            self.updater = row[16]
            self.update_time = row[17]