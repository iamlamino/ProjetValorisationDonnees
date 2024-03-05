
"""def clean_price(price):
    try:
        
        return float(price.split()[0].replace('$', ''))
    except (ValueError, IndexError):
        return None

def clean_weight(weight):
    try:
       
        weight_in_ounces = float(weight.split()[0])
        weight_in_pounds = weight_in_ounces * 0.0625
        return weight_in_pounds
    except (ValueError, IndexError):
        return None

# Insérer les données 
for product in products:
    price = clean_price(product[2])
    weight = clean_weight(product[3])

    
    if price is not None and weight is not None:
        cursor.execute("INSERT INTO Produits (idProduit, idCategories, prix, poids) VALUES (%s, %s, %s, %s)",
                       (product[0], product[1], price, weight))"""
