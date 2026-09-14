# Análise Exploratória de Dados — Stroke Prediction

**Por:** Carolina Amorim e Lara Abduni

Análise exploratória de dados (EDA) sobre um conjunto de registros de pacientes, com o objetivo de entender quais características se associam à ocorrência de AVC (*stroke*) e preparar os dados para as fases de modelagem subsequentes.

A variável-alvo é `stroke`: `0` indica que a pessoa não teve AVC e `1` indica que teve. O dataset é fortemente desbalanceado (apenas 4,87% dos registros são casos positivos), o que orienta várias das decisões de análise e pré-processamento.

## Dataset

[Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) (Kaggle) — 5.110 registros e 11 features preditoras, incluindo idade, nível médio de glicose, IMC, hipertensão, doença cardíaca, tipo de trabalho e histórico de tabagismo. O download é feito automaticamente pelo notebook via `kagglehub`.

## Documentação

A documentação do projeto foi organizada com MkDocs Material e está preparada para publicação aberta via GitHub Pages:

[Documentação](https://carolinaoamorim.github.io/StrokePrediction-EDA/)

## Estrutura da análise

1. **Carregamento e inspeção inicial** — features, dimensões, tipos, valores ausentes, desbalanceamento do alvo e separação treino/teste.
2. **Análise univariada** — estatísticas descritivas e distribuições das variáveis numéricas e categóricas.
3. **Análise bivariada e multivariada** — correlações, relação das categóricas com o alvo e boxplots de numéricas por categóricas.
4. **Pré-processamento** — tratamento de ausentes e outliers, encoding, padronização, PCA e um pipeline reprodutível (`Pipeline` + `ColumnTransformer`).
5. **Achados, limitações e conclusão.**

## Principais achados

- Idade é a variável numérica mais associada ao AVC (correlação ≈ 0,25); casos positivos têm idade média bem mais alta.
- Hipertensão eleva de forma marcante a taxa de AVC (13,25% contra 3,97%).
- As classes não são linearmente separáveis: o PCA no espaço completo mostra forte sobreposição, indicando a necessidade de modelos não-lineares e de tratamento do desbalanceamento na modelagem.

## Tecnologias utilizadas

Python, com Pandas, NumPy, Matplotlib, Seaborn e Scikit-learn.

## Como executar

1. Instale as dependências: `pip install pandas numpy matplotlib seaborn scikit-learn kagglehub`
2. Abra `StrokePrediction.ipynb` e execute todas as células (Restart & Run All).