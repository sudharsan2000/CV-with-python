import urllib2
import time
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sudhar",
    password="ni6ga2rd",
    database="mydatabase"
)
mycursor = mydb.cursor()
old =0.000
r=urllib2.urlopen("http://192.168.43.52/turnon")
while(1):
    data = urllib2.urlopen("http://192.168.43.52/data.txt").read(5)
    value = float(data)
    sql = "SELECT payed FROM consumer WHERE id = 2"
    mycursor.execute(sql)
    for x in mycursor:
        #print(x);
        if(x==(0,)):
            r=urllib2.urlopen("http://192.168.43.52/turnoff")
        time.sleep(2)    
            
    mydb.commit()


    if old!=value :
        sql = "UPDATE consumer SET units = %s WHERE id = %s"
        val = (value, 2)
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "UPDATE consumer SET bill = %s WHERE id = %s"
        if ( value >= 501):
            bill = ((value-500)*5) + 1390
        elif (value>= 201):
            bill = ((value-200)*3.5) + 310
        elif (value>=101):
            bill = ((value-100)*2.5) + 30;
        else :
            bill = 0
        val = (bill, 2)
        mycursor.execute(sql, val)
        mydb.commit()
        print("inloop")
        
    old = value
    if(value>=1.5):
        r=urllib2.urlopen("http://192.168.43.52/turnoff")
