from pathlib import Path

import joblib
import streamlit as st

# -----------------------------------------------------
# Configuração da página
# -----------------------------------------------------

st.set_page_config(
    page_title="Predição de Nível de Obesidade",
    page_icon="⚕️",
    layout="wide",
)

# -----------------------------------------------------
# Título
# -----------------------------------------------------

st.title("🏥 Predição do Nível de Obesidade")

st.markdown(
    """
Aplicação desenvolvida para o **Tech Challenge – FIAP Pós-Tech Data Analytics**.

O objetivo é estimar o nível de obesidade de um indivíduo a partir de
características individuais, histórico familiar e hábitos de vida,
utilizando um modelo de Machine Learning baseado em **Random Forest**.
"""
)

st.divider()

# -----------------------------------------------------
# Modelo
# -----------------------------------------------------

CAMINHO_MODELO = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "random_forest_comportamental.joblib"
)

try:

    modelo = joblib.load(CAMINHO_MODELO)

    st.success("✅ Modelo carregado com sucesso!")

    st.info(f"Pipeline carregada: {type(modelo).__name__}")

except Exception as erro:

    st.error("Erro ao carregar o modelo.")

    st.exception(erro)

st.divider()

st.markdown(
    """
Utilize o menu lateral para navegar entre as páginas da aplicação.
"""
)

from utils.model_loader import carregar_modelo

modelo = carregar_modelo()

st.subheader("Diagnóstico da Pipeline")

preprocessador = modelo.named_steps["preprocessador"]

st.write("Colunas esperadas pelo preprocessador:")

st.write(preprocessador.feature_names_in_)