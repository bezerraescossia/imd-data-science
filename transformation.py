import pandas as pd

df = pd.read_csv('data/raw_log.csv')
df.head()

municipios = pd.read_csv('data/codigo_municipio.csv')
municipios.head()

df = pd.merge(df, municipios, how='left', left_on='cod_ibge_municipio', right_on='codigo')

estados = pd.read_csv('data/codigo_estado.csv')
estados.head()

df = pd.merge(df, estados, how='left', left_on='cod_ibge_estado', right_on='codigo')

df[['filename', 'data', 'municipio', 'estado', 'remedio']].to_csv('log.csv', index=False)