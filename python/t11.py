import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()
# Récupération des données de la table Product en utilisant une jointure avec Categories
cursor.execute("INSERT INTO produit (idProduit,nomProduit,prix,poids,idCategories) SELECT idProduit,nomProduit,prix,poidsExpedition,idCategories FROM products P, categories c  c.nomCategorie = TRIM(SUBSTRING_INDEX(P.categorieProduit,\"|\",-1))")
res = cursor.fetchall() 
print(res)           
conn.commit()
conn.close()