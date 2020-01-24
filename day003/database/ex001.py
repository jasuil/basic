# sql lite

#import keyword

#print(keyword.kwlist) # 예약어 리스트

import sqlite3 as sql

conn = sql.connect("mysql_lite.db") # relative path
mycursor = conn.cursor()

mycursor.execute("drop table if exists address")
mycursor.execute("drop table if exists menu")
mycursor.execute("create table menu (menu varchar(50), price int)")

mycursor.execute("insert into menu (menu, price) values (\"짱성일\", 2000);")
mycursor.execute("insert into menu (menu, price) values (\"성일짱\", 2300);")
mycursor.execute("insert into menu (menu, price) values (\"jasuil\", 2700);")



# address
mycursor.execute("create table address (id int(100), name varchar(500), phone varchar(20), memo varchar(1000),  day DATETIME DEFAULT CURRENT_TIMESTAMP)")
mycursor.execute("insert into address values (1, \"jasuil\", \"010-3119-6481\", \"jasuil is a good person\",  datetime(CURRENT_TIMESTAMP, 'localtime'))")
mycursor.execute("insert into address values (2, \"jsi\", \"032-231-6481\", \"jsi is a good person\", datetime(CURRENT_TIMESTAMP, 'localtime'))")

conn.commit()


mycursor.execute("select * from address")
rows = mycursor.fetchall()

for element in rows:
    print("{}, {}, {}, {}, {}".format(element[0], element[1], element[2], element[3], element[4], end=':'))


