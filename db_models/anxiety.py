import mysql.connector  #mysql connector

connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()

def anxiety():
    cursor.execute("create table anxiety(email varchar(300),date varchar(10),result varchar(15))")

anxiety()