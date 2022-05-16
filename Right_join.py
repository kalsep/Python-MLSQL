import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()


sql = 'SELECT users.name AS user,products.name AS favorite FROM users RIGHT JOIN products ON users.fav = products.id'

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)