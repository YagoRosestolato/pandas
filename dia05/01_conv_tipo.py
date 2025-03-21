# %%
import pandas as pd
# %%

df = pd.read_csv('../data/clientes.csv')
df

# %%

df ['qtdePontos'].astype(float)

# %%

df['dtCriacao'].replace({
    '0000-00-00 00:00:00.000': '2025-03-19 09:00:00.000'
})

# %%

pd.to_datetime(df['dtCriacao']) 