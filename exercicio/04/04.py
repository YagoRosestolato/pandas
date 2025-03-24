
# %%
# 04.01 - Quantos clientes tem vínculo com a Twitch?
import pandas as pd

df = pd.read_csv('../../data/clientes.csv')
filtro = df['flTwitch'] == 1
clientes = df[filtro].shape[0]
print(f'Temos {clientes} com vínculo na twitch')



# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

maior_queMil = df['qtdePontos'] > 1000
maior = df[maior_queMil].shape[0] 
print(f'Existem {maior} clientes com saldo acima de 1000')


# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
import pandas as pd

df = pd.read_csv('../../data/transacoes.csv')

filtro = (df['dtCriacao'] >= '2025-02-01') & (df['dtCriacao'] < '2025-02-02')
data = df[filtro].shape[0]
data
