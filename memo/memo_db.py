import pymysql

def write_memo (id, type, title, content, date, time):
    con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8mb4')
    cursor = con.cursor()

    time = date + ' ' + time + ':00'


    inspection="SELECT memo_name FROM Memo_management WHERE member_num=%s AND memo_name=%s"
    cursor.execute(inspection, (id, title))
    num = 0

    while (cursor.rowcount != 0):
        num += 1
        cursor.execute(inspection, (id, title + '(' + str(num) + ')'))

    if (num != 0):
        title = title + '(' + str(num) + ')'

    insert="INSERT INTO Memo_management VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(insert, (id, type, title, content, time))
    
    con.commit()
    con.close()

#def delete_memo (id, title):
def delete_memo (title):
    con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8mb4')
    cursor = con.cursor()

    #delete="DELETE FROM Memo_management WHERE member_num=%s AND memo_name=%s"
    delete="DELETE FROM Memo_management WHERE memo_name=%s"
    cursor.execute(delete, (title))

    con.commit()
    con.close()


#def view_memo(id):
def view_memo(user_name):
    con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8mb4')
    cursor = con.cursor()

    view = "SELECT * FROM Memo_management WHERE member_num = %s"
    #view = "SELECT * FROM Memo_management"
    cursor.execute(view, (user_name))


    result = cursor.fetchall()
    #print(result)

    con.commit()
    con.close()

    return result

def count_memo(user_name):
    con = pymysql.connect(host= 'root.camyxyxscvxt.ap-northeast-2.rds.amazonaws.com', user= 'porsche', password= 'root1234', db= 'OSS_db', charset= 'utf8mb4')
    cursor = con.cursor()

    search = "SELECT * FROM Memo_management WHERE member_num = %s"
    #search = "SELECT * FROM Memo_management"        #회원에 맞는거 탐색으로 변경해야함 ㅇ 

    cursor.execute(search,(user_name))

    count = cursor.rowcount

    con.commit()
    con.close()
    return count