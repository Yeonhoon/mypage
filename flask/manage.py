import pymysql
import csv
import os
db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'jyhoon94',
    passwd = 'Zpflrjs94!',
    db = 'dan_db',
    charset='utf8'
    )   

class User_info:
    def __init__(self, user_id, user_email, blog_id):
        self.user_id = user_id
        self.user_email = user_email
        self.blog_id = blog_id
        
    def __str__(self):
        return f"{self.user_id}, f{self.user_email}, f{self.blog_id}"
    
    # def to_dict(self):
    #     return {}

#회원가입
def user_input(email, blog_id, pw):
    sql = "insert into user_info (user_email, blog_id, user_pw) values ('%s', '%s', '%s')"\
        % (email, blog_id, pw)
    cursor = db_conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e.args)
    else:
        db_conn.commit()
    return 

def user(user_id):
    sql = "select * from user_info where user_id = '%s'" %(user_id)
    cursor = db_conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# 전체 조회
def userlist():
    sql = "select * from user_info"
    cursor = db_conn.cursor()
    cursor.execute(sql)
    user_list = []
    for user in cursor:
        user_list.append(User_info(*user))

    return user_list

# 회원 탈퇴
def user_out():
    return ""


# 회원정보 수정
def user_update():
    return ""

