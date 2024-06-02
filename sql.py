import sqlite3

## connection to database
connection=sqlite3.connect("student.db")

## cursor object to insert data, retrive table, create table
cursor=connection.cursor()

## create table
table_info="""
CREATE TABLE student(Name VARCHAR(20), Roll INTEGER, Marks INTEGER)
"""

cursor.execute(table_info)

## insert data
cursor.execute("INSERT INTO student VALUES('Amit', 1, 90)")
cursor.execute("INSERT INTO student VALUES('Rahul', 2, 80)")
cursor.execute("INSERT INTO student VALUES('Rohit', 3, 70)")
cursor.execute("INSERT INTO student VALUES('Raj', 4, 60)")
cursor.execute("INSERT INTO student VALUES('Ravi', 5, 50)")

## display table
print("Inserted data in table are")

data=cursor.execute("Select * from student")

for row in data:
    print(row)

## commit the changes
connection.commit()
connection.close()
