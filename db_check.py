#this program check databases
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
)

mycursor = mydb.cursor()

mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)