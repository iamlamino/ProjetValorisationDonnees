USE ecommerce;

##Relations clients par simple création puis renommage en SQL
create table clients  select *  from customers 
### AJOUT DE LA COLONE VILLES 
ALTER TABLE clients add column ville VARCHAR (37)

### Ajout de la colone PAYS 
ALTER TABLE clients add column PAYS as region VARCHAR (44)

### AJOUT DE LA COLONE MOT DE PASSE 
ALTER TABLE clients add column mdp varchar(40)





