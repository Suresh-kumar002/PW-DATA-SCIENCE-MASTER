import mysql.connector

# connection create
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jugnu",
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from test2.test_table")
for i in mycursor.fetchall():
    print(i)
mydb.close()
