import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(host='localhost',user='root', password='', database='ecommerce')

curA = cnx.cursor()

# texte de la requete SQL a executer
query = ("SELECT employee_id, first_name, last_name FROM customers WHERE employee_id < %s")


# execution de la requete dans le cursor en passant une liste de parametres ici reduite a un seul element
curA.execute(query, (110,))

# on itere sur le resultat de la requete "stocke" dans curA
for (id, fn, ln) in curA:
	print (id, fn, ln)

cnx.close()
