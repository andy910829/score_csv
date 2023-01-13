from pymongo import MongoClient
import csv
from pprint import pprint

class fix:
    def __init__(self) -> None:
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["user_storage"]
        self.group_collection = self.db['group']
        self.user_collection = self.db['user']
        self.file_name =  'target.csv'

    def fix_group(self):
        num_list=['109360780','109360209']
        for num in num_list:
            group = self.group_collection.find_one({"group_id":num})
            id_list,name_list,advisor=self.get_group_info(num=num)
            for i in range(len(id_list)):
                member_dict={}
                member_dict['name'] = name_list[i]
                member_dict['student_id'] = id_list[i]
                member_dict['last_score'] = '00'
                member_dict['next_score'] = '00'
                self.fix_user(student_id=id_list[i],advisor=advisor,group_id=num,name=name_list[i])
                group['member'].append(member_dict)
                member_dict={}
            self.group_collection.update_one({"group_id":num},{"$set":group})
        print('Fix Group Information done!')

    def get_group_info(self,num):
        with open(self.file_name, newline='') as f:
            rows = csv.reader(f)
            for row in rows:
                member_list=row[8:14]
                if row[3] == num:
                    name_list=[]
                    id_list=[]
                    advisor=row[1]
                    for i in range(0,len(member_list),2):
                        if member_list[i] != '':
                            name_list.append(member_list[i])
                    for j in range(1,len(member_list),2):
                        if member_list[j] != '':
                            id_list.append(member_list[j])
        return id_list,name_list,advisor

    def fix_user(self,student_id,advisor,group_id,name):
        user={
        "account":'',
        "password":'',
        "student_id":'',
        "type":"student",
        "user_identity":"group_member",
        "group_id":'',
        "name":'',
        "phonenumber":'',
        "advisor":'',
        "acedemic_year":'111',
        }
        user['account'] = 't'+student_id+'@ntut.org.tw'
        user['student_id'] = student_id
        user['advisor'] = advisor
        user['group_id'] = group_id
        user['name'] = name
        self.user_collection.insert_one(user)
        print(f"Insert {student_id} Information!")


if __name__ == "__main__":
    fix().fix_group()