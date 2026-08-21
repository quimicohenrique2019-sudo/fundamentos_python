# Autor: Henrique Prestes
# Projeto:

import streamlit as st

# Título da página
st.title('Calculadora de IMC')

# Texto explicativo
st.write('Minha primeira página')

# Input de dados
nome = st.text_input('Digite seu nome:')

# Botão
if st.button ('Enviar'):
    if nome: 
        st.sucess(f'Olá, {nome}. Seja bem vindo!!!')
    else:
        st.warning('Gentileza, digitar um nome!')

# para rodar, digitar "python -m streamlit run imc_site.py"