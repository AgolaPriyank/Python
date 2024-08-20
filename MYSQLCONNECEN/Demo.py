import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="Priyank@002",database="priyank")

mycursor = db.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in result:
    print(i)