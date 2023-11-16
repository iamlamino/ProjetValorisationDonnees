-- REQUETES DE LA SEMAINE 3

--T1 


CREATE TABLE clients (
  idClients VARCHAR(255),
  prenom VARCHAR(255),
  nom VARCHAR(255),
  email VARCHAR(255),
  dateNaissance DATE,
  ville VARCHAR(37),
  pays VARCHAR(44),
  mdp VARCHAR(40)
);

INSERT INTO clients (idClients, prenom, nom, email, dateNaissance)
SELECT `User id`, `First Name`, `Last Name`, `Email`, `Date of birth`
FROM customers;


--T2 T3 T4 T5  

CREATE TABLE Catégories(
   idCategorie INT,
   nomCategorie VARCHAR(50) NOT NULL,
   idCategorieMere VARCHAR(50) NOT NULL,
   PRIMARY KEY(idCategorie)
);


CREATE TABLE LignesCommande(
   idCommande VARCHAR(50),
   noLigne INT NOT NULL,
   idProduit VARCHAR(50) NOT NULL,
   quantité INT NOT NULL,
   PRIMARY KEY(idCommande)
);

CREATE TABLE Produits(
   idProduit INT,
   idCategorie VARCHAR(50),
   nomproduit VARCHAR(50) NOT NULL,
   prix INT NOT NULL,
   poids DECIMAL(15,2) NOT NULL,
   idCommande VARCHAR(50) NOT NULL,
   PRIMARY KEY(idProduit, idCategorie),
   FOREIGN KEY(idCommande) REFERENCES LignesCommande(idCommande)
);

CREATE TABLE Commandes(
   idCommandes INT,
   idClient INT,
   dateCommande DATE NOT NULL,
   statut VARCHAR(50) NOT NULL,
   idClient_1 INT NOT NULL,
   idCommande VARCHAR(50) NOT NULL,
   PRIMARY KEY(idCommandes, idClient),
   FOREIGN KEY(idClient_1) REFERENCES Clients(idClient),
   FOREIGN KEY(idCommande) REFERENCES LignesCommande(idCommande)
);

CREATE TABLE appartenir(
   idProduit INT,
   idCategorie VARCHAR(50),
   idCategorie_1 INT,
   PRIMARY KEY(idProduit, idCategorie, idCategorie_1),
   FOREIGN KEY(idProduit, idCategorie) REFERENCES Produits(idProduit, idCategorie),
   FOREIGN KEY(idCategorie_1) REFERENCES Catégories(idCategorie)
);

