import mysql.connector

# connection create
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jugnu",
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test2.test_table(C1 INT,C2 VARCHAR(30),C3 FLOAT,C4 INT,C5 VARCHAR(20));")
mydb.close()
