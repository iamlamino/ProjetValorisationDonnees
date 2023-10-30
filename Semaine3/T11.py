import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

# Insérer des données dans la table Produit à partir de productso
cursor.execute("""
    INSERT INTO Produit (nomProduit, prix, poids, idCategories)
    SELECT productso.product_name, 
           CASE
               WHEN productso.price_unit = 'USD' THEN CAST(REPLACE(productso.price, ' USD', '') AS DECIMAL(10,2))
               ELSE NULL
           END AS price,
           CASE
               WHEN productso.weight_unit = 'ounce' THEN CAST(REPLACE(productso.weight, ' ounce', '') AS DECIMAL(10,2)) * 0.0625
               WHEN productso.weight_unit = 'pound' THEN CAST(REPLACE(productso.weight, ' pound', '') AS DECIMAL(10,2))
               ELSE NULL
           END AS weight,
           c.idCategories
    FROM productso
    LEFT JOIN Categories c ON FIND_IN_SET(c.nomCategorie, REPLACE(productso.category, ' | ', ',')) > 0
""")

conn.commit()
conn.close()
