var = [select * from product]
for i in mes :
    nameC = i.categorieProduit.splite('|')
    [select* from product p, categorie c 
     where c.categorieProduit like"%:nameC" and c.nomcategorie =:nameC]
    
    SELECT * 
   FROM products p,categories c 
   WHERE p.categorieProduit = "categorieProduit" And c.nomCategorie = "nomCategorie" ;*


   var = [select * from product]
    for i in mes :
        nameC = i.categorieProduit.splite('|')
        [select* from product p, categorie c 
        where c.categorieProduit like"%:nameC" and c.nomcategorie =:nameC]