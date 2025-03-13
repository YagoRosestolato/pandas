# %%

import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv')
df_clientes

# %%

df_clientes.head(10) #Mostra as 10 primeiras linhas do dataset


# %%

df_clientes.tail() #Mostra as 5 linhas finais do dataset


# %%

df_clientes.sample(10) #Mostra 10 linhas aleatorias

# %%

df_clientes.shape # Mostra a quantidade de linhas e colunas

print(f'A tabela tem {df_clientes.shape[0]} linhas e {df_clientes.shape[1]} colunas ')

# %%

df_clientes.columns #Mostra todas as colunas do dataset

# %%

df_clientes.info(memory_usage='deep')

# %%

df_clientes.dtypes #Uma serie que mostra o valor da tipagem de cada coluna


