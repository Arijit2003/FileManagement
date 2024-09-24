import mysql.connector

#database connection
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="file_sharing_pj")
cursor=mydb.cursor()


def getUser(username,password) : 
    query = "SELECT id, name FROM users WHERE username = %s and password = %s"
    cursor.execute(query,(username,password))
    result = cursor.fetchone()
    if (result):
        return result
    else:
        return None
    
