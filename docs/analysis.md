# Análise Exploratória

## Objetivos da EDA

A análise exploratória foi conduzida para identificar padrões de distribuição, relações entre variáveis, ausência de informação e possíveis fatores associados à ocorrência de AVC. Nesta etapa, o objetivo não é provar causalidade, mas construir uma leitura estatística consistente do dataset.

## Checklist Executado

- [x] Verificação do número de linhas e colunas.
- [x] Avaliação de tipos de dados.
- [x] Detecção de valores ausentes.
- [x] Cálculo de estatísticas descritivas.
- [x] Exploração da variável-alvo `stroke`.
- [x] Comparação de grupos com e sem AVC.
- [x] Discussão de limitações para modelagem.

## Leitura Executiva

| Evidência | Interpretação |
|---|---|
| `stroke = 1` representa 4,87% da base | A classe positiva é rara e exige avaliação cuidadosa. |
| Pacientes 60+ têm taxa observada de AVC de 13,15% | Idade aparece como um dos sinais mais fortes na EDA. |
| Hipertensos têm taxa de AVC de 13,25% | A taxa é maior do que no grupo sem hipertensão. |
| Pacientes com doença cardíaca têm taxa de AVC de 17,03% | O histórico cardíaco se destaca como fator associado. |
| `bmi` possui 201 valores ausentes | A variável precisa de estratégia de tratamento antes de modelagem. |

## Distribuição por Faixa Etária

| Faixa etária | Pacientes | Casos de AVC | Taxa observada |
|---|---:|---:|---:|
| 0-17 | 856 | 2 | 0,23% |
| 18-39 | 1.314 | 6 | 0,46% |
| 40-59 | 1.564 | 60 | 3,84% |
| 60+ | 1.376 | 181 | 13,15% |

!!! success "Insight principal"
    A taxa de AVC cresce de forma expressiva nas faixas etárias mais altas. Isso sugere que `age` deve ser uma variável central em análises futuras e em qualquer modelo preditivo.

## Condições Clínicas

### Hipertensão

| Hipertensão | Pacientes | Casos de AVC | Taxa observada |
|---|---:|---:|---:|
| Não | 4.612 | 183 | 3,97% |
| Sim | 498 | 66 | 13,25% |

### Doença Cardíaca

| Doença cardíaca | Pacientes | Casos de AVC | Taxa observada |
|---|---:|---:|---:|
| Não | 4.834 | 202 | 4,18% |
| Sim | 276 | 47 | 17,03% |

!!! note "Interpretação"
    Hipertensão e doença cardíaca aparecem como variáveis associadas a maior taxa de AVC no conjunto analisado. Essa leitura é associativa: a EDA não permite concluir causalidade.

## Desafios Identificados

Os desafios e hipóteses observados incluem:

- Idade como fator com associação relevante ao AVC.
- Hipertensão como variável relevante.
- Distribuição de glicose e IMC em pacientes com e sem evento.
- Impacto de doenças cardíacas e status de tabagismo.
- Presença de valores ausentes em `bmi`.
- Grande proporção de `Unknown` em `smoking_status`.

## Implicações para Modelagem

Para etapas futuras, a análise sugere alguns cuidados:

1. Separar treino e teste antes de qualquer transformação aprendida a partir dos dados.
2. Tratar `bmi` ausente de forma controlada, evitando vazamento de informação.
3. Avaliar técnicas para desbalanceamento, como pesos de classe, reamostragem ou ajuste de threshold.
4. Priorizar métricas como recall, precision, F1-score, ROC-AUC e PR-AUC.
5. Validar se os padrões encontrados permanecem no conjunto de teste.

## Conclusão da EDA

A EDA indica que o dataset possui sinais coerentes para investigação preditiva, principalmente em idade e condições clínicas prévias. Ao mesmo tempo, o forte desbalanceamento da variável-alvo e a presença de dados faltantes tornam a preparação dos dados uma etapa crítica para que a modelagem seja avaliada de forma justa e tecnicamente defensável.
