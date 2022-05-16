import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM customers LIMIT 5')

myresults = mycursor.fetchall()

for i in myresults:
    print(i)
