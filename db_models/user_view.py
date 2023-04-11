import mysql.connector  #mysql connector

connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()

def user_view():
    cursor.execute("create view user_view as select email,password from user")

user_view()