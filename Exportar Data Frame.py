import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'Dias1e2.xlsx'
arquivo_excel_2 = 'Dias3.xlsx'

# Ler o conteúdo e mandar para a variável => Data Frame df
df_dia_1 = pd.read_excel(arquivo_excel_1,sheet_name='dia 1')
df_dia_2 = pd.read_excel(arquivo_excel_1,sheet_name='dia 2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

#print(df_dia_1)

df_todas_planilhas = pd.concat([df_dia_1,df_dia_2,df_dia_3])

print(df_todas_planilhas)

#df_todas_planilhas.to_excel('consolidado.xlsx')

#print(df_todas_planilhas['Vendedor'])

lucro_dos_vendedores = df_todas_planilhas.groupby(['Vendedor']).sum()
#print(lucro_dos_vendedores)

relatorio_bonito = lucro_dos_vendedores.loc[:, "Unidade": "Preço"]
print(relatorio_bonito)

relatorio_bonito.plot(kind = "bar")
plt.show()