create DATABASE e_commerce;
use e_commerce;
CREATE TABLE Clients (
    idClient INT PRIMARY KEY,
    prénom VARCHAR(255),
    nom VARCHAR(255),
    email VARCHAR(255),
    telephone VARCHAR(255),
    dateNaissance DATE,
    mdp VARCHAR(255),
    ville VARCHAR(255),
    pays VARCHAR(255)
);

CREATE TABLE Categories (
    idCategorie INT PRIMARY KEY,
    nomCategorie VARCHAR(255),
    idCategorieMere INT,
    FOREIGN KEY (idCategorieMere) REFERENCES Categories(idCategorie)
);

CREATE TABLE Produits (
    idProduit INT PRIMARY KEY,
    nomproduit VARCHAR(255),
    prix DECIMAL(10, 2),
    poids DECIMAL(10, 2),
    idCategorie INT,
    FOREIGN KEY (idCategorie) REFERENCES Categories(idCategorie)
);

CREATE TABLE Commandes (
    idCommande INT PRIMARY KEY,
    idClient INT,
    dateCommande DATE,
    statut VARCHAR(255),
    FOREIGN KEY (idClient) REFERENCES Clients(idClient)
);

CREATE TABLE LignesCommandes (
    idCommande INT,
    noligne INT,
    idProduit INT,
    quantité INT,
    PRIMARY KEY (idCommande, noligne),
    FOREIGN KEY (idCommande) REFERENCES Commandes(idCommande),
    FOREIGN KEY (idProduit) REFERENCES Produits(idProduit)
);