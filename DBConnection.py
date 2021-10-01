import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print("Name |  Address")

for x in myresult:
    print(x[0] + " | " + x[1])
    print(type(x))
mydb.commit()

print(mycursor.rowcount, "record inserted.")
