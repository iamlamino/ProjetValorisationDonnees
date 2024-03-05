import pandas as pd
import random

# Charger les données depuis les fichiers CSV
commandes_df = pd.read_csv('commandes.csv')
produit_df = pd.read_csv('produit.csv')

# Créer un DataFrame pour stocker les données à insérer dans la table LignesCommande
lines_data = {'idCommande': [], 'noLigne': [], 'quantite': [], 'idProduit': []}

# Parcourir les commandes
for order_id in commandes_df['idCommande']:
    # Générer des numéros de ligne uniques pour cette commande
    available_line_numbers = list(set(range(1, 4)))
    line_numbers_to_generate = random.sample(available_line_numbers, k=random.randint(1, min(len(available_line_numbers), 3)))

    # Générer des données pour chaque ligne à insérer
    for line_number in line_numbers_to_generate:
        product_id = random.choice(produit_df['idProduit'])
        quantity = random.randint(1, 4)

        lines_data['idCommande'].append(order_id)
        lines_data['noLigne'].append(line_number)
        lines_data['quantite'].append(quantity)
        lines_data['idProduit'].append(product_id)

# Créer un DataFrame à partir des données générées
lines_df = pd.DataFrame(lines_data)

# Enregistrer le DataFrame dans un fichier CSV
lines_df.to_csv('lignesCommande.csv', index=False)