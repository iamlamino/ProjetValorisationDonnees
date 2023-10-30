import mysql.connector
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

# Récupérer les ID des clients
cursor.execute("SELECT idClient FROM Clients")
clients = cursor.fetchall()

# Liste des statuts possibles
statuses = ['en cours', 'payée', 'livrée', 'annulée']

for client in clients:
    # Générer entre 0 et 5 commandes pour chaque client
    num_orders = random.randint(0, 5)
    
    for _ in range(num_orders):
        # Générer une date aléatoire entre le 1er janvier 2020 et le 1er septembre 2022
        random_date = datetime(2020, 1, 1) + timedelta(days=random.randint(0, 975))  # 975 days is roughly 2.67 years

        # Choisir un statut aléatoire parmi la liste de statuts
        status = random.choice(statuses)

        # Insérer la commande pour le client actuel
        cursor.execute("INSERT INTO Commandes (idCommande, dateCommande, statut, idClient) VALUES (UUID(), %s, %s, %s)",
                       (random_date.strftime('%Y-%m-%d'), status, client[0]))

conn.commit()
conn.close()
s