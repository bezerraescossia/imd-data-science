# IMD - Data Science

## Resumo
- Disciplina: IMD1151 - Ciência de Dados
- Professor: Leonardo Bezerra
- Grupo: Joseane Palhares de Aquino
         Rafael Bezerra da Escóssia Araújo
         Thereza Angélica Moura e Silva
         Wagner Gama

Esse repositório é destinado ao projeto da disciplina Ciência de Dados da Universidade Federal do Rio Grande do Norte. Nesse projeto, será fiscalizado a menção de remédios não eficazes em diários oficiais do município de Natal - Rio Grande do Norte. Para essa finalidade, será utilizado as ferramentas dispostas pelo projeto [querido diário](https://github.com/okfn-brasil/querido-diario) da Open knowledge Brasil.

## Obtenção dos Diários Oficiais

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

Dessa forma, finaliza-se a obtenção e organização dos diários oficiais.

## Transformação dos diários para .txt
