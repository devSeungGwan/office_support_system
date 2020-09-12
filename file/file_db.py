import pymysql

class DB_object():
    con = None
    curs = None
    def __init__(self): pass

    @classmethod
    def mysql_connect(cls):
        try:
            if cls.con==None or cls.con.open != 1:
                cls.con = pymysql.connect(host='root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db='OSS_db', charset='utf8mb4')
                cls.curs = cls.con.cursor(pymysql.cursors.DictCursor)
                print('MYSQL-connect success')
            else: print('db연결 돼있음')
        except: print('MYSQL-connect error')
        finally: pass

    @classmethod
    def mysql_close(cls):
        if cls.con.open:
            print('MYSQL-connect close')
            cls.con.close()
        else:
            print('MYSQL-closed')
            pass


    @classmethod
    def user_connect_list(cls):
        DB_object.mysql_connect()
        sql = "select id, e_mail, nickname from Member_management where login_switch=1"
        cls.curs.execute(sql)
        rows = cls.curs.fetchall()
        DB_object.mysql_close()
        for row in rows: print('total',row)

    @classmethod
    def user_file_list(cls): pass

    @classmethod
    def user_memo_list(cls): pass



class file_db(DB_object):
    @classmethod
    def upload_file(id, file_name, file_path, file_type):
        DB_object.mysql_connect()

        prime_number_check = "SELECT MAX(prime_number) FROM File_management"
        self.curs.execute(prime_number_check)

        result = cursor.fetchall()

        max_value = result[0][0]        #prime_number로 사용 prime_number

        if max_value == None: max_value = 0  #초기 파일 없으면 0으로 설정
        else: max_value += 1  #아니면 increment

        file_name_check = "SELECT file_name FROM File_management WHERE file_name=%s"
        self.curs.execute(file_name_check, (file_name))
        num = 0

        while (cursor.rowcount != 0):
            num += 1
            cursor.execute(file_name_check, (file_name + '(' + str(num) + ')'))

        if (num != 0): file_name = file_name + '(' + str(num) + ')'

        time_check = "SELECT now()"     #서버 시간을 업로드 시간으로
        self.curs.execute(time_check)
        result = cursor.fetchall()
        upload_time = result[0][0]

        upload = "INSERT into File_management VALUES(%s, %s, %s, %s, %s, %s)"

        self.curs.execute(upload, (id, max_value, file_name, upload_time, file_type, file_path))

        self.con.commit()
        DB_object.mysql_close()
        return file_name



    @classmethod
    def prime_check():
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        check = "SELECT prime_number FROM File_management"
        cursor.execute(check)

        result = cursor.fetchall()

        search = "SELECT * FROM File_management"        #회원에 맞는거 탐색으로 변경해야함 ㅇ
        cursor.execute(search)
        count = cursor.rowcount


        prime_list = []
        for i in range(0 , count):
            prime_number = result[i][0]
            prime_list.append(prime_number)


        if prime_list == None:                         #초기 파일 없으면 0으로 설정
            prime_list.append(0)
        else:
            pass

        con.commit()
        con.close()
        return prime_list



    @classmethod
    def file_check(prime_number):
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        check = "SELECT * FROM File_management WHERE prime_number = %s"
        cursor.execute(check, (prime_number))
        result = cursor.fetchall()

        exist = result[0]

        con.commit()
        con.close()
        return exist


    @classmethod
    def delete_file(prime_number):
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        delete = "DELETE FROM File_management WHERE prime_number=%s"

        cursor.execute(delete, (prime_number))

        con.commit()
        con.close()


    @classmethod
    def count_file():
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        search = "SELECT * FROM File_management"        #회원에 맞는거 탐색으로 변경해야함 ㅇ

        cursor.execute(search)

        count = cursor.rowcount

        con.commit()
        con.close()
        return count

    @classmethod
    def view_file():
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        view = "SELECT * FROM File_management"
        cursor.execute(view)


        result = cursor.fetchall()

        con.commit()
        con.close()

        return result

    @classmethod
    def get_file_name_path(prime_number):
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        con.set_charset('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')

        path = "SELECT file_path, file_name FROM File_management WHERE prime_number = %s"
        cursor.execute(path, prime_number)

        result = cursor.fetchall()

        path = result[0][0]
        name = result[0][1]

        con.commit()
        con.close()

        return path, name


    @classmethod
    def get_file_owner(prime_number):
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        path = "SELECT member_num FROM File_management WHERE prime_number = %s"
        cursor.execute(path, prime_number)

        result = cursor.fetchall()

        owner = result[0][0]


        con.commit()
        con.close()

        return owner

    @classmethod
    def rename_file(prime_number, to_name):
        con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8')
        cursor = con.cursor()

        rename = "UPDATE File_management SET file_name = %s WHERE prime_number = %s"
        cursor.execute(rename, (to_name, prime_number))

        con.commit()
        con.close()
