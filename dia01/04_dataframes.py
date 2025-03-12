# %%

import pandas as pd

idades = [
    32, 28, 30, 32, 31
]

nomes = [
    "Yago", "Dani", "Luna", "Birita", "Torby"
]


series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)


# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df 



# %%
df["nomes"]
df.iloc[0] #Retorna uma series


# %%

df.iloc[-1]["idades"]