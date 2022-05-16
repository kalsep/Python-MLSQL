import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()

#sql1 = "CREATE TABLE IF NOT EXISTS users (id INT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250) NOT NULL, fav VARCHAR(220))"
#mycursor.execute(sql1)

sql2 = "INSERT INTO users (id,name,fav) VALUES (%s,%s,%s)"
val = [(1,'John',154),(2,'Peter',154,),(3,'Amy',155),(4,'Hannah','NULL'),(5,'Michael','NULL')]

mycursor.executemany(sql2,val)

mydb.commit()

print(mycursor.rowcount, 'was Inserted')