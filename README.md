# Resumo
- **Disciplina**: IMD1151 - Ciência de Dados
- **Ano**: 2021.2
- **Professor**: Leonardo Bezerra [![Open GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/leobezerra?tab=repositories)
- **Grupo**: Joseane Palhares de Aquino, Rafael Bezerra da Escóssia Araújo, Thereza Angélica Moura e Silva, Wagner Gama

Esse repositório é destinado ao projeto da disciplina Ciência de Dados da Universidade Federal do Rio Grande do Norte. Nesse projeto, será fiscalizado a menção de remédios não eficazes em diários oficiais do município de Natal - Rio Grande do Norte. Para essa finalidade, será utilizado as ferramentas dispostas pelo projeto querido diário [![Open GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/okfn-brasil/querido-diario) da Open knowledge Brasil.

# Contextualização
De acordo com o próprio site, a Open Knowledge Brasil (OKBR), também chamada de Rede pelo Conhecimento Livre, é uma Organização da Sociedade Civil (OSC) sem fins lucrativos e apartidária, regida por estatuto. A principal missão da OKBR é desenvolver ferramentas cívicas, projetos, análises de políticas públicas, jornalismo de dados e promover o conhecimento livre nos diversos campos da sociedade. Na esfera política, a organização busca tornar a relação entre governo e sociedade mais próxima e transparente.

Em resumo, a OKBR é uma rede que desenvolve projetos, visando construir uma sociedade mais transparente e inovadora. Nessa perspectiva, um projeto da organização que ganhou grande notoriedade na mídia foi a Operação Serenata de Amor, que é um projeto aberto e colaborativo que utiliza a ciência de dados para fiscalizar os reembolsos efetuados pela Cota para o Exercício da Atividade Parlamentar (CEAP), verba que custeia alimentação, transporte, hospedagem e até despesas com cultura e assinaturas de TV dos deputados federais.

Com o sucesso dessa iniciativa, surgiu a demanda de fiscalizações que transbordem a fronteira de Brasília, que representa apenas uma fatia do orçamento público. Entretanto, ao deparar-se com as esferas municipais, infelizmente, não há muitos dados disponíveis e sem dados não é possível fiscalizar, e é nesse cenário é que surge o projeto Querido Diário.

Sendo assim, o Querido Diário objetiva realizar, na esfera municipal, o mesmo que o projeto Serenata de Amor fez na esfera federal. Entretanto, atualmente, os diários oficiais são as principais fontes de informação sobre as prefeituras, encontrando-se, na maioria das vezes, em um formato não estruturado, o que dificulta a exploração das informações. Nesse cenário, o projeto Querido Diário aparece justamente para “libertar” e centralizar essas informações e torná-las mais acessíveis para fiscalização.

O funcionamento da aplicação, de forma resumida, é baseado na realização de scrapings nos sites oficiais das prefeituras e um posterior tratamento de texto.

Neste trabalho, as ferramentas do projeto Querido Diário serão utilizadas para auxiliar na fiscalização de condutas e na análise de possíveis irregularidades nos municípios do estado do Rio Grande do Norte.

# Objetivos

- Fiscalizar a atuação da pandemia nos municípios do RN, no primeiro momento para Natal;

## Objetivos Específicos

- Investigar menções a remédios não eficazes a covid, além de vacinas;
- Analisar licitações mencionadas nos diários que fazem menção a remédios e vacinas não eficazes;
- Verificar qual área as empresas reportadas nas licitações trabalham.


# Coleta de Dados
## Preparação de Ambiente com querido-diario

O primeiro passo do projeto foi a obtenção dos diários oficiais do município de Natal do dia 01/01/2020 (próximo ao início da pandemia) até a data de escrita desse material (26/11/2021). Mas, antes, foi necessário a criação de um ambiente de desenvolvimento. Para isso, bastou, primeiramente, clonar o repositório do projeto querido-diário [![Open GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/okfn-brasil/querido-diario), dirigir-se ao diretório pelo terminal e executar os comandos abaixo:

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

## Preparação de Ambiente com querido-diario-toolbox

Nesse momento, é necessário ainda a criação de um ambiente de desenvolvimento para o diretório que iremos trabalhar "trabalho-grupo/". Para isso, utilizou-se o gerenciador de ambientes conda, mas qualquer outro poderia ser utilizado. Com o ambiente virtual criado e ativado, instalou-se a ferramenta do querido-diario-toolbox através do gerenciador de pacotes pip (pip install querido-diario-toolbox). 

Finalizado todos os passos até aqui, finalmente foi possível trabalhar em nosso notebook e realizar as fiscalizações propostas no trabalho.

# Análise Exploratória de Dados

Nessa altura, já estamos com todo ambiente de desenvolvimento preparado para explorar e analisar as informações dos diários oficiais. De forma resumido, foi utilizado o jupyter lab como interface para o python, seguindo os seguintes passos:

- Importar as bibliotecas devidas e configurá-las
- Extrair arquivos .txt e .json (metadados) dos pdfs
- Localizar os documentos que citam os remédios não eficazes
- Estruturar as informações em um arquivo .csv no formato de log (data, nome do documento, remédio citado, número de páginas do documento)
- Gerar visualizações

Nesse primeiro momento, na análise exploratória dos dados, geramos apenas a contagem de quantas vezes certos medicamentos foram citados e como resultado temos:

![alt text](https://github.com/bezerraescossia/imd-data-science/blob/main/imagem.jpg?raw=true)

Observe todo o código através do [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/bezerraescossia/imd-data-science/blob/main/report.ipynb)
