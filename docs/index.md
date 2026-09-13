# Análise Exploratória de Dados — Stroke Prediction

Bem-vindo à documentação do projeto de predição de AVC com foco em análise exploratória de dados.

## Visão Geral

Este projeto investiga um conjunto de registros de pacientes com o objetivo de identificar padrões associados à ocorrência de acidente vascular cerebral (*stroke*). A análise combina inspeção inicial, tratamento de valores ausentes, distribuição das variáveis, correlações, visualizações e preparação de dados para modelagem.

## Objetivo

Compreender quais variáveis se relacionam com o diagnóstico de AVC e gerar uma base analítica organizada para etapas futuras de modelagem preditiva.

## Dataset

O dataset utilizado é o [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset), com 5.110 registros e 11 variáveis preditivas. A variável alvo é `stroke`, com classes `0` e `1`.

## Pipeline de Análise

1. Carregamento e inspeção do dataset.
2. Estatísticas descritivas e exploração de distribuições.
3. Tratamento de valores ausentes e encoding categórico.
4. Visualização de correlações e comportamento por faixa de risco.
5. Preparação da análise para modelagem.

## Principais Descobertas

- A idade apresenta associação mais clara com o desfecho.
- Hipertensão e histórico de doenças cardíacas aparecem como fatores relevantes.
- O conjunto é fortemente desbalanceado, o que impacta decisões futuras de modelagem.

## Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- KaggleHub
