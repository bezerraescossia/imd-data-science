# Importações e Configurações
import os
import shutil
from os import listdir
from querido_diario_toolbox import Gazette
from querido_diario_toolbox.etl.text_extractor import create_text_extractor
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