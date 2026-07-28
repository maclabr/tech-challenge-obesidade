import streamlit as st

from utils.model_loader import carregar_modelo
from utils.styles import aplicar_estilos, hero, rodape


st.set_page_config(
    page_title="Obesity Care Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

aplicar_estilos()


with st.sidebar:
    st.markdown("### 🏥 Obesity Care")
    st.caption("Analytics & Machine Learning")
    st.divider()

    st.info(
        "Navegue pelas páginas para explorar os dados, realizar uma "
        "predição e consultar o desempenho do modelo."
    )


hero(
    "Obesity Care Analytics",
    "Plataforma analítica para apoiar ações preventivas e a priorização "
    "do cuidado relacionado à obesidade.",
)


col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("📊 Dashboard")
        st.write(
            "Explore a distribuição dos níveis de obesidade e os padrões "
            "de hábitos identificados na EDA."
        )

with col2:
    with st.container(border=True):
        st.subheader("🩺 Predição")
        st.write(
            "Estime o nível de obesidade a partir de dados pessoais e "
            "comportamentais."
        )

with col3:
    with st.container(border=True):
        st.subheader("🧠 Modelo")
        st.write(
            "Consulte métricas, metodologia e fatores mais relevantes "
            "para o Random Forest."
        )


try:
    carregar_modelo()

    st.success(
        "Pipeline de Machine Learning carregada e disponível para predição."
    )

except Exception as erro:
    st.error(
        f"Não foi possível carregar o modelo: {erro}"
    )


st.markdown("### Uso responsável")

st.markdown(
    """
    <div class="clinical-note">
        A classificação é uma estimativa estatística para apoio educacional
        e analítico. Ela não constitui diagnóstico, não prescreve condutas
        e deve ser interpretada em conjunto com avaliação clínica.
    </div>
    """,
    unsafe_allow_html=True,
)


rodape()