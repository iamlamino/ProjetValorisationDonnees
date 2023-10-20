import pandas as pd

df = pd.read_csv('../CSV/villes.csv')
df = df.dropna()

df.to_csv('../CSV/clients.csv', index=False)

