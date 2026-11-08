# Mini-Projeto Avaliativo — Análise Exploratória de Dados (AED) da Base Varejo Kaggle

**Disciplina:** Visualização de Dados e Business Intelligence
**Curso:** CARREIRA TECH SCTEC - SENAI/SC - Lab 365 (Módulo: M1S07)
**Professor:** Rodrigo Garcia Brunini
**Aluna:** Natali Caroline de Miranda Stoquera
**Turma:** VDBIT1

---

# 1. Objetivo do Projeto

O objetivo deste mini-projeto foi aplicar conceitos de Análise Exploratória de Dados (AED) em uma base de varejo, realizando a identificação de problemas de qualidade, limpeza dos dados, transformação de tipos, geração de estatísticas descritivas e análise de padrões de compra.

A proposta busca simular atividades comuns na rotina de profissionais de Business Intelligence e Análise de Dados, demonstrando como transformar dados brutos em informações úteis para apoio à tomada de decisão.

---

# 2. Base de Dados Utilizada

Base de dados: **Varejo**

Fonte:

https://www.kaggle.com/datasets/namespaiva/base-varejo/data

A base contém informações relacionadas a compras realizadas em um estabelecimento varejista, incluindo:

* Data da compra;
* Número da compra (nota fiscal);
* Cliente;
* Gênero;
* Estado civil;
* Número de filhos;
* Segmentação econômica;
* Produto adquirido;
* Categoria do produto.

---

# 3. Etapas Desenvolvidas

## Sprint 1 — Importação dos Dados

Nesta etapa foi realizado o carregamento do arquivo CSV utilizando a biblioteca pandas.

Também foram exibidas informações básicas da base:

* Quantidade de registros;
* Quantidade de colunas;
* Tipos de dados;
* Amostra inicial dos registros.

---

## Sprint 2 — Transformação de Tipos

Foi realizada a padronização dos tipos de dados para garantir maior consistência nas análises.

Principais transformações:

* Conversão da coluna DATA para o tipo datetime;
* Padronização das colunas textuais;
* Conversão das colunas numéricas para formato adequado;
* Verificação da regra de negócio do identificador CO_ID.

---

## Sprint 3 — Limpeza de Dados

Foram identificados e tratados problemas de qualidade presentes na base.

Tratamentos realizados:

### Remoção de colunas desnecessárias

Foram removidas colunas "Unnamed", geradas automaticamente durante a exportação do arquivo.

### Tratamento de categorias inválidas

Os registros com valor "#N/D" na coluna PR_CAT foram substituídos por "Sem Categoria".

Essa decisão foi adotada porque a venda ocorreu normalmente e apenas a categoria estava ausente. Remover esses registros resultaria em perda de informações válidas.

### Remoção de duplicatas

Foram eliminados registros duplicados para evitar distorções nas análises e nos agrupamentos.

---

## Sprint 4 — Estatística Descritiva

Foi realizada análise estatística da coluna CL_FHL (Número de Filhos).

Indicadores calculados:

* Média;
* Mediana;
* Moda;
* Desvio padrão;
* Valor mínimo;
* Valor máximo;
* Contagem de registros.

Essas métricas ajudam a compreender o perfil familiar dos clientes presentes na base.

---

## Sprint 5 — Agrupamentos e Análises

Foram realizados agrupamentos para identificar padrões de comportamento.

### Agrupamento por Gênero

Permitiu identificar qual gênero concentrou maior volume de compras.

### Agrupamento por Categoria

Permitiu identificar quais categorias possuem maior participação nas vendas.

### Cruzamento Segmento Econômico × Gênero

Utilizando tabela dinâmica (pivot table), foi possível visualizar a distribuição dos clientes entre segmentos econômicos e gênero.

---

## Sprint 6 — Relatório Final e Exportação

Ao final do processo foi gerado:

* Relatório consolidado no terminal;
* Arquivo CSV limpo e padronizado;
* Principais insights obtidos durante a análise.

---

# 4. Problemas Encontrados na Base

Durante a análise foram identificados os seguintes problemas:

* Registros duplicados;
* Categorias com valor "#N/D";
* Colunas extras "Unnamed";
* Coluna DATA armazenada como texto;
* Necessidade de validação dos identificadores de compra.

Esses problemas poderiam comprometer a qualidade das análises caso não fossem tratados adequadamente.

---

# 5. Principais Insights Obtidos

## 1. Categoria Líder

A categoria de produtos com maior volume de vendas foi a categoria líder da base analisada.

Esse resultado pode auxiliar decisões relacionadas a estoque, reposição e ações promocionais.

---

## 2. Perfil de Compras

Foi identificado um gênero predominante no volume de compras registrado.

Esse tipo de informação pode apoiar futuras estratégias de segmentação de campanhas e comunicação.

---

## 3. Número de Filhos dos Clientes

A mediana e a moda da quantidade de filhos foram iguais a zero.

Isso indica que a maior parte dos clientes não possui filhos.

Ao mesmo tempo, a média superior a zero sugere a existência de grupos familiares que realizam compras em maior volume.

---

## 4. Segmentação Econômica

A Classe B apresentou maior participação nas compras registradas.

Esse resultado indica que esse segmento representa o principal público consumidor da base analisada.

---

## 5. Qualidade dos Dados

A remoção de duplicidades e o tratamento de inconsistências contribuíram para uma base mais confiável e adequada para análises futuras.

---

## 6. Limitação da Base

A base não possui informações financeiras como preço ou valor total das compras.

Por esse motivo, não foi possível calcular indicadores como:

* Receita;
* Ticket médio;
* Faturamento;
* Margem de lucro.

---

# 6. Reflexão Teórica

## O que é ETL?

ETL significa:

### Extract (Extração)

Consiste em obter os dados da fonte original.

Neste projeto, essa etapa ocorreu durante a leitura do arquivo CSV.

### Transform (Transformação)

Corresponde ao tratamento dos dados.

Nesta etapa foram realizadas:

* Conversão de tipos;
* Padronização de textos;
* Tratamento de categorias inválidas;
* Remoção de duplicatas.

### Load (Carga)

Consiste em disponibilizar os dados tratados para utilização posterior.

Neste projeto, a carga foi realizada por meio da exportação do arquivo CSV limpo.

---

## Importância da Qualidade dos Dados

A qualidade dos dados influencia diretamente a qualidade das análises.

Registros duplicados, valores incorretos ou informações ausentes podem gerar interpretações equivocadas e impactar a tomada de decisões.

Por esse motivo, a etapa de limpeza é considerada uma das mais importantes dentro de um processo de análise de dados.

---

# 7. Estrutura do Projeto

```
Miniprojeto_NataliStoquera_VDBIT1/

├── Base Varejo.csv
├── script_NataliStoquera_VDBIT1.py
├── df_limpo_NataliStoquera_VDBIT1.csv
└── README_NataliStoquera_VDBIT1.md
```

---

# 8. Aprendizados e Boas Práticas Aplicadas

Durante o desenvolvimento deste mini-projeto foram aplicados conhecimentos adquiridos ao longo da disciplina, bem como boas práticas de programação, análise de dados e versionamento.

## Reutilização e Evolução de Código

Parte da estrutura utilizada neste projeto foi inspirada em um mini-projeto anterior desenvolvido em grupo, denominado **"Limpeza de Dados de Vendas da Zé Pequeno LTDA"**, realizado pela equipe **Django Livre**.

A reutilização ocorreu principalmente em aspectos estruturais do código, tais como:

* Organização por etapas (Sprints);
* Utilização de funções (`def`) para modularização;
* Definição de constantes e configurações iniciais;
* Função principal (`main`) para controle do fluxo de execução;
* Exportação da base tratada ao final do processo.

Apesar da reutilização da estrutura, toda a lógica de tratamento, validação, análise e documentação foi adaptada para atender às necessidades específicas da Base Varejo e aos requisitos deste projeto avaliativo.

---

## Boas Práticas de Estruturação

O script foi organizado utilizando programação estruturada, buscando facilitar a leitura, manutenção e reutilização do código.

Foram adotadas as seguintes práticas:

* Separação das etapas em funções específicas;
* Comentários explicativos ao longo do código;
* Nomes de variáveis descritivos;
* Organização das atividades conforme as Sprints propostas;
* Centralização da execução na função `main()`.

Essa abordagem torna o projeto mais organizado e próximo das práticas utilizadas em ambientes profissionais.

---

## Análise Exploratória de Dados (EDA)

Embora não fosse uma exigência explícita do projeto, foi incluída uma etapa de **Análise Exploratória de Dados (EDA)** antes do processo de limpeza.

Nessa etapa foram avaliados:

* Quantidade de registros e colunas;
* Tipos de dados;
* Valores nulos;
* Registros duplicados;
* Categorias inválidas;
* Colunas desnecessárias.

A realização da EDA permitiu compreender melhor a qualidade da base antes de aplicar qualquer transformação, contribuindo para decisões mais conscientes durante a limpeza dos dados.

---

## Correção de Problemas de Importação

Durante os testes do projeto foi identificado um problema na leitura do arquivo CSV.

Inicialmente o arquivo estava sendo carregado utilizando a configuração padrão do pandas, fazendo com que toda a linha fosse interpretada como uma única coluna.

Após investigação, verificou-se que o arquivo utilizava o caractere ponto e vírgula (`;`) como separador de campos.

A solução adotada foi:

```python
pd.read_csv(caminho, sep=";")
```

Esse ajuste permitiu a correta identificação das 14 colunas da base e a execução adequada das etapas posteriores de análise e limpeza.

---

## Utilização do Terminal do VS Code

O desenvolvimento e os testes foram realizados utilizando o terminal integrado do VS Code.

Principais comandos utilizados:

### Instalação da biblioteca Pandas

```bash
pip install pandas
```

### Atualização do gerenciador de pacotes

```bash
python -m pip install --upgrade pip
```

### Execução do script

```bash
python script_NataliStoquera_VDBIT1.py
```

A utilização do terminal permitiu validar o funcionamento do projeto durante todo o processo de desenvolvimento.

---

## Versionamento com Git e GitHub

Foi utilizado Git para controle de versão do projeto e GitHub para armazenamento do repositório.

Principais comandos utilizados:

### Inicialização do repositório

```bash
git init
```

### Adição dos arquivos

```bash
git add .
```

### Criação dos commits

```bash
git commit -m "Miniprojeto Avaliativo - Natali Stoquera - VDBIT1 "
```

### Envio para o GitHub

```bash
git push origin main
```

O versionamento permitiu registrar a evolução do projeto e manter uma cópia pública para avaliação e consulta futura.

---

## Considerações Finais

Este projeto permitiu praticar atividades fundamentais da preparação de dados, incluindo importação, validação, limpeza, análise exploratória e documentação.

Além dos requisitos obrigatórios, também foram aplicadas boas práticas de organização de código, testes em ambiente local, versionamento e investigação de erros, aproximando a experiência de situações encontradas em projetos reais de análise de dados.

---

# 9. Como Executar

## VS Code

Instale a dependência necessária:

```bash
pip install pandas
```

Execute o script:

```bash
python script_NataliStoquera_VDBIT1.py
```

---

## Google Colab

1. Faça upload dos arquivos do projeto.
2. Execute o script normalmente.
3. O arquivo limpo será gerado automaticamente ao final da execução.

---

# 10. Tecnologias Utilizadas

* Python
* Pandas
* VS Code
* Git e GitHub

---

Projeto desenvolvido para fins educacionais na disciplina de Visualização de Dados e Business Intelligence do SENAI/SC – Lab 365.

