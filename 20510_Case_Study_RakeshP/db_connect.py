import mysql.connector


def connect_sql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hospital"
    )
    return mydb

