import streamlit as st

from utils.model_loader import carregar_modelo

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

modelo = carregar_modelo()

st.divider()

st.markdown(
    """
Utilize o menu lateral para navegar entre as páginas da aplicação.
"""
)