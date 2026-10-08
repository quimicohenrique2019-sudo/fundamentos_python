# Controle de Despesas

Aplicação de controle de despesas desenvolvida em Python + Streamlit, com persistência dos dados em Excel.

## Estrutura

```text
controle_despesas/
├── main.py
├── analise.py
├── bd.xlsx
├── login.json
├── requirements.txt
├── .env
├── .gitignore
└── usuario.png       # opcional
```

## Instalação

```bash
python -m venv .venv
```

### Windows

```bash
.venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run main.py
```

### Linux/macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```

## Login padrão

- Usuário: `user`
- Senha: `batata`

As credenciais ficam em `login.json`.

## Observação sobre segurança

O `login.json` é adequado para um projeto local/protótipo. Para um sistema publicado na internet, as senhas devem ser armazenadas com hash e o arquivo de dados deve ficar protegido.
