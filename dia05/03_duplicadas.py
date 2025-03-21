# %%
import pandas as pd

# %%

df = pd.DataFrame({
    'nome': ['Paulo', 'Roberto', 'Cesar', 'Carlos', 'Daniel', 'Teo'],
    'sobrenome': ['Silva', 'Moreira', 'Pereira', 'Silva', 'Moreira', 'Guimarães'],
    'salario': [2132, 1231, 454, 6543, 6532, 4322]
})

df.sort_values('nome')