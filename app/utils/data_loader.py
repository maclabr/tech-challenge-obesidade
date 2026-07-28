"""Carregamento e preparação dos dados analíticos da aplicação."""
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
CAMINHO_SILVER = ROOT / "data" / "silver" / "obesity_tratado.csv"


@st.cache_data(show_spinner=False)
def carregar_dados_dashboard() -> pd.DataFrame:
    if not CAMINHO_SILVER.exists():
        raise FileNotFoundError(
            f"Base Silver não encontrada em: {CAMINHO_SILVER}"
        )

    dados = pd.read_csv(CAMINHO_SILVER)

    colunas_obrigatorias = {
        "ds_genero",
        "nr_idade",
        "fl_historico_familiar_sobrepeso",
        "fl_consumo_calorico_frequente",
        "cd_consumo_de_vegetais",
        "cd_consumo_agua",
        "cd_frequencia_atividade_fisica",
        "ds_meio_transporte",
        "ds_nivel_obesidade",
        "nr_imc",
        "fl_transporte_ativo",
        "ds_faixa_etaria",
    }

    faltantes = colunas_obrigatorias - set(dados.columns)

    if faltantes:
        raise ValueError(
            f"A base Silver não contém as colunas esperadas: {sorted(faltantes)}"
        )

    return dados