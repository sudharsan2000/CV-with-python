import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sudhar",
    password="ni6ga2rd",
    database="mydatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE consumer (id INTEGER PRIMARY KEY, units FLOAT, bill FlOAT, payed INTEGER)")   #CREATE TABLE consumer (id INTEGER PRIMARY KEY, units FLOAT, bill FlOAT)
mycursor.execute("ALTER TABLE consumer ALTER payed SET DEFAULT 1;")
for x in mycursor:
    print(x)

mydb.commit()
mycursor.close()
