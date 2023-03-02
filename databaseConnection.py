import mysql.connector

con = mysql.connector.connect(user='root', password='Samsung753', host='localhost',
                              database='intelligent_transportation')
cur = con.cursor()
sql = 'select * from vehicle_info'


def connect():
    cur.execute(sql)
    dbRecord = cur.fetchall()
    for i in dbRecord:
        print(i)
