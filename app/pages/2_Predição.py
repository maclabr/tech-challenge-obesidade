import streamlit as st

from utils.ui_options import (
    SEXO,
    SIM_NAO,
    FREQUENCIA,
    TRANSPORTE,
    TITULOS,
    HELP,
    SECOES,
)

from utils.predictor import prever

st.title("🔍 Predição de Obesidade")

st.markdown(
    """
    Preencha as características do indivíduo para estimar o nível de obesidade
    utilizando o modelo Random Forest treinado no projeto.
    """
)

st.divider()

# Características Individuais

st.header(SECOES["individuais"])

col1, col2 = st.columns(2)

with col1:

    sexo_label = st.selectbox(
        TITULOS["sexo"],
        options=list(SEXO.keys()),
        help=HELP["sexo"],
    )

    genero = SEXO[sexo_label]

with col2:

    idade = st.number_input(
        TITULOS["idade"],
        min_value=1,
        max_value=100,
        value=25,
        help=HELP["idade"],
    )

st.divider()

# Histórico Familiar

st.header(SECOES["historico"])

historico_label = st.selectbox(
    TITULOS["historico"],
    options=list(SIM_NAO.keys()),
    help=HELP["historico"],
)

historico = SIM_NAO[historico_label]

st.divider()

# Hábitos Alimentares

st.header(SECOES["alimentacao"])

col1, col2 = st.columns(2)

with col1:

    favc_label = st.selectbox(
        TITULOS["favc"],
        options=list(SIM_NAO.keys()),
        help=HELP["favc"],
    )

    favc = SIM_NAO[favc_label]

    fcvc = st.slider(
        TITULOS["fcvc"],
        min_value=1.0,
        max_value=3.0,
        value=2.0,
        step=0.5,
        help=HELP["fcvc"],
    )

    ncp = st.slider(
        TITULOS["ncp"],
        min_value=1.0,
        max_value=4.0,
        value=3.0,
        step=0.5,
        help=HELP["ncp"],
    )

with col2:

    caec_label = st.selectbox(
        TITULOS["caec"],
        options=list(FREQUENCIA.keys()),
        help=HELP["caec"],
    )

    caec = FREQUENCIA[caec_label]

    ch2o = st.slider(
        TITULOS["ch2o"],
        min_value=1.0,
        max_value=3.0,
        value=2.0,
        step=0.5,
        help=HELP["ch2o"],
    )

    scc_label = st.selectbox(
        TITULOS["scc"],
        options=list(SIM_NAO.keys()),
        help=HELP["scc"],
    )

    scc = SIM_NAO[scc_label]

st.divider()

# Estilo de Vida

st.header(SECOES["estilo_vida"])

col1, col2 = st.columns(2)

with col1:

    faf = st.slider(
        TITULOS["faf"],
        min_value=0.0,
        max_value=3.0,
        value=1.0,
        step=0.5,
        help=HELP["faf"],
    )

    tue = st.slider(
        TITULOS["tue"],
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.5,
        help=HELP["tue"],
    )

with col2:

    smoke_label = st.selectbox(
        TITULOS["smoke"],
        options=list(SIM_NAO.keys()),
        help=HELP["smoke"],
    )

    smoke = SIM_NAO[smoke_label]

    calc_label = st.selectbox(
        TITULOS["calc"],
        options=list(FREQUENCIA.keys()),
        help=HELP["calc"],
    )

    calc = FREQUENCIA[calc_label]

st.divider()

# Mobilidade

st.header(SECOES["mobilidade"])

mtrans_label = st.selectbox(
    TITULOS["mtrans"],
    options=list(TRANSPORTE.keys()),
    help=HELP["mtrans"],
)

mtrans = TRANSPORTE[mtrans_label]

st.divider()

dados_usuario = {
    "Gender": genero,
    "Age": idade,
    "family_history": historico,
    "FAVC": favc,
    "FCVC": fcvc,
    "NCP": ncp,
    "CAEC": caec,
    "SMOKE": smoke,
    "CH2O": ch2o,
    "SCC": scc,
    "FAF": faf,
    "TUE": tue,
    "CALC": calc,
    "MTRANS": mtrans,
}

if st.button(
    "Realizar Predição",
    type="primary",
    use_container_width=True,
):
    try:

        resultado = prever(dados_usuario)

        classe_prevista = resultado["classe"]
        probabilidades = resultado["probabilidades"]

        confianca = probabilidades[classe_prevista]

        st.success("🩺 Predição realizada com sucesso!")

        with st.container(border=True):

         st.subheader("Resultado da Predição")

        st.metric(
        label="Classificação prevista",
        value=classe_prevista,
    )

        st.write("#### Confiança da predição")

        st.progress(confianca)

        st.caption(f"{confianca:.1%} de confiança")

    except Exception as e:

        st.error(
            f"Erro ao realizar a predição:\n\n{e}"
        )