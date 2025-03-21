# %%

import pandas as pd


df = pd.read_csv('../data/transacoes.csv')
df.head()


# %%

filtro = df['qtdePontos'] >= 50

df[filtro].shape


# %%

filtro = (df['qtdePontos'] >= 50) & (df['qtdePontos'] < 100)

df[filtro]

# %%

filtro = (df['qtdePontos'] == 1) | (df['qtdePontos'] == 100)

df[filtro]


# %%

filtro = (df['qtdePontos'] > 0 ) & (df['qtdePontos'] <= 50) & (df['dtCriacao'] >= '2025-01-01') 

df[filtro]