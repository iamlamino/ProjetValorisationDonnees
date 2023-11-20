import mysql.connector
import random

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='ecommerce')
curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)


# recherche d'un couple ville, région à partir d'un id
select_data = ("SELECT ville, region FROM VillesSenegal WHERE id = %s")
# requete de mise à jour d'un vendeur en lui donnant un couple ville, région
add_data = ("UPDATE Vendeurs  set ville=%s, region=%s  WHERE idVendeur=%s")

# on a 92 vendeurs c est pourquoi on itère de 0 à 91
for i in range (91):
    #on tire au hasard un id de villesenegal sur l'intervalle 1 à 55 (il y a 55 villes dans la table)
    index = random.randint(1,55)
    # on sélectionne le couple ville, région correspondant
    curA.execute(select_data, (index))
    # ici on donne une valeur constant à data mais il faudrait que cela soit les valeurs venant de la requete precedente
    data=('paris', 'france')
    # on fait l update sur la table vendeurs
    curB.execute(add_data, ('paris', 'france',i))

# on doit valider la transaction sinon les modifications faites ne sont pas effectives
cnx.commit()
curA.close ()
curB.close ()

cnx.close()
