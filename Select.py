from unittest import result
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

results = mycursor.fetchall()

for x in results:
    print(x)
