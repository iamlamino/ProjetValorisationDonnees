INSERT INTO produit (idProduit,nomProduit,prix,poids,idCategories) 
SELECT idProduit,nomProduit,prix,poidsExpedition,idCategories
FROM products P, categories c 
where c.nomCategorie = TRIM(SUBSTRING_INDEX(P.categorieProduit, "|", -1))