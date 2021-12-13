# IMPORTANDO BIBLIOTECAS
import pandas as pd

# CARREGANDO E AJUSTANDO DATASET
df = pd.read_csv('data/log.csv')
df[df['texto'].str.contains('COVID') | df['texto'].str.contains('CORONA') | df['texto'].str.contains('PANDEMIA')].reset_index(drop=True).to_csv('data/ml.csv', index=False)

# INSERINDO LABELS
