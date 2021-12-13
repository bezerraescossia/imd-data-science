# IMPORTANDO BIBLIOTECAS
import os
import json
from os import listdir
import nltk
import pandas as pd

# ESTRUTURANDO TABELA PARA EDA
## Ivermectina
with open ('log.csv', 'w') as csv:
    csv.write('filename;cod_ibge_municipio;cod_ibge_estado;data;texto;remedio\n')
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'IVERMECTINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        tokens = nltk.sent_tokenize(text)
                        for token in tokens:
                            token.replace(',', ' ')
                            token.replace('\n', ' ')
                            try:
                                if 'IVERMECTINA' in token:
                                    text = json.loads(js.read())
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + text['date'] + ';' + token +';' +'ivermectina\n')
                            
                            except:
                                if 'IVERMECTINA' in token:
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + 'Não Informado' + ';' + token + ';' +'ivermectina\n')

## Cloroquina
with open ('log.csv', 'a') as csv:
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'CLOROQUINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        tokens = nltk.sent_tokenize(text)
                        for token in tokens:
                            token.replace(',', ' ')
                            token.replace('\n', ' ')
                            try:
                                if 'CLOROQUINA' in token:
                                    text = json.loads(js.read())
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + text['date'] + ';' + token + ';' +'cloroquina\n')
                            except:
                                if 'CLOROQUINA' in token:
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + 'Não Informado' + ';' + token + ';' +'cloroquina\n')

## Hidroxicloroquina
with open ('log.csv', 'a') as csv:
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'HIDROXICLOROQUINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        tokens = nltk.sent_tokenize(text)
                        for token in tokens:
                            token.replace(',', ' ')
                            token.replace('\n', ' ')
                            try:
                                if 'HIDROXICLOROQUINA' in token:
                                    text = json.loads(js.read())
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + text['date'] + ';' + token + ';' +'hidroxicloroquina\n')
                            
                            except:
                                if 'HIDROXICLOROQUINA' in token:
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + 'Não Informado' + ';' + token + ';' +'hidroxicloroquina\n')

## Azitromicina
with open ('log.csv', 'a') as csv:
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'HIDROXICLOROQUINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        tokens = nltk.sent_tokenize(text)
                        for token in tokens:
                            token.replace(',', ' ')
                            token.replace('\n', ' ')
                            try:
                                if 'AZITROMICINA' in token:
                                    text = json.loads(js.read())
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + text['date'] + ';' + token + ';' +'azitromicina\n')
                            
                            except:
                                if 'AZITROMICINA' in token:
                                    csv.write(file + ';' + folder + ';' + folder[:2] + ';' + 'Não Informado' + ';' + token + ';' +'azitromicina\n')

## Inserindo os nomes das cidades e estados
df = pd.read_csv('log.csv')
municipios = pd.read_csv('data/codigo_municipio.csv')
municipios['codigo'] = municipios['codigo'].astype(object)
df = pd.merge(df, municipios, how='left', left_on='cod_ibge_municipio', right_on='codigo')

estados = pd.read_csv('data/codigo_estado.csv')
estados['codigo'] = estados['codigo'].astype(object)
df = pd.merge(df, estados, how='left', left_on='cod_ibge_estado', right_on='codigo')


df[['filename', 'data', 'municipio', 'estado', 'remedio', 'texto']].to_csv('log.csv', index=False)