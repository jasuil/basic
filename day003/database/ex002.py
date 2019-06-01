# insert into database

import sqlite3 as sql

arr = []
arr2 = [[]]

with open("score.txt", "r", encoding="utf-8") as file:

    lines = file.readlines()

    for line in lines:
        elements = line.split()
        arr.append(elements)


print("성적표")
for e in range(6):

    print(arr[e][0], arr[e][1])


conn = sql.connect("mysql_lite.db")

corsor = conn.cursor()
corsor.execute("drop table if exists student")
corsor.execute("create table student (name varchar(50), kor int, eng int, math int)")

query = "insert into student (name, kor, eng, math) values (?, ?, ?, ?)"

for i in range(len(arr)):
    corsor.execute(query, (arr[i][0], arr[i][1], arr[i][2], arr[i][3]))

conn.commit()

corsor.execute("select * from student")
rows = corsor.fetchall()

#  select from student table
print("student score")
print("==============")
print("name kor eng math")
for row in rows:
    print("{}: {:.2f}, {:.2f}, {:.2f}".format(row[0], row[1], row[2], row[3]))
print("==============")


###########################

query = "select * from student where name=?"
corsor.execute(query, (["김연아"]))
rows = corsor.fetchall()

print("{}성적===>".format("김연아"))

for i in rows:
    print(i)

