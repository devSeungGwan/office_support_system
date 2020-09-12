import pymysql
import hashlib
import time, datetime
'''

디비관련
1. pyqt클래스내에 connect 시 불가.
2. 클래스외 전역변수로 connect시 성공
3. 2로 성공시, 클래스내부에서 닫았다 열었다 할 수 있음
예상 결론: 최초의 연결은 선의 생성, 문을 연다. 두번째부터는 문만 닫고 연다.


'''
###################
## DB부모 클래스 ##
###################
class DB_object():
    con = None
    curs = None
    def __init__(self):
         pass
    @classmethod
    def mysql_connect(cls):
        try:
            if cls.con==None or cls.con.open != 1:
                cls.con = pymysql.connect(host='root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db='OSS_db', charset='utf8mb4') 
                cls.curs = cls.con.cursor(pymysql.cursors.DictCursor)
                print('MYSQL-connect success')
            else:
                print('db연결 돼있음')
        except:
            print('MYSQL-connect error')
        finally:
            pass

    @classmethod
    def mysql_close(cls): 
        if cls.con.open:
            print('MYSQL-connect close')
            cls.con.close()
        else:
            print('MYSQL-closed')
            pass

#####################m
    @classmethod
    def user_connect_list(cls):
        DB_object.mysql_connect()
        sql = "select id, e_mail, nickname from Member_management where login_switch=1"
        cls.curs.execute(sql)
        rows = cls.curs.fetchall()
        DB_object.mysql_close()
        for row in rows:
             print('total',row)
    
    @classmethod
    def user_file_list(cls):
        pass

    @classmethod
    def user_memo_list(cls):
        pass

   #######################


####################
## DB로그인 클래스##
####################

####a
class DB_login(DB_object):
    def member_login(self, _id):
        DB_object.mysql_connect()
        sql = "UPDATE Member_management SET login_switch='1' WHERE id=%s"
        self.curs.execute(sql, (_id))
        self.con.commit()
        DB_object.mysql_close()

        

    def member_equal(self,_id, password):
        DB_object.mysql_connect()

        _pwd = hashlib.sha3_256(password.encode())
        _pwd = _pwd.hexdigest()

        sql = "select * from Member_management where id=%s and pwd=%s"
        self.curs.execute(sql, (_id, _pwd))
        row = self.curs.fetchone()
        DB_object.mysql_close()
        
        if row == None:
            return False  
        else:
            return (row['id'], row['e_mail'])       # (id, email) retur

        
    def member_switch_state(self, _id):
        DB_object.mysql_connect()

        sql = "SELECT COUNT(*) FROM Member_management WHERE id=%s and login_switch='1'"
        self.curs.execute(sql, (_id))
        row = self.curs.fetchone()
        DB_object.mysql_close()

        if row['COUNT(*)'] == 1:
            return False
        else:           ##접속가능 switch=0ㅇ이라서
            return True
##

#####################
## DB회원가입 클래스##
#####################
class DB_register(DB_object):
    '''
    ID regist (회원가입)
    필수 입력 사항: identify: 아이디 / password: 비밀번호 /  E_mail: 이메일주소 / Nickname: 닉네임
    '''
    def member_register(self, identify: str, password: str, e_mail: str, nickname: str):
        DB_object.mysql_connect()

        _id = identify
        _pwd = hashlib.sha3_256(password.encode())
        _pwd = _pwd.hexdigest()

        sql = "INSERT INTO Member_management VALUES (%s, %s, %s, %s, %s, %s)"
        self.curs.execute(sql,(_id, _pwd, e_mail, nickname, "1", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
        self.con.commit()
        
        DB_object.mysql_close()
    
    def member_id_check(self, _id: str):
        DB_object.mysql_connect()

        sql = "SELECT COUNT(*) FROM Member_management WHERE id=%s"
        self.curs.execute(sql, (_id))
        row = self.curs.fetchone()

        DB_object.mysql_close()
        if row['COUNT(*)']== 1:    ##중복있다
            return False
        else:                      ##중복없다
            return True



#######################
## DB 찾기 클래스###
########################
class DB_find(DB_object):
    def id_search(self,_e_mail: str):
        DB_object.mysql_connect()

        sql = "SELECT id FROM Member_management WHERE e_mail=%s"
        self.curs.execute(sql, (_e_mail))
        row = self.curs.fetchall()
        print("search result:", row)
        DB_object.mysql_close()
        try:
            if row == None:
                return (None)
            else:
                return row
        finally:
            pass

    def pwd_search(self, _id, _e_mail):
        DB_object.mysql_connect()

        sql = "SELECT COUNT(*) FROM Member_management WHERE id=%s and e_mail=%s"
        self.curs.execute(sql, (_id, _e_mail))
        row = self.curs.fetchone()
        print('[log]pwd_search ', row)
        DB_object.mysql_close()
        try:
            if row['COUNT(*)'] == 0:
                return False
            else:
                return True
        except:
            print('pwd search error')
            pass

######################
## DB재설정 클래스##
######################
class DB_config(DB_object):
    def pwd_config(self, id:str, password:str):
        DB_object.mysql_connect()

        sql = "UPDATE Member_management SET pwd=%s WHERE id=%s"
        self.curs.execute(sql, (password, id))
        self.con.commit()

        DB_object.mysql_close()


######################
## DB로그아웃 클래스##
######################
class DB_logout(DB_object):
     def member_logout(self, _id:str):
        DB_object.mysql_connect()
        sql = "UPDATE Member_management SET login_switch='0' WHERE id=%s"
        self.curs.execute(sql, (_id))
        self.con.commit()
        DB_object.mysql_close() 
    
if __name__=='__main__':
    pass
