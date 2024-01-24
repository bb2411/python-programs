import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="practice"
)
print(mydb)
mycursor = mydb.cursor()
val=(123,"abc","asasasas")
q="insert into user values(%d,%s,%s)"
mycursor.execute(q,val)
mycursor.commit()
  