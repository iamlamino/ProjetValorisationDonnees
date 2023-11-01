import mysql.connector
import random

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

# Récupérer les ID des commandes
cursor.execute("SELECT idCommande FROM Commandes")
orders = cursor.fetchall()

# Récupérer les ID des produits
cursor.execute("SELECT idProduit FROM Produit")
products = cursor.fetchall()

for order in orders:
    # Générer entre 1 et 3 lignes pour chaque commande
    num_lines = random.randint(1, 3)
    
    for _ in range(num_lines):
        # Générer un numéro de ligne aléatoire entre 1 et 3
        line_number = random.randint(1, 3)
        
        # Choisir un produit aléatoire parmi la liste de produits
        product = random.choice(products)
        
        # Générer une quantité aléatoire entre 1 et 4
        quantity = random.randint(1, 4)

        # Insérer la ligne de commande pour la commande actuelle
        cursor.execute("INSERT INTO LignesCommande (idCommande, noLigne, quantite, idProduit) VALUES (%s, %s, %s, %s)",
                       (order[0], line_number, quantity, product))

conn.commit()
conn.close()
