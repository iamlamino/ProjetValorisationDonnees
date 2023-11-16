import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

cursor.execute("SELECT categorieProduit FROM products")
categories = cursor.fetchall()
print (categories)
category_list = []

for category in categories:
    category_list.append (category[0].split(' | '))
    print(category_list)
    
    parent_id = None

    for cat in category_list:
        # Vérifier si la catégorie existe déjà
        cursor.execute("SELECT idCategories FROM categories WHERE nomCategorie = %s AND idCategorieMere = %s", (cat, parent_id))
        cat_id = cursor.fetchone()

        if cat_id:
            parent_id = cat_id[0]
        else:
            # Insérer la catégorie uniquement si elle n'existe pas encore
            cursor.execute("INSERT INTO categories (nomCategorie, idCategorieMere) VALUES (%s, %s)", (cat, parent_id))
            parent_id = cursor.lastrowid  # Récupérer l'ID de la nouvelle catégorie

conn.commit()
conn.close()