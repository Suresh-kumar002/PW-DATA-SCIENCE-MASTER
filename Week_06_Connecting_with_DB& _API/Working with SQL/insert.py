import mysql.connector

# connection create
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jugnu",
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mycursor.execute("insert into test2.test_table values(123,'suru',796.76,876,'ku')")
mydb.commit()
mydb.close()
