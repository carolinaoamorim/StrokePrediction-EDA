# Dataset

## Fonte

O dataset utilizado é o [**Stroke Prediction Dataset**](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset), publicado no Kaggle. Ele reúne informações clínicas e demográficas de pacientes para apoiar estudos de classificação binária relacionados à ocorrência de AVC.

!!! info "Variável-alvo"
    A coluna `stroke` indica se o paciente teve AVC (`1`) ou não (`0`). Como a classe positiva é rara, a análise precisa considerar o desbalanceamento antes de propor qualquer modelo.

## Características Gerais

| Métrica | Valor |
|---|---:|
| Registros | 5.110 |
| Atributos preditivos | 11 |
| Variável-alvo | `stroke` |
| Casos sem AVC | 4.861 |
| Casos com AVC | 249 |
| Taxa de AVC | 4,87% |
| Registros com `bmi` ausente | 201 |
| Registros com `smoking_status = Unknown` | 1.544 |

## Dicionário de Dados

| Coluna | Descrição |
|---|---|
| `id` | Identificador do paciente |
| `gender` | Gênero |
| `age` | Idade |
| `hypertension` | Indica hipertensão |
| `heart_disease` | Indica doença cardíaca |
| `ever_married` | Estado civil |
| `work_type` | Tipo de trabalho |
| `Residence_type` | Tipo de residência |
| `avg_glucose_level` | Nível médio de glicose |
| `bmi` | Índice de massa corporal |
| `smoking_status` | Status de tabagismo |
| `stroke` | Variável-alvo |

## Qualidade e Pontos de Atenção

| Ponto observado | Impacto na análise | Decisão recomendada |
|---|---|---|
| Classe positiva rara | Pode inflar métricas como acurácia | Usar métricas como recall, precision, F1-score e matriz de confusão |
| `bmi` com valores ausentes | Pode reduzir amostra se removido diretamente | Avaliar imputação ou análise separada dos casos ausentes |
| `smoking_status = Unknown` | Indica falta de informação sobre tabagismo | Tratar como categoria própria ou testar estratégias de imputação |
| `gender = Other` com apenas 1 registro | Categoria muito pouco representativa | Avaliar remoção ou agrupamento antes de modelagem |
| Variáveis clínicas e demográficas juntas | Exige cuidado na interpretação | Separar associação estatística de causalidade |

## Distribuição da Classe Alvo

| Classe | Quantidade | Proporção |
|---|---:|---:|
| `stroke = 0` | 4.861 | 95,13% |
| `stroke = 1` | 249 | 4,87% |

!!! warning "Desbalanceamento"
    O dataset contém muito mais pacientes sem AVC do que com AVC. Em uma etapa de modelagem, um classificador que sempre prevê `0` poderia ter alta acurácia aparente, mas seria inútil para identificar o evento de interesse.

## Leitura Inicial

O conjunto é adequado para uma EDA porque combina variáveis numéricas, categóricas, dados faltantes e uma classe-alvo desbalanceada. Esses elementos permitem discutir limpeza, visualização, comparação entre grupos e preparação responsável para modelos de classificação.
