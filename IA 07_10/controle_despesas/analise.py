from datetime import date
from pathlib import Path

import pandas as pd
from openpyxl import Workbook

COLUNAS = ["Descrição", "Valor", "Data"]


def garantir_bd(caminho_bd: Path):
    caminho_bd = Path(caminho_bd)
    if not caminho_bd.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "Despesas"
        ws.append(COLUNAS)
        wb.save(caminho_bd)


def carregar_despesas(caminho_bd: Path) -> pd.DataFrame:
    garantir_bd(caminho_bd)
    try:
        df = pd.read_excel(caminho_bd, sheet_name="Despesas")
    except Exception:
        return pd.DataFrame(columns=COLUNAS)

    for coluna in COLUNAS:
        if coluna not in df.columns:
            df[coluna] = None

    df = df[COLUNAS].copy()
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0)
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    return df


def salvar_despesas(df: pd.DataFrame, caminho_bd: Path):
    garantir_bd(caminho_bd)
    df = df[COLUNAS].copy()
    df.to_excel(caminho_bd, sheet_name="Despesas", index=False)


def adicionar_despesa(descricao: str, valor: float, data: date, caminho_bd: Path):
    df = carregar_despesas(caminho_bd)
    nova = pd.DataFrame([{
        "Descrição": descricao,
        "Valor": float(valor),
        "Data": pd.Timestamp(data),
    }])
    df = pd.concat([df, nova], ignore_index=True)
    salvar_despesas(df, caminho_bd)


def excluir_despesa(indice: int, caminho_bd: Path):
    df = carregar_despesas(caminho_bd)
    if indice in df.index:
        df = df.drop(index=indice).reset_index(drop=True)
        salvar_despesas(df, caminho_bd)


def total_mes(df: pd.DataFrame, ano: int, mes: int) -> float:
    if df.empty:
        return 0.0
    filtro = (df["Data"].dt.year == ano) & (df["Data"].dt.month == mes)
    return float(df.loc[filtro, "Valor"].sum())


def quantidade_mes(df: pd.DataFrame, ano: int, mes: int) -> int:
    if df.empty:
        return 0
    filtro = (df["Data"].dt.year == ano) & (df["Data"].dt.month == mes)
    return int(filtro.sum())
