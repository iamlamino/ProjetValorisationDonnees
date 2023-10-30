-- Contraintes d'intégrité pour la table Clients
ALTER TABLE Clients
    ADD CONSTRAINT FK_Clients_ville FOREIGN KEY (ville_) REFERENCES Villes(ville),
    ADD CONSTRAINT FK_Clients_pays FOREIGN KEY (pays) REFERENCES Pays(nomPays);

-- Contraintes d'intégrité pour la table Commandes
ALTER TABLE Commandes
    ADD CONSTRAINT FK_Commandes_Client FOREIGN KEY (idClient) REFERENCES Clients(idClient);

-- Contraintes d'intégrité pour la table Categories
ALTER TABLE Categories
    ADD CONSTRAINT PK_Categories PRIMARY KEY (idCategories),
    ADD CONSTRAINT FK_Categories_Mere FOREIGN KEY (idCategorieMere) REFERENCES Categories(idCategories);

-- Contraintes d'intégrité pour la table Produit
ALTER TABLE Produit
    ADD CONSTRAINT PK_Produit PRIMARY KEY (idProduit),
    ADD CONSTRAINT FK_Produit_Categorie FOREIGN KEY (idCategories) REFERENCES Categories(idCategories);

-- Contraintes d'intégrité pour la table LignesCommande
ALTER TABLE LignesCommande
    ADD CONSTRAINT PK_LignesCommande PRIMARY KEY (idCommande, noLigne),
    ADD CONSTRAINT FK_LignesCommande_Commande FOREIGN KEY (idCommande) REFERENCES Commandes(idCommande),
    ADD CONSTRAINT FK_LignesCommande_Produit FOREIGN KEY (idProduit) REFERENCES Produit(idProduit);
