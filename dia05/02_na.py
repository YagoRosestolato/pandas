# %%
import pandas as pd

# %%

clientes = pd.read_csv('../data/clientes.csv')
clientes

# %%

clientes.dropna()

# %%

df = pd.DataFrame(
    {
        'nome':['Pessoa1', None, 'Pessoa2', ' Pessoa3'],
        'idade':[None, None,26, 6],
        'salario': [34354, 43545, None, 43545]
    }
)

df.dropna(how='all', subset=['idade'])

# %%

df['idade'].fillna(0).astype(int)