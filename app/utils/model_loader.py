"""Carregamento centralizado da pipeline de Machine Learning."""
from pathlib import Path
import joblib
import streamlit as st

CAMINHO_MODELO = Path(__file__).resolve().parents[2] / "models" / "random_forest_comportamental.joblib"

@st.cache_resource(show_spinner=False)
def carregar_modelo():
    if not CAMINHO_MODELO.exists():
        raise FileNotFoundError(f"Modelo não encontrado em: {CAMINHO_MODELO}")
    return joblib.load(CAMINHO_MODELO)