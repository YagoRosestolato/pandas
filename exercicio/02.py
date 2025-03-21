# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')
df

# %%

df['nova_coluna']  = 1
df.to_csv('transacoes.csv', index=False)

