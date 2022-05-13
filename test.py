import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="Test@1995",
  database = 'test_sql'
)

print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("DROP TABLES customers")
#for x in mycursor:
 # print(x) 
