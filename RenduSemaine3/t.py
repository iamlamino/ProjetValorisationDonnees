import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)
with conn.cursor() as cursor :
# Récupération des données de la table Product en utilisant une jointure avec Categories
    cursor.execute("SELECT * FROM products")
    res = cursor.fetchall()

    for i in res:
            nameC = i[2].split('|')
            taille=len(nameC)
            nomCat = nameC[taille -1]
            cursor.execute(f"SELECT * FROM products p, categories c WHERE p.categorieProduit LIKE \"{nomCat}\" AND c.nomCategorie=\"{nomCat}\"")
            res2 = cursor.fetchall()
            print(res2)
            conn.commit()
            cursor.close()
