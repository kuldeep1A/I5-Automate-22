import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
)
# Create course Object
mycursor = database.cursor()
mycursor.execute("CREATE DATABASE dcrmDatabase")
print("All Done")

