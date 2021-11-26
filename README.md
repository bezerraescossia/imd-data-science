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

Inicialmente, é necessário a obtenção de todos os diários oficiais do município de Natal, desde datas próximas ao início da pandemia. Nesse trabalho, capturamos a partir do dia 01/01/2020. Para a obtenção desses PDFs, o projeto querido diário já disponibiliza uma aplicação de webscraping. Portanto, seguindo os codigos abaixo (sugeridos pelo próprio querido diário)

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r data_collection/requirements-dev.txt
$ pre-commit install
```
