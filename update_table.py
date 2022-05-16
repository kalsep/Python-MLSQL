import mysql.connector

mydb = mysql.connector.connect( host='localhost',
    user = 'new_test',
    password = 'Pravin@1995',
    database = 'test_sql')

mycursor = mydb.cursor()

#sql = "UPDATE customers SET address='Highway 21' WHERE address='Vally 345'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount,'Rocord Affected')



sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")