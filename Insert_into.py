import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql'
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s,%s)"
val = ("John",'Highway 21')


mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount,'Record Inserted..')