import streamlit as st
from utils.styles import aplicar_estilos, hero, rodape

aplicar_estilos()
hero("Sobre o projeto", "Contexto de negócio, recorte metodológico e fluxo de desenvolvimento do Tech Challenge.")

st.markdown("## Objetivo")
st.write("Desenvolver uma solução de Machine Learning capaz de estimar o nível de obesidade de pacientes a partir de características individuais, histórico familiar e hábitos de vida, apoiando ações preventivas e a priorização do cuidado.")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Cenário de produção")
        st.write("A aplicação utiliza o cenário comportamental, que exclui altura, peso e IMC. Essa decisão evita que o modelo apenas reproduza a fórmula usada originalmente para definir o alvo.")
with col2:
    with st.container(border=True):
        st.subheader("Fonte de dados")
        st.write("Dataset público Estimation of Obesity Levels, com informações demográficas, alimentares, de atividade física e estilo de vida.")

st.markdown("## Etapas realizadas")
st.write("Validação do schema → limpeza de duplicatas → arredondamento das escalas ordinais → engenharia de features comportamentais → comparação de modelos → seleção do Random Forest → deploy em Streamlit.")

st.warning("A aplicação tem finalidade acadêmica e demonstrativa. O resultado não substitui diagnóstico, avaliação antropométrica ou decisão de um profissional de saúde.")
rodape()
