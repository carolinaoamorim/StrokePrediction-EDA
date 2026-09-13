# Análise Exploratória de Dados — Stroke Prediction

Projeto de análise exploratória de dados para estimar fatores associados à ocorrência de acidente vascular cerebral (`stroke`) a partir de um conjunto público de registros clínico-demográficos.

## Autoria

- Carolina Amorim
- Lara Abduni

## Visão Geral

A análise aborda o dataset do Kaggle `Stroke Prediction Dataset`, com foco em:

- perfil dos pacientes;
- distribuição da variável alvo;
- correlação entre atributos e ocorrência de AVC;
- tratamento de dados faltantes e outliers;
- preparação dos dados para modelagem.

## Objetivo

Compreender quais variáveis se associam à presença de AVC e construir uma base sólida para futuras etapas de modelagem preditiva.

## Dataset

Fonte: [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

- Registros: 5.110
- Variáveis preditivas: 11
- Variável alvo: `stroke`
- Classe positiva: aproximadamente 4,87%

## Estrutura do projeto

```text
StrokePrediction-EDA/
├── docs/
├── healthcare-dataset-stroke-data.csv
├── StrokePrediction.ipynb
├── mkdocs.yml
├── requirements.txt
└── requirements-docs.txt
```

## Análise em Destaque

A investigação do notebook inclui:

1. Carregamento e inspeção inicial dos dados.
2. Estatísticas descritivas e visualizações univariadas.
3. Correlações e relações entre variáveis categóricas e numéricas.
4. Tratamento de dados e preparação para modelagem.
5. Conclusões e limitações observadas no estudo.

## Principais Achados

- Idade apresenta associação mais forte com a ocorrência de AVC.
- Hipertensão apresenta maior taxa de eventos em relação ao grupo sem hipertensão.
- O conjunto é altamente desbalanceado, o que exige medidas especiais para avaliação e modelagem.

## Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- KaggleHub

## Requisitos de Execução

```bash
pip install -r requirements.txt
```

## Executar o Notebook

Abra o notebook `StrokePrediction.ipynb` e execute todas as células com o fluxo **Restart & Run All**.

## Documentação

A documentação está organizada em Markdown e pode ser servida localmente com MkDocs:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

A documentação deste projeto pode ser entregue como site público com GitHub Pages.
