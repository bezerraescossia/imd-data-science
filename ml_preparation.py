# IMPORTANDO BIBLIOTECAS
import pandas as pd

# CARREGANDO E AJUSTANDO DATASET
df = pd.read_csv('data/log.csv')
df = df[['texto']].to_csv('data/ml.csv', index=False)

# INSERINDO LABELS
