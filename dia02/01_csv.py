# %%
import pandas as pd


df = pd.read_csv('../data/clientes.csv')

df

# %%

df.to_csv("clientes.csv", index=False) #Salva o arquivo


# %%

df.to_parquet('clientes.parquet', index=False)


# %%

df.to_excel('clientes.xlsx', index=False)

# %%

df2 = pd.read_excel('clientes.xlsx')