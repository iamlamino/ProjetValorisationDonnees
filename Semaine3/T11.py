import pandas as pd

df = pd.read_csv('../CSV/produits.csv', on_bad_lines='skip', sep=",")
df = df.dropna()
df.replace(to_replace='\$', value='', regex=True, inplace=True)
df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

def convert_weights(weight):
    if isinstance(weight, str):
        if 'pounds' in weight:
            return float(weight.replace(' pounds', ''))
        elif 'ounces' in weight:
            return float(weight.replace(' ounces', '')) * 0.0625
        else:
            return weight
    return weight

df['poidsExpedition'] = df['poidsExpedition'].apply(convert_weights)

df["venteAmazone"] = df["venteAmazone"] .replace({'Y':1,'N':0}) 



df.to_csv('../CSV/produits.csv', index=False)

#df['prix'] = df['prix'].str.replace('$', '', regex=True)


"""for col in df.columns:
    print(col)
    print(len(col))
"""