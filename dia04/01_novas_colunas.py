# %% 

import pandas as pd

df = pd.read_csv('../data/clientes.csv')
df.head()


# %%


df["pontos_100"] = df['qtdePontos'] + 100

df.head()
# %%

df['qtdePontos'] + 100


# %%

