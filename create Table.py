import mysql.connector

mydb = mysql.connector.connect(
     host = 'localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE customers(name VARCHAR(255), age VARCHAR(255))')

