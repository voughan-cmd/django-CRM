#install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql connector
#pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   password = 'Voughan09'

   )

# prepare a cursor object
cursorObject = database.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")