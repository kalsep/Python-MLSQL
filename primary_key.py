import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'new_test',
    password ='Pravin@1995',
    database = 'test_sql'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(id INT(10) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),address VARCHAR(255))")
