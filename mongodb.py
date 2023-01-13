from pymongo import MongoClient
import csv


class SQL:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.group_file_name =  'target.csv'
        self.user_file_name=['304804_2022104_1.csv','304834_2022104_1.csv','307614_2022104_1.csv','307688_2022104_1.csv']
        self.db = self.cluster["user_storage"]
        self.group_collection = self.db['group']
        self.user_collection = self.db['user']

    def set_group(self):
        with open(self.group_file_name, newline='') as file:
            rows = csv.reader(file)
            count = 0
            for row in rows:
                if count == 0:
                    count+=1
                else:
                    member_list=[]
                    group = {
                        "group_id": '',
                        "apply":[],
                        "advisor":'',
                        "leader":{'student_id':'','name':'','last_score':'00','next_score':'00'},
                        "member":[],
                        "interm_report":{'file_path':''},
                        "competition":{'file_path':''},
                        "acedemic_year":'111',
                        "comment":'',
                        }
                    leader_name = row[2]
                    leader_id = row[3]
                    group['group_id'] = row[3]
                    group['leader']['name'] = row[2]
                    group['leader']['student_id'] =row[3]
                    group['advisor'] = row[1]
                    member_list = row[6:14]
                    member_dict = {}
                    for i in range(len(member_list)):
                        if i%2 == 0:
                            if member_list[i]!= '' and member_list[i] != leader_name:
                                member_dict['name'] = member_list[i]
                            else:
                                if member_list[i] != '':
                                    print(leader_id)
                        else:
                            if member_list[i] != '' and member_list[1] != leader_id:
                                member_dict['student_id'] = member_list[i]
                                member_dict['last_score'] = '00'
                                member_dict['next_score'] = '00'
                                group['member'].append(member_dict)
                                member_dict={}
                            else:
                                pass
                    #self.group_collection.insert_one(group)
        print('Set group information done.')
            
    def set_user_leader(self):
        with open(self.group_file_name, newline='') as file:
            rows = csv.reader(file)
            count = 0
            for row in rows:
                if count ==0:
                    count+=1
                else:
                    user={
                        "account":'',
                        "password":'',
                        "student_id":'',
                        "type":"student",
                        "user_identity":"group_leader",
                        "group_id":"",
                        "name":'',
                        "phonenumber":'',
                        "advisor":'',
                        "acedemic_year":'111',
                    }
                    user['name'] = row[2]
                    user['account'] = 't'+row[3]+'@ntut.org.tw'
                    user['student_id'] = row[3]
                    user['group_id'] = row[3]
                    user['phonenumber'] = row[4]
                    user['advisor'] = row[1]
                    self.user_collection.insert_one(user)
        print('Set group leader user information done.')
    
    def set_user_member(self):
        with open(self.group_file_name, newline='') as file:
            rows = csv.reader(file)
            count = 0
            for row in rows:
                if count == 0:
                    count+=1
                else:
                    leader_name = row[2]
                    leader_id = row[3]
                    member_list=row[6:14]
                    user={
                        "account":'',
                        "password":'',
                        "student_id":'',
                        "type":"student",
                        "user_identity":"group_member",
                        "group_id":"",
                        "name":'',
                        "phonenumber":'',
                        "advisor":'',
                        "acedemic_year":'111',
                        }
                    for i in range(len(member_list)):
                        if i%2 == 0:
                            if member_list[i] != leader_name and member_list[i]!='':
                                user['name'] = member_list[i]
                            else:
                                pass
                        else:
                            if member_list[1] != leader_id and member_list[i]!='':
                                user['student_id'] = member_list[i]
                                user['account'] = 't'+member_list[i]+'@ntut.org.tw'
                                user['group_id'] = row[3]
                                user['advisor'] = row[1]
                                self.user_collection.insert_one(user)
                                user={
                                "account":'',
                                "password":'',
                                "student_id":'',
                                "type":"student",
                                "user_identity":"group_member",
                                "group_id":"",
                                "name":'',
                                "phonenumber":'',
                                "advisor":'',
                                "acedemic_year":'111',
                                }
                            else:
                                pass
        print('Set group member user information done.')
    
    def set_professor_user(self):
        pro = {'李士修':'ericli@ntut.edu.tw',
        '鄭瑞清':'juiching@ntut.edu.tw',
        '李仁貴':'evans@ntut.edu.tw',
        '邱弘緯':'hwchiu@ntut.edu.tw',
        '黃育賢':'yshwang@ntut.edu.tw',
        '陳建中':'jjchen@ntut.edu.tw',
        '曾恕銘':'shuming@ntut.edu.tw',
        '李文達':'wtlee@ntut.edu.tw',
        '林信標':'hplin@ntut.edu.tw',
        '范育成':'skystar@ntut.edu.tw',
        '王多柏':'tpwang@ntut.edu.tw',
        '劉玉蓀':'ysliu@ntut.edu.tw',
        '余政杰':'ccyu@ntut.edu.tw',
        '林鼎然':'tinglan@ntut.edu.tw',
        '高立人':'ljkau@mail.ntut.edu.tw',
        '黃士嘉':'schuang@ntut.edu.tw',
        '胡心卉':'hhhu@ntut.edu.tw',
        '蔡偉和':'whtsai@ntut.edu.tw',
        '段裘慶':'cctuan@ntut.edu.tw',
        '孫卓勳':'jssun@ntut.edu.tw',
        '曾德樟':'dctseng@ntut.edu.tw',
        '陳晏笙':'yschen@ntut.edu.tw',
        '王紳':'wangsen@ntut.edu.tw',
        '譚巽言':'sytan@mail.ntut.edu.tw',
        '楊濠瞬':'haoshun@mail.ntut.edu.tw',
        '潘孟鉉':'mspan@ntut.edu.tw',
        '賴冠廷':'ktlai@mail.ntut.edu.tw',
        '黃柏鈞':'po.chun.huang@ntut.edu.tw',
        '李昭賢':'chlee@ntut.edu.tw',
        '鍾明桉':'mingannchung@ntut.edu.tw',
        '陳維昌':'wcchen@ntut.edu.tw',
        '曾柏軒':'phtseng@ntut.edu.tw'
        }
        for name in pro:
            pro_info={
                'account':'',
                'password':'',
                'name':'',
                'type':'professor'
            }
            pro_info['name'] = name
            pro_info['account'] = pro[name]
            self.user_collection.insert_one(pro_info)
        print('Set professor user done.')

    def count(self):
        count = 0
        for file_name in self.user_file_name:
            with open(file_name,newline='') as rows:
                for row in rows:
                    count+=1
        print(count)
                


    def delete_all(self):
        self.group_collection.delete_many({})
        self.user_collection.delete_many({'type':'student'})
        print('Delete group collection and user collection done.')

if __name__ == '__main__':
    sql = SQL()
    #sql.delete_all()
    sql.set_group()
    # sql.set_user_leader()
    # sql.set_user_member()
    #sql.set_professor_user()
    print('All done!')
