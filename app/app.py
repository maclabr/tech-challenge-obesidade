import streamlit as st

from utils.model_loader import carregar_modelo

# -----------------------------------------------------
# Configuração da aplicação
# -----------------------------------------------------

st.set_page_config(
    page_title="Obesity Care Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------
# Página inicial
# -----------------------------------------------------

st.title("🏥 Obesity Care Analytics")

st.markdown(
    """
## Bem-vindo(a)!

Esta aplicação foi desenvolvida como parte do **Tech Challenge da FIAP – Pós-Tech Data Analytics**.

O objetivo é utilizar técnicas de Machine Learning para estimar o nível de obesidade de um indivíduo com base em características pessoais, hábitos de vida e informações comportamentais.

Utilize o menu lateral para navegar pelas funcionalidades da aplicação.
"""
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Dashboard")
    st.write("Visualize indicadores e análises exploratórias dos dados.")

with col2:
    st.subheader("🩺 Predição")
    st.write("Realize uma predição utilizando o modelo treinado.")

with col3:
    st.subheader("🧠 Modelo")
    st.write("Consulte informações e métricas do modelo de Machine Learning.")

st.divider()

try:
    carregar_modelo()
    st.success("✅ Modelo carregado com sucesso.")
except Exception as erro:
    st.error(f"Erro ao carregar o modelo: {erro}")

st.info(
    "Esta aplicação possui finalidade educacional e analítica. "
    "Os resultados não substituem avaliação ou diagnóstico médico."
)