import mysql.connector

# connection create
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jugnu",
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test2")
mydb.close()
