# %%
import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

dfs = pd.read_html(url)

uf = dfs[1]
uf.dtypes


# %%

def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0", "")
            )
    return float(x)

# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)


# %%

def teste(exp:str):
    exp = float(exp.replace(',', '.').replace(' anos', ''))
    return exp

uf['Expectativa de vida (2016)'].apply(teste)


# %%

def alfa(x):
    x = float(x.replace(',','.').replace('%', '')) 
    x /= 100
    return x
uf['Alfabetização (2016)'].apply(alfa)




# %%
def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "")
               .replace(",", ".")
              )
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
# %%
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and 
            linha["IDH (2010)"] > 700)
    
# %%
uf.apply(classifica_bom, axis=1)