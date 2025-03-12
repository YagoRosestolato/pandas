# %%
idades = [
    32, 28, 30, 32, 31
]


media = sum(idades)/len(idades)

print(media)


diffs = 0 

for i in idades:
    diffs += (i - media) ** 2
    
variancia = diffs / (len(idades)-1)
variancia

# %%

import pandas as pd

series_idades = pd.Series(idades)
media_idade = series_idades.mean() #média
var_idades = series_idades.var() # Variancia
summary_idades = series_idades.describe() # Gera estastiticas resumidas

print(media_idade)
print(var_idades)
print(summary_idades)







