import pandas as pd 

dados = {'Vendedor' : ['Naruto', 'Goku', 'Seiya'],
         'Produto': ['Geladeira', 'Fogão', 'Ar Condicionado'],
         'Valor Vendido' : [3400, 750, 2650]}

df = pd.DataFrame(dados)
print(df)