# IMD - Data Science

## Resumo
- Disciplina: IMD1151 - Ciência de Dados
- Professor: Leonardo Bezerra
- Grupo: Joseane Palhares de Aquino
         Rafael Bezerra da Escóssia Araújo
         Thereza Angélica Moura e Silva
         Wagner Gama

Esse repositório é destinado ao projeto da disciplina Ciência de Dados da Universidade Federal do Rio Grande do Norte. Nesse projeto, será fiscalizado a menção de remédios não eficazes em diários oficiais do município de Natal - Rio Grande do Norte. Para essa finalidade, será utilizado as ferramentas dispostas pelo projeto [querido diário](https://github.com/okfn-brasil/querido-diario) da Open knowledge Brasil.

## Preparação de Ambiente com querido-diario

O primeiro passo do projeto foi a obtenção dos diários oficiais do município de Natal do dia 01/01/2020 (próximo ao início da pandemia) até a data atual. Mas, antes foi necessário a criação de um ambiente de desenvolvimento. Para isso, basta, primeiramente, clonar o repositório do projeto querido-diário [link](https://github.com/okfn-brasil/querido-diario), dirigir-se ao diretório pelo terminal e executar os comandos abaixo:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r data_collection/requirements-dev.txt
$ pre-commit install
```

Desse modo, foi criado um ambiente de desenvolvimento através do virtual-env, ativado e instalado todos os requisitos contido no arquivo requirements-dev.txt.

Após a criação do ambiente virtual e sua ativação, foi executado a aplicação de webscraping para o município de Natal/RN. Para isso, foi preciso dirigir-se para o diretório data_collection e executar o seguinte comando:

```
$ scrapy crawl rn_natal -a start_date=2020-01-01
```

Os PDFs relativos a pesquisa foram coletados e armazenados no diretório data_collection/data. Entretanto, esses PDFs dispõem-se em diversas pastas, com suas respectivas datas. Para facilitar a organização, é desejável que esses PDFs encontrem-se em apenas uma pasta, com nome "pdfs", por exemplo. Para isso, foi executado o seguinte comando no diretório data_collection/data:

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

## Preparação de Ambiente com querido-diario-toolbox

Nesse momento, é necessário ainda a criação de um ambiente de desenvolvimento para o diretório que iremos trabalhar "trabalho-grupo/". Para isso, utilize o gerenciador de ambientes de sua preferência. Com o ambiente virtual criado e ativado, instale a ferramenta do querido-diario-toolbox através do gerenciador de pacotes pip (pip install querido-diario-toolbox). 

Finalizado todos os passos até aqui, finalmente será possível trabalhar em nosso notebook e realizar as fiscalizações propostas no trabalho.

## Fiscalização dos diários oficiais

Nessa altura, já estamos com todo ambiente de desenvolvimento preparado para explorar e analisar as informações dos diários oficiais. De forma resumido, foi utilizado o jupyter lab como interface para o python, seguindo os seguintes passos:

- Importar as bibliotecas devidas e configura-las
- Extrair arquivos .txt e .json (metadados) dos pdfs
- Localizar os documentos que citam os remédios não eficazes
- Estruturar as informações em um arquivo .csv no formato de log (data, nome do documento, remédio citado, número de páginas do documento)
- Gerar visualizações

Nesse primeiro momento, na análise exploratória dos dados, geramos apenas a contagem de quantas vezes certos medicamentos foram citados e como resultado temos:

Observe todo o código através do notebook [link](https://github.com/bezerraescossia/imd-data-science/blob/main/report.ipynb)
