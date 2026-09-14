<section class="hero" markdown>
<p class="eyebrow">APS Machine Learning • Documentação aberta</p>

# Stroke Prediction EDA

Análise exploratória de dados sobre fatores clínicos e demográficos associados à ocorrência de AVC, com documentação preparada para publicação em GitHub Pages.

<div class="hero-actions" markdown>
[Ver análise](analysis.md){ .md-button .md-button--primary }
[Conhecer o dataset](dataset.md){ .md-button }
[Executar localmente](setup.md){ .md-button }
</div>
</section>

## Visão Geral

Este projeto investiga o **Stroke Prediction Dataset**, um conjunto público com registros de pacientes e variáveis como idade, hipertensão, doença cardíaca, glicose média, IMC e tabagismo. O foco desta etapa é entender a estrutura dos dados, identificar limitações e extrair sinais relevantes antes de qualquer modelagem preditiva.

<div class="metric-grid" markdown>
<div class="metric-card" markdown>
<span class="metric-label">Registros</span>
<strong>5.110</strong>
Pacientes no arquivo original.
</div>

<div class="metric-card" markdown>
<span class="metric-label">Classe positiva</span>
<strong>4,87%</strong>
249 casos de AVC registrados.
</div>

<div class="metric-card" markdown>
<span class="metric-label">Variáveis</span>
<strong>11</strong>
Atributos preditivos mais a variável-alvo.
</div>

<div class="metric-card" markdown>
<span class="metric-label">IMC ausente</span>
<strong>3,93%</strong>
201 registros com `bmi` sem informação.
</div>
</div>

## Resumo Executivo

| Pergunta | Resposta da EDA |
|---|---|
| Qual é o problema? | Classificação binária da ocorrência de AVC (`stroke`). |
| Qual é o maior desafio? | A base é altamente desbalanceada: a classe positiva representa apenas 4,87% dos registros. |
| Quais variáveis chamam atenção? | Idade, hipertensão, doença cardíaca, glicose média e IMC. |
| O que precisa de cuidado? | Valores ausentes em `bmi`, categoria `Unknown` em tabagismo e avaliação com métricas adequadas para dados desbalanceados. |

## Pipeline da EDA

```mermaid
flowchart LR
    A[Carregamento do CSV] --> B[Inspeção inicial]
    B --> C[Qualidade dos dados]
    C --> D[Análise univariada]
    D --> E[Análise bivariada]
    E --> F[Insights e limitações]
    F --> G[Preparação para modelagem]
```

## Principais Achados

<div class="highlight-grid" markdown>
<div class="highlight-card" markdown>
<span class="status-pill">Achado 1</span>

### Idade concentra risco

Pacientes com 60 anos ou mais concentram a maior taxa observada de AVC no dataset, com 13,15% de casos positivos nesse grupo.
</div>

<div class="highlight-card" markdown>
<span class="status-pill">Achado 2</span>

### Comorbidades importam

Hipertensão e doença cardíaca aparecem associadas a taxas de AVC bem superiores às dos grupos sem essas condições.
</div>

<div class="highlight-card" markdown>
<span class="status-pill">Achado 3</span>

### Métrica exige cuidado

Como a classe positiva é rara, acurácia isolada pode mascarar modelos ruins para detectar pacientes com AVC.
</div>
</div>

## Critérios de Entrega

<div class="checklist" markdown>
<div markdown>
**Documentação aberta**<br>
Site MkDocs pronto para publicação em GitHub Pages.
</div>

<div markdown>
**Reprodutibilidade**<br>
Instruções de ambiente, dependências e execução do notebook.
</div>

<div markdown>
**Clareza analítica**<br>
Dataset, hipóteses, limitações e achados documentados em páginas separadas.
</div>

<div markdown>
**Acabamento profissional**<br>
Tema Material, busca, navegação organizada, cards, tabelas e diagrama de pipeline.
</div>
</div>

## Autoria

**Carolina Amorim** e **Lara Abduni**<br>
Projeto de Machine Learning com foco em análise exploratória de dados.
