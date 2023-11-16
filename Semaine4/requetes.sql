-- Active: 1698010070526@@127.0.0.1@3306@ecommerce

!-- 1) Quel sont les clients qui on fait plus de commandes ?
   SELECT c.idClient, c.prenom, c.nom, COUNT(co.idCommande) AS NombreCommandes
   FROM Clients c
   JOIN Commandes co ON c.idClient = co.idClient
   GROUP BY c.idClient
   ORDER BY NombreCommandes DESC
   LIMIT 5;
   

!--  2) nombre de commande fait par un client :
   SELECT * FROM Commandes WHERE idClient = '5f10e9D33fC5f2b';
   

!-- 3) liste des categ_produits avec le nbr de produit pour chaque categorie
   SELECT c.nomCategorie, COUNT(p.idProduit) AS NombreProduits
   FROM Categories c
   LEFT JOIN Produit p ON c.idCategories = p.idCategories
   GROUP BY c.nomCategorie;
   

!-- 4) Quel est la moyenne des prix des ADD produit pour chaque categories  ?
   SELECT c.nomCategorie, AVG(p.prix) AS PrixMoyen
   FROM Categories c
   JOIN Produit p ON c.idCategories = p.idCategories
   GROUP BY c.nomCategorie;
   
!--  5) les 20 produits les plus vendue 
   SELECT p.nomProduit, SUM(lc.quantite) AS TotalQuantiteVendue
   FROM Produit p
   JOIN LignesCommande lc ON p.idProduit = lc.idProduit
   GROUP BY p.nomProduit
   ORDER BY TotalQuantiteVendue DESC
   LIMIT 20;
   

!--  6) identifier le ou les  clients qui ont  acheter un produit connaissant la categorie  
SELECT c.idClient, c.prenom, c.nom, co.idCommande, ca.nomCategorie
FROM Clients c
JOIN Commandes co ON c.idClient = co.idClient
JOIN LignesCommande lc ON co.idCommande = lc.idCommande
JOIN Produit p ON lc.idProduit = p.idProduit
JOIN Categories ca ON p.idCategories = ca.idCategories
WHERE ca.nomCategorie = 'Fuse & Perler Beads';
    

!--  7) la liste des commande à une periode donnes 
SELECT * FROM Commandes WHERE dateCommande BETWEEN '2021-03-19' AND '2022-03-21';
    
!--  8) la Liste des produits dont le poids est supérieur  à 8
 SELECT * FROM Produit WHERE poids > 8;
    

!--  9) Nombre de commandes selon le statut 
SELECT statut, COUNT(*) AS NombreCommandesParStatut
FROM Commandes
GROUP BY statut;
    

!-- 10) Clients n'ayant pas encore effectué de commandes   
    SELECT c.idClient, c.prenom, c.nom
    FROM Clients c
    LEFT JOIN Commandes co ON c.idClient = co.idClient
    WHERE co.idCommande IS NULL;
    

!-- 11)Liste des produits dans une catégorie spécifique triée par prix décroissant :
    
    SELECT p.nomProduit, p.prix
    FROM Produit p
    JOIN Categories c ON p.idCategories = c.idCategories
    WHERE c.nomCategorie = 'NomCategorieSpecifique'
    ORDER BY p.prix DESC;

!-- 12) liste des clients dont la commande est en cours  

    SELECT idClient, prenom, nom, statut 
    FROM clients NATURAL JOIN commandes where statut = "en cours" 

!-- 13) Le nombre de commandes livrées, annulées ,payées ou en cours

    SELECT statut, COUNT(*) from commandes GROUP BY statut   
 
!-- 14) La ville qui contient le plus grand nombre de commandes 
    SELECT 

!-- 15) La liste des clients nés le 1 er Janvier ou le 24 décembre 

    SELECT * FROM Clients
    WHERE DATE(dateNaissance) IN ('YYY-08-17', 'YYYY-06-28');   


!-- CREATION DES VUE 

!-- vUE 1 : REQUETE 3

   CREATE VIEW produitParCategorie AS SELECT c.nomCategorie, COUNT(p.idProduit) AS NombreProduits
   FROM Categories c
   LEFT JOIN Produit p ON c.idCategories = p.idCategories
   GROUP BY c.nomCategorie
   WITH CHECK OPTION;

!-- vUE 2: REQUETE 4 

CREATE VIEW VueMoyennePrix AS
SELECT c.nomCategorie, AVG(p.prix) AS PrixMoyen
FROM Categories c
JOIN Produit p ON c.idCategories = p.idCategories
GROUP BY c.nomCategorie
WITH CHECK OPTION
;

!-- vUE 3 : REQUETE 1 
   CREATE VIEW ClientsPotentiel AS 
   SELECT c.idClient, c.prenom, c.nom, COUNT(co.idCommande) AS NombreCommandes
   FROM Clients c
   JOIN Commandes co ON c.idClient = co.idClient
   GROUP BY c.idClient
   ORDER BY NombreCommandes DESC
   LIMIT 5
   WITH CHECK OPTION
;
   

Assurez-vous de remplacer les valeurs comme `'idClientSpecifique'`, `'NomCategorieSpecifique'`, `'DateDebut'`, `'DateFin'`, et `'ValeurPoids'` par les valeurs réelles que vous souhaitez analyser.