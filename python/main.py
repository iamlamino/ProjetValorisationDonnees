from getpass import getpass
from mysql.connector  import connect, Error

try:
    connection = connect(
        user = input("Saisir le nom d'utilisateur: \n"),
        password = getpass("Saisir le mot de passe : \n"), 
        host= input ("saisir l'adresse de l'hôte: \n"), 
        database= input ("saisir le nom de la base de donnée à laquelle vous voulez vous connecter: \n")
    ) 
    print(connection)
    select_villes_query = "SELECT * FROM villes LIMIT 20"
    


    with connection.cursor() as cursor:
        cursor.execute(select_villes_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
except Error as e:
    print(e)