# Setup e Execução

## Requisitos

- Python 3.10 ou superior
- Ambiente virtual recomendado
- Conexão com internet para instalar dependências e, se necessário, baixar dados pelo Kaggle

## Instalação

=== "Windows PowerShell"

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    pip install -r requirements-docs.txt
    ```

=== "macOS/Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-docs.txt
    ```

## Dependências de Análise

```bash
pip install -r requirements.txt
```

Principais bibliotecas usadas:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `kagglehub`

## Executando o Notebook

1. Abra o notebook `StrokePrediction.ipynb`.
2. Execute todas as células com **Restart & Run All**.
3. Confira se o arquivo `healthcare-dataset-stroke-data.csv` está no diretório raiz do projeto.

## Rodando a Documentação Localmente

Instale as dependências de documentação:

```powershell
pip install -r requirements-docs.txt
```

Sirva o site em modo de desenvolvimento:

```bash
mkdocs serve
```

Abra o endereço exibido no terminal, normalmente `http://127.0.0.1:8000/`.

## Build de Verificação

```bash
mkdocs build --strict
```

O modo `--strict` ajuda a encontrar links quebrados, páginas ausentes e problemas que poderiam prejudicar a publicação.

## Publicação no GitHub Pages

```bash
mkdocs gh-deploy
```

!!! tip "Entrega com conceito +"
    Para uma entrega aberta, publique o site no GitHub Pages e coloque o link no README do repositório. Assim a documentação fica acessível sem precisar abrir o notebook localmente.
