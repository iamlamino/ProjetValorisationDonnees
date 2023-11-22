# liste des colonnes de la tables lignes de commandes 
import pandas as pd
datas = []
columns = ['idCommande','noligne','idProduit','quantite'] 
index = [0,1,2,3]
  
# creation de la table  
lignesCommandes = pd.DataFrame(columns) 

# affichage
print(lignesCommandes)

# transformation en fichier csv 
lignesCommandes.to_csv('lignesCommandes.csv')
  