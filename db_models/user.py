import mysql.connector  #mysql connector

connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()


def user():
    cursor.execute("create table user(name varchar(50), age int, email varchar(300) primary key,mobile varchar(10), password varchar(300))")

user()
