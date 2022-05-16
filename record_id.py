#You can get the id of the row you just inserted by asking the cursor object.

#Note: If you insert more than one row, the id of the last inserted row is returned.
import mysql.connector
import connection

mycursor = cnt.conn.cursor()

mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)