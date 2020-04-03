import mysql.connector  
try:
    conn=mysql.connector.connect(host="localhost",user="root",passwd="root",db="pythondb")
    if(not(conn)):
        print("server not connected")
    else:
        print("server connected")
except:
    print("server issue")
