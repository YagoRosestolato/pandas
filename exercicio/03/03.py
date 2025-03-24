# 03.01 - Quantas linhas há no arquivo clientes.csv ?
# %%
import pandas as pd

df = pd.read_csv('../../data/clientes.csv')

print(f'A tabela de clientes tem {df.shape[0]} linhas')

# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
# df.types
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
df.info()
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
# %%

import pandas as pd

df = pd.read_csv('../../data/clientes.csv')

df = df.loc[4]['idCliente']
df

print(f'O ID do cliente no inde 4 é {df}')





# %%
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?
import pandas as pd

df = pd.read_csv('../../data/clientes.csv')

df = df.iloc[9]['qtdePontos']

df







