'''
.open mysql_lite.db
sqlite> .table
address  menu     student
sqlite> select * from menu;
짱성일|2000
성일짱|2300
jasuil|2700

'''

import sqlite3 as sql

conn = sql.connect("mysql_lite.db")
c = conn.cursor()

# foodName = input("food name?")
# foodPrice = int(input("food price?"))
#
# query = "insert into menu (menu, price) values (?, ?);"
# c.execute(query, (foodName, foodPrice))
#
# conn.commit()

c.execute("select * from menu")
rows = c.fetchall()

for row in rows:
    print(row)