# Análise Exploratória de Dados — Stroke Prediction

Projeto de análise exploratória de dados para identificar fatores associados à ocorrência de acidente vascular cerebral (`stroke`) a partir de um conjunto público de registros clínico-demográficos.

## Documentação

A documentação do projeto foi organizada com MkDocs Material e está preparada para publicação aberta via GitHub Pages:

[Acessar documentação](https://carolinaoamorim.github.io/StrokePrediction-EDA/)

## Autoria

- Carolina Amorim
- Lara Abduni

## Visão Geral

A análise aborda o dataset do Kaggle **Stroke Prediction Dataset**, com foco em:

- perfil dos pacientes;
- distribuição da variável-alvo;
- qualidade dos dados e valores ausentes;
- relações entre atributos clínicos, demográficos e ocorrência de AVC;
- preparação da base para futuras etapas de modelagem.

## Dataset

Fonte: [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

- Registros: 5.110
- Variáveis preditivas: 11
- Variável-alvo: `stroke`
- Classe positiva: 249 casos, aproximadamente 4,87% da base

## Principais Achados

- Idade apresenta associação relevante com a ocorrência de AVC.
- Hipertensão e doença cardíaca aparecem associadas a taxas observadas mais altas de AVC.
- O conjunto é altamente desbalanceado, o que exige cuidado na avaliação de modelos.
- A variável `bmi` possui valores ausentes e deve ser tratada antes da modelagem.

## Estrutura do Projeto

```text
StrokePrediction-EDA/
├── docs/
├── healthcare-dataset-stroke-data.csv
├── StrokePrediction.ipynb
├── mkdocs.yml
├── requirements.txt
└── requirements-docs.txt
```

## Executar a Análise

Instale as dependências:

```bash
pip install -r requirements.txt
```

Abra o notebook `StrokePrediction.ipynb` e execute todas as células com **Restart & Run All**.

## Rodar a Documentação Localmente

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Os gráficos da documentação podem ser recriados com:

```bash
python scripts/generate_docs_figures.py
```

## Validar e Publicar

Valide o build:

```bash
mkdocs build --strict
```

Publique no GitHub Pages:

```bash
mkdocs gh-deploy
```
