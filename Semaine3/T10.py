import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

# Récupérer les catégories depuis les produits
cursor.execute("SELECT DISTINCT idcategories FROM Produit")
categories = cursor.fetchall()

# Fonction récursive pour traiter les catégories
def process_categories(cat_string, parent_id=None):
    if cat_string:
        categories = cat_string.split('|')
        for category in categories:
            parent_id = insert_category(category, parent_id)
            process_categories(category, parent_id)  # Appel récursif pour traiter les catégories suivantes

  
    else:
        # Insérer la nouvelle catégorie
        cursor.execute("INSERT INTO Categories (nomCategorie, idCategorieMere) VALUES (%s, %s)", (category_name, parent_id))
        return cursor.lastrowid  # Renvoyer l'ID de la nouvelle catégorie

# Fonction récursive pour traiter les catégories
def process_categories(cat_string, parent_id=None):
    if cat_string:
        categories = cat_string.split('|')
        for category in categories:
            parent_id = insert_category(category, parent_id)
            process_categories(category, parent_id)

# Insérer les catégories pour chaque produit
for category in categories:
    process_categories(category[0])

conn.commit()
conn.close()
