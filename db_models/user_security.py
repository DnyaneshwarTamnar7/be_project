import mysql.connector  #mysql connector

connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()

def user_security():
    cursor.execute("create table user_security(email varchar(300) primary key,question varchar(60),answer varchar(60))")

user_security()