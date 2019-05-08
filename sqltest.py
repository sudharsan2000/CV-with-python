import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sudhar",
    password="ni6ga2rd",
    database="mydatabase"
)
mycursor = mydb.cursor()
choice = raw_input("Enter your choice")
if( choice == "add" ):
    sql = "INSERT INTO consumer (id, units,bill,payed) VALUES (%s, %s, %s, %s)"
    val = (3,0.00,0.00,0)
    mycursor.execute(sql, val)
else:
    mycursor.execute("SELECT * FROM consumer")
    result  = mycursor.fetchall()
    for x in result:
        print (x)

    

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
    #print(x)
#mycursor.execute("CREATE TABLE consumer (id INTEGER PRIMARY KEY, units FLOAT, bill FlOAT)")

mydb.commit()
mycursor.close()
