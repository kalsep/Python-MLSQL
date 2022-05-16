##If you are only interested in one row, you can use the fetchone() method.

##The fetchone() method will return the first row of the result:
import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

results =mycursor.fetchall()

for x in results:
    print(x)