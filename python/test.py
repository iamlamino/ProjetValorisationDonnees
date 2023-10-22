from getpass import getpass
from mysql.connector  import connect, Error
try :
    connection =  connect(
            user = "root",
            password = "", 
            host= "localhost", 
            database= "ecommerce",
        ) 
    print(connection)
    
        


    select_villes_query = "SELECT * FROM villes LIMIT 20"
    with connection.cursor() as cursor:
        cursor.execute(select_villes_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
except : 
    print(Error)