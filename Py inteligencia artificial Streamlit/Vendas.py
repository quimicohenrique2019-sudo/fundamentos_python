# Autor: Henrique Xavier Prestes
# Projeto: Automação de vendas com IA

# -------- Bibliotecas --------
import streamlit as st # pip install streamlit
import pandas as pd # pip install pandas
import json
from google import genai # pip install google-genai

# -------- Configurações --------
With open ("token.json") as arquivo:
    token = json.load(arquivo)

client = genai.Client(api_key=token[api_key])

# -------- Interface --------
st.title("🤖 Agente de IA - Vendas")

# Abrir uma planilha específica
arquivo = st.file_uploader(
    "Escolha a planilha", 
    type=["xlsx"]
)

# Condicional para ler os dados da planilha
if arquivo:
    dados = pd.read_excel(arquivo)
    st.subheader("dados da planilha")
    st.dataframe(dados)
    pergunta = st.text_input("O que deseja saber?")