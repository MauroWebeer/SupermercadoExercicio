import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")

mycursor = mydb.cursor()
