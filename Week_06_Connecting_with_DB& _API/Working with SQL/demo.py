import mysql.connector

# connection create
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jugnu",
    database="test1" 
)
print(mydb)
# cursor create
mycursor = mydb.cursor()

# query run
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)