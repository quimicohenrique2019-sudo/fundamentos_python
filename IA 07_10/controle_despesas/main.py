import json
from datetime import date, datetime
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from analise import (
    adicionar_despesa,
    carregar_despesas,
    excluir_despesa,
    total_mes,
    quantidade_mes,
)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
LOGIN_FILE = BASE_DIR / "login.json"
DB_FILE = BASE_DIR / "bd.xlsx"

st.set_page_config(
    page_title="Controle de Despesas",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)


def carregar_login():
    try:
        with open(LOGIN_FILE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"user": "user", "senha": "batata"}


def inicializar_sessao():
    defaults = {
        "autenticado": False,
        "usuario": "",
        "tela": "historico",
    }
    for chave, valor in defaults.items():
        if chave not in st.session_state:
            st.session_state[chave] = valor


@st.dialog("Confirmação")
def confirmar_exclusao(indice):
    st.write("Deseja realmente excluir esta despesa?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Excluir", type="primary", use_container_width=True):
            excluir_despesa(indice, DB_FILE)
            st.success("Despesa excluída.")
            st.rerun()
    with col2:
        if st.button("Cancelar", use_container_width=True):
            st.rerun()


def tela_login():
    st.markdown(
        """
        <style>
        .login-box {
            max-width: 420px;
            margin: 90px auto 0 auto;
            padding: 30px;
            border-radius: 16px;
            background: rgba(255,255,255,0.04);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.title("💰 Controle de Despesas")
        st.caption("Entre para acessar seu controle financeiro.")

        with st.form("login_form"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            entrar = st.form_submit_button("Entrar", type="primary", use_container_width=True)

        if entrar:
            credenciais = carregar_login()
            if usuario == credenciais.get("user") and senha == credenciais.get("senha"):
                st.session_state.autenticado = True
                st.session_state.usuario = usuario
                st.session_state.tela = "historico"
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")

        st.markdown("</div>", unsafe_allow_html=True)


def sidebar():
    with st.sidebar:
        foto = BASE_DIR / "usuario.png"
        if foto.exists():
            st.image(str(foto), width=100)
        else:
            st.markdown("# 👤")

        st.markdown(f"### {st.session_state.usuario}")
        st.divider()

        if st.button("➕ Lançar despesas", use_container_width=True):
            st.session_state.tela = "lancar"
            st.rerun()

        if st.button("📋 Histórico", use_container_width=True):
            st.session_state.tela = "historico"
            st.rerun()

        st.divider()

        if st.button("🚪 Sair", use_container_width=True):
            st.session_state.autenticado = False
            st.session_state.usuario = ""
            st.session_state.tela = "historico"
            st.rerun()


def card(titulo, valor):
    st.markdown(
        f"""
        <div style="padding:18px;border-radius:12px;border:1px solid rgba(128,128,128,.25);">
            <div style="font-size:14px;opacity:.7;">{titulo}</div>
            <div style="font-size:28px;font-weight:700;margin-top:6px;">{valor}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def tela_historico():
    agora = datetime.now()
    df = carregar_despesas(DB_FILE)

    mes_atual = agora.month
    ano_atual = agora.year
    total = total_mes(df, ano_atual, mes_atual)
    quantidade = quantidade_mes(df, ano_atual, mes_atual)

    nomes_meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    st.title("Controle de Despesas")
    st.caption(f"Olá, {st.session_state.usuario}. Aqui está o resumo do mês.")

    col_mes, col_qtd, col_total = st.columns(3)
    with col_mes:
        card("Mês corrente", nomes_meses[mes_atual - 1])
    with col_qtd:
        card("Quantidade comprada", str(quantidade))
    with col_total:
        card("Total de despesas", f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    st.subheader("Despesas")

    if df.empty:
        st.info("Nenhuma despesa cadastrada.")
        return

    exibicao = df.copy()
    exibicao["Data"] = pd.to_datetime(exibicao["Data"]).dt.strftime("%d/%m/%Y")
    exibicao["Valor"] = exibicao["Valor"].map(
        lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    for indice, linha in exibicao.iterrows():
        col1, col2, col3, col4 = st.columns([4, 2, 2, 1])
        col1.write(linha["Descrição"])
        col2.write(linha["Valor"])
        col3.write(linha["Data"])
        if col4.button("🗑️", key=f"del_{indice}", help="Excluir despesa"):
            confirmar_exclusao(indice)


def tela_lancar():
    st.title("Lançar despesa")
    st.caption("Informe os dados da nova despesa.")

    with st.form("despesa_form", clear_on_submit=True):
        descricao = st.text_input("Descrição", placeholder="Ex.: Supermercado")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=0.01, format="%.2f")
        data = st.date_input("Data", value=date.today(), format="DD/MM/YYYY")
        salvar = st.form_submit_button("Salvar despesa", type="primary", use_container_width=True)

        if salvar:
            if not descricao.strip():
                st.error("Informe uma descrição.")
            else:
                adicionar_despesa(descricao.strip(), valor, data, DB_FILE)
                st.success("Despesa salva com sucesso!")
                st.session_state.tela = "historico"
                st.rerun()


inicializar_sessao()

if not st.session_state.autenticado:
    tela_login()
else:
    sidebar()
    if st.session_state.tela == "lancar":
        tela_lancar()
    else:
        tela_historico()