CREATE DATABASE E_commerce;
USE E_ommerce;
CREATE TABLE CLIENTS(
   idClient INT,
   prenom VARCHAR(50),
   nom VARCHAR(50),
   email VARCHAR(50),
   telephone INT,
   dateNaissance DATE,
   mdp INT,
   ville VARCHAR(50),
   pays VARCHAR(50),
   PRIMARY KEY(idClient)
);

CREATE TABLE Commandes(
   idCommande INT,
   dateCommande DATE,
   statut VARCHAR(60),
   idClient INT NOT NULL,
   PRIMARY KEY(idCommande),
   FOREIGN KEY(idClient) REFERENCES CLIENTS(idClient)
);

CREATE TABLE CategorieMere(
   idCaterieMere INT,
   PRIMARY KEY(idCaterieMere)
);

CREATE TABLE Categories(
   idCategories INT,
   nomCategorie VARCHAR(50),
   idCaterieMere INT NOT NULL,
   PRIMARY KEY(idCategories),
   FOREIGN KEY(idCaterieMere) REFERENCES CategorieMere(idCaterieMere)
);

CREATE TABLE Produit(
   idProduit INT,
   nomProduit VARCHAR(50),
   prix INT,
   poids INT,
   idCategories INT NOT NULL,
   PRIMARY KEY(idProduit),
   FOREIGN KEY(idCategories) REFERENCES Categories(idCategories)
);

CREATE TABLE LignesCommande(
   idCommande INT,
   noLigne INT,
   quantite INT,
   idProduit INT NOT NULL,
   PRIMARY KEY(idCommande, noLigne),
   FOREIGN KEY(idCommande) REFERENCES Commandes(idCommande),
   FOREIGN KEY(idProduit) REFERENCES Produit(idProduit)
);
