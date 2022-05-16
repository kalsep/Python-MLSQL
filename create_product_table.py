import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()

#sql1 = "CREATE TABLE products (id INT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250) NOT NULL)"
#mycursor.execute(sql1)
#mycursor.commit()
sql2 = "INSERT INTO products (id,name) VALUES (%s,%s)"
val = [(154,'Chocolate Heaven'),(155,'Tasty Lemons'),(156,'Vanilla Dreams')]

mycursor.executemany(sql2,val)

mydb.commit()

print(mycursor.rowcount, 'was Inserted')