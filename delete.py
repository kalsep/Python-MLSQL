import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address='Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'Record Deleted')

#To prevent sql Injection we should use Escape values by using the placeholder %s method:

#sql = "DELETE FROM customers WHERE address='%s"
#add = 'Mountain 21'
#mycursor.execute(sql,add)
