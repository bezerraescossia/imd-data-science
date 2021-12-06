# Importações e Configurações
import os
import json
import shutil
from os import listdir
import pandas as pd
import glob
import seaborn as sns
from querido_diario_toolbox import Gazette
from querido_diario_toolbox.etl.text_extractor import create_text_extractor
import matplotlib.pyplot as plt
config = {"apache_tika_jar": "tika-app-1.24.1.jar"}
extrator = create_text_extractor(config)

# Extraindo .txt
for folder in listdir("data_raw"):
    os.mkdir(os.path.join('data_raw', folder, 'txt'))
    for file in listdir(os.path.join('data_raw', folder, 'pdfs')):
        if (file[:-4] + '.txt') not in listdir(os.path.join('data_raw', folder, 'txt')):
            try:
                with open(os.path.join('data_raw', folder, 'pdfs', file)) as f:
                    diario = Gazette(filepath=os.path.join('data_raw', folder, 'pdfs', file))
                    extrator.extract_text(diario)
                shutil.move(os.path.join('data_raw', folder, 'pdfs', file[:-4]) + '.txt', os.path.join('data_raw', folder, 'txt', file[:-4]) + '.txt')
            except:
                continue

# Extraindo metadados
for folder in listdir("data_raw"):
    os.mkdir(os.path.join('data_raw', folder, 'json'))
    for file in listdir(os.path.join('data_raw', folder, 'pdfs')):
        if (file[:-4] + '.json') not in listdir(os.path.join('data_raw', folder, 'json')):
            try:
                with open(os.path.join('data_raw', folder, 'pdfs', file)) as f:
                    diario = Gazette(filepath=os.path.join('data_raw', folder, 'pdfs', file))
                    extrator.extract_metadata(diario)
                shutil.move(os.path.join('data_raw', folder, 'pdfs', file[:-4]) + '.json', os.path.join('data_raw', folder, 'json', file[:-4]) + '.json')
            except:
                continue

# Encontrando Palavras Chaves
## Ivermectina
with open ('log.csv', 'w') as csv:
    csv.write('filename,cod_ibge_municipio,cod_ibge_estado,data,remedio\n')
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'IVERMECTINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        try:
                            text = json.loads(js.read())
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + text['date'] + ',' +'ivermectina\n')
                            print(folder, file)
                        except:
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + 'Não Informado' + ',' +'ivermectina\n')
                            print(f'Arquivo com erro {folder, file}')

## Cloroquina
with open ('log.csv', 'a') as csv:
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'CLOROQUINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        try:
                            text = json.loads(js.read())
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + text['date'] + ',' +'cloroquina\n')
                            print(folder, file)
                        except:
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + 'Não Informado' + ',' +'cloroquina\n')
                            print(f'Arquivo com erro {folder, file}')

## Hidroxicloroquina
with open ('log.csv', 'a') as csv:
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'HIDROXICLOROQUINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        try:
                            text = json.loads(js.read())
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + text['date'] + ',' +'hidroxicloroquina\n')
                            print(folder, file)
                        except:
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + 'Não Informado' + ',' +'hidroxicloroquina\n')
                            print(f'Arquivo com erro {folder, file}')

## Azitromicina
with open ('log.csv', 'a') as csv:
    for folder in listdir("data_raw"):
        for file in listdir(os.path.join('data_raw', folder, 'txt')):
            with open(os.path.join('data_raw', folder, 'txt', file)) as currentFile:
                text = currentFile.read().upper()
                if 'AZITROMICINA' in text:
                    with open(os.path.join('data_raw', folder, 'json', file[:-4]) + '.json') as js:
                        try:
                            text = json.loads(js.read())
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + text['date'] + ',' +'azitromicina\n')
                            print(folder, file)
                        except:
                            csv.write(file + ',' + folder + ',' + folder[:2] + ',' + 'Não Informado' + ',' +'azitromicina\n')
                            print(f'Arquivo com erro {folder, file}')