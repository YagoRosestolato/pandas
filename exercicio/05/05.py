# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
# %%
import pandas as pd

df = pd.read_csv('../../data/clientes.csv')
df["twitch_points"] = df["qtdePontos"] * df["flTwitch"]
df.head()


# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
# 05.05 - Selecione a primeira transação diária de cada cliente.
