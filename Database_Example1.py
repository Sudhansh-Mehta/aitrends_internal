import mysql.connector
connection = mysql.connector.connect(host='localhost',database = 'testdb',user='root',password='cdac123')
if connection.is_connected():
    print(connection.get_server_info())
    cursor = connection.cursor()
    cursor.execute("select database();")
    record=cursor.fetchone()
    print("You are connected to database : ",record)
    cursor.close()
    connection.close()
    
    
