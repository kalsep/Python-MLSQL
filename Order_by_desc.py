import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

my_results = mycursor.fetchall()

for x in my_results:
    print(x)