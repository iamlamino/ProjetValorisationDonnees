import mysql.connector
import datetime

# Connect with the MySQL Server
cnx = mysql.connector.connect(host='localhost',user='root', password='', database='ecommerce')

curA = cnx.cursor(buffered=True) # selection des clients
curB = cnx.cursor(buffered=True) # insertion d'une commande
curC = cnx.cursor(buffered=True) # insertion d une ligne de commande

# texte de la requete SQL a executer
query = ("SELECT idClient FROM clients")


# execution de la requete dans le cursor en passant une liste de parametres ici reduite a un seul element
curA.execute(query)

# preparation requete insertion dans commandes qui va etre executee pour chaque client
# schema de COMMANDES (idCom auto_increment, dateCom, idClient, statut)
q2=("INSERT INTO COMMANDES (dateCom, idClient, statut) VALUES (%s, %s, %s)")

# preparation requete insertion dans lignecommande qui va etre executee pour chaque commande de chaque client
# schema de LIGNECOMMANDES(idCommande, noligne, idProduit, quantite)
q3=("INSERT INTO LIGNECOMMANDES(%s,%s,%s,1)")


# on itere sur le resultat de la requete "stocke" dans curA
for (id) in curA:
	#on tire le nombre de commandes pour ce client, entier entre 0 et 4
	nbcom=randint(0,4)
	for i in range(nbcom):
		# choisir une date
		dateCom=datetime.date(2022, 10, 1)
		# choisir un statut avec la fonction choice
		statut="en cours"
		curB.execute(q2, (dateCom, id[0], statut))
		# on recupere idCommande genere via l autoincrement
		idCom=curB.lastrowid
		# on tire le nombre de produits pour cette commande, entier entre 1 et 3 et on le met dans la variable nbprod (à écrire)
		for j in range(nbprod):
			# on tire un numéro de produit entre 1 et 1243 et on le met dans la variable nump (a faire)
			# on fait l'insertion de la ligne de commande avec le numero de commande, le numero de ligne de commande, l'id de produit et la quantite (1 ou 2)
		print ("commande inseree avec ses lignes de commandes")
	cnx.commit()
	print ("on a traite un client supplementaire")
print ("on a fini de traiter tous les clients")
cnx.close()

