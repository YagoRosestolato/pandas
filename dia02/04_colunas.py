# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')

df

# %%

df.shape

# %%

df.info(memory_usage='deep')

# %%

df.dtypes

# %%

df = df.rename(columns={'qtdePontos': 'qtPontos'})

# %%
df[['idCliente', 'qtPontos']]


# %%
#SELECT idCliente from df
df[['idCliente']]
# %%
#SELECT idCliente, qtPontos from df LIMIT 5
df[['idCliente', 'qtPontos']].head()

# %%

# SELECT idCliente, idTransacao, qtPontos from df LIMIT 5

df[['idCliente','idTransacao', 'qtPontos']].head(5)

# %%
#Ordenando colunas
colunas = list(df.columns)
colunas.sort()

colunas

df = df[colunas]
df