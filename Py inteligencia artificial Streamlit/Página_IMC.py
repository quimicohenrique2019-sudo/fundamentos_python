# Autor: Henrique Xavier Prestes
# Projeto: página Web

# Instalar a biblioteca (pip install streamlit)

# Importar as bibliotecas do streamlit
import streamlit as st

# Confguração da página
st.set_page_config(
    page_title="Página IMC",
    page_icon="🤖"
)

# Título da página
st.title("Cálculo do IMC")
st.number_input(label="Digite seu peso (kg)")
st.number_input(label="Digite sua altura(cm)")

st.button(label)
