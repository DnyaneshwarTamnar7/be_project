import mysql.connector  #mysql connector

connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()

def result():
    cursor.execute("create table result(email varchar(300),date varchar(10),stress varchar(20),anxiety varchar(20),depression varchar(20))")

result()