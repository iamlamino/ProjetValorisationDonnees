import pandas as pd

df = pd.read_csv('../CSV/customers.csv')
df = df.dropna()
#df.rename(columns={'sex': 'sexe'}, inplace=True)

#df['sexe'] = df['sexe'].replace({'Male': 'Homme', 'Female': 'Femme'})
df.to_csv('../CSV/clients.csv', index=False)
