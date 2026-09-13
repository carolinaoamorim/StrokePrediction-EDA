# Setup e Execução

## Requisitos

- Python 3.10+
- Ambiente virtual recomendado
- Conexão com internet para baixar o arquivo do Kaggle

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-docs.txt
```

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-docs.txt
```

## Dependências de Análise

```bash
pip install pandas numpy matplotlib seaborn scikit-learn kagglehub
```

## Executando o Notebook

1. Abra o notebook `StrokePrediction.ipynb`.
2. Execute todas as células com a opção **Restart & Run All**.
3. Caso o dataset ainda não exista, o notebook pode usar `kagglehub` para carregá-lo automaticamente.

## Gerando a Documentação

```bash
pip install mkdocs
mkdocs serve
```

A documentação pode ser publicada com GitHub Pages usando a configuração padrão do MkDocs.
