# %%

import pandas as pd 

df = pd.read_csv('../data/clientes.csv')
df.shape


# %%

df.info()


# %%

df = pd.read_csv('../data/produtos.csv')
df.info()