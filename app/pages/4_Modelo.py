import plotly.express as px
import streamlit as st
from utils.explainability import obter_importancia_global
from utils.model_loader import carregar_modelo
from utils.styles import aplicar_estilos, hero, rodape

METRICAS_MODELO = {
    "accuracy_cv": 0.7963,
    "accuracy_teste": 0.7943,
    "f1_macro_cv": 0.7891,
    "meta": 0.75,
}

aplicar_estilos()
hero("Modelo de Machine Learning", "Metodologia, desempenho e interpretabilidade do Random Forest selecionado para o cenário comportamental.")

c1,c2,c3,c4=st.columns(4)
c1.metric("Accuracy CV", f"{METRICAS_MODELO['accuracy_cv']:.1%}")
c2.metric("Accuracy teste", f"{METRICAS_MODELO['accuracy_teste']:.1%}")
c3.metric("F1-macro CV", f"{METRICAS_MODELO['f1_macro_cv']:.1%}")
c4.metric("Meta do projeto", f"{METRICAS_MODELO['meta']:.1%}", "Atingida")

st.markdown("## Por que Random Forest?")
st.write("Embora o XGBoost tenha alcançado a maior média de validação cruzada no cenário comportamental, o Random Forest foi recomendado para produção por apresentar desempenho muito próximo, menor diferença entre validação e teste, treinamento mais rápido e menor sinal de overfitting.")

try:
    pipeline=carregar_modelo(); modelo=pipeline.named_steps["modelo"]
    c1,c2,c3=st.columns(3)
    c1.metric("Algoritmo", "Random Forest")
    c2.metric("Árvores", f"{modelo.n_estimators}")
    c3.metric("Features de entrada", f"{len(pipeline.feature_names_in_)}")
except Exception as erro:
    st.warning(f"Não foi possível inspecionar a pipeline: {erro}")

st.markdown("## Importância global")
imp=obter_importancia_global().head(12).sort_values("importancia")
fig=px.bar(imp,x="importancia",y="variavel",orientation="h",title="Variáveis com maior contribuição global para as divisões das árvores")
fig.update_layout(xaxis_title="Importância agregada",yaxis_title="",height=500)
st.plotly_chart(fig,use_container_width=True)
st.caption("Importância global indica frequência e ganho das variáveis nas árvores. Não prova causalidade e não substitui interpretação clínica.")

with st.expander("Pipeline de pré-processamento"):
    st.write("Variáveis numéricas são padronizadas com StandardScaler; escalas ordinais são preservadas; variáveis categóricas são codificadas com OneHotEncoder. A pipeline salva contém preprocessing e modelo no mesmo arquivo joblib.")
with st.expander("Limitação metodológica"):
    st.write("O alvo do dataset original está relacionado a faixas de IMC. Para evitar circularidade, o modelo em produção exclui altura, peso e IMC, utilizando apenas variáveis demográficas e comportamentais.")
rodape()
