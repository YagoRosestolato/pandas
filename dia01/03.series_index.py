# %%
import pandas as pd

idades = [
    32, 28, 30, 32, 31
]
series_idades = pd.Series(idades)
series_idades


# %%
series_idades[0]
series_idades[len-1]


# %%

series_idades.iloc[0]

# %%

series_idades.iloc[-1]

# %% 

series_idades.iloc[:3]

# %%

idades = [
    32, 28, 30, 32, 31
]

index = [
    "Yago", "Dani", "Luna", "Birita", "Torby"
]

series_idades = pd.Series(idades, index=index)
series_idades

series_idades.iloc[-1]





