  # -*- coding: utf-8 -*-
import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'database':'',
    'host' : '',
    'charset' : 'sjis'
}

cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
#cur.execute("SET NAMES sjis")
sql ="SELECT * FROM  WHERE '"

cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(row[0])

###DATE, VALUE
##for (DATE, VALUE) in cur:
##    print(DATE, VALUE)

cur.close()
cnx.close()