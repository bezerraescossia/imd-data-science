# Resumo
- Disciplina: IMD1151 - Ciência de Dados
- Professor: [Leonardo Bezerra](https://github.com/leobezerra?tab=repositories)
- Grupo: Joseane Palhares de Aquino, Rafael Bezerra da Escóssia Araújo, Thereza Angélica Moura e Silva, Wagner Gama

Esse repositório é destinado ao projeto da disciplina Ciência de Dados da Universidade Federal do Rio Grande do Norte. Nesse projeto, será fiscalizado a menção de remédios não eficazes em diários oficiais do município de Natal - Rio Grande do Norte. Para essa finalidade, será utilizado as ferramentas dispostas pelo projeto [querido diário](https://github.com/okfn-brasil/querido-diario) da Open knowledge Brasil.

# Preparação de Ambiente com querido-diario

O primeiro passo do projeto foi a obtenção dos diários oficiais do município de Natal do dia 01/01/2020 (próximo ao início da pandemia) até a data de escrita desse material (26/11/2021). Mas, antes, foi necessário a criação de um ambiente de desenvolvimento. Para isso, bastou, primeiramente, clonar o repositório do [projeto querido-diário](https://github.com/okfn-brasil/querido-diario), dirigir-se ao diretório pelo terminal e executar os comandos abaixo:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r data_collection/requirements-dev.txt
$ pre-commit install
```

Desse modo, foi criado um ambiente de desenvolvimento através do virtual-env, ativado e instalado todos os requisitos contidos no arquivo requirements-dev.txt.

Após a criação do ambiente virtual e sua ativação, foi executado a aplicação de webscraping para o município de Natal/RN. Para isso, foi preciso dirigir-se para o diretório data_collection e executar o seguinte comando:

```
$ scrapy crawl rn_natal -a start_date=2020-01-01
```
[imagem]

Os PDFs relativos a pesquisa foram coletados e armazenados no diretório data_collection/data. Entretanto, esses PDFs dispõem-se em diversas pastas (ver imagem acima), com suas respectivas datas. Para facilitar a organização, é desejável que esses PDFs encontrem-se em apenas uma pasta, com nome "pdfs", por exemplo. Para isso, foi executado o seguinte comando no diretório data_collection/data:

```
find . -name '*.pdf' -exec mv -t ./pdfs {} +
```

Logo após, foi criada uma pasta relativa ao trabalho do grupo, ficando com a seguinte estrutura:

```
data-science/
├─ querido-diario/ (repositório utilizado na obtenção dos diários oficiais)
├─ trabalho-grupo/
```

A pasta "pdf" foi então movida de querido-diario/data_collection/data para trabalho-grupo/data.

# Preparação de Ambiente com querido-diario-toolbox

Nesse momento, é necessário ainda a criação de um ambiente de desenvolvimento para o diretório que iremos trabalhar "trabalho-grupo/". Para isso, utilizou-se o gerenciador de ambientes conda, mas qualquer outro poderia ser utilizado. Com o ambiente virtual criado e ativado, instalou-se a ferramenta do querido-diario-toolbox através do gerenciador de pacotes pip (pip install querido-diario-toolbox). 

Finalizado todos os passos até aqui, finalmente foi possível trabalhar em nosso notebook e realizar as fiscalizações propostas no trabalho.

# Fiscalização dos diários oficiais

Nessa altura, já estamos com todo ambiente de desenvolvimento preparado para explorar e analisar as informações dos diários oficiais. De forma resumido, foi utilizado o jupyter lab como interface para o python, seguindo os seguintes passos:

- Importar as bibliotecas devidas e configurá-las
- Extrair arquivos .txt e .json (metadados) dos pdfs
- Localizar os documentos que citam os remédios não eficazes
- Estruturar as informações em um arquivo .csv no formato de log (data, nome do documento, remédio citado, número de páginas do documento)
- Gerar visualizações

Nesse primeiro momento, na análise exploratória dos dados, geramos apenas a contagem de quantas vezes certos medicamentos foram citados e como resultado temos:

![alt text](https://github.com/bezerraescossia/imd-data-science/blob/main/imagem.jpg?raw=true)

Observe todo o código através do [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/bezerraescossia/imd-data-science/blob/main/report.ipynb)
