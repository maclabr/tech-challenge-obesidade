import time

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.explainability import obter_importancia_global
from utils.predictor import prever
from utils.styles import (
    aplicar_estilos,
    card_imc,
    hero,
    placeholder_imc,
    rodape,
)
from utils.ui_options import (
    FREQUENCIA,
    HELP,
    SEXO,
    SIM_NAO,
    TITULOS,
    TRANSPORTE,
)


def classificar_imc(valor_imc: float) -> tuple[str, str]:
    """Retorna a classificação e a classe visual do IMC para adultos."""

    if valor_imc < 18.5:
        return "Baixo peso", "bmi-low"
    if valor_imc < 25.0:
        return "Peso adequado", "bmi-adequate"
    if valor_imc < 30.0:
        return "Sobrepeso", "bmi-overweight"
    if valor_imc < 35.0:
        return "Obesidade grau I", "bmi-obesity-one"
    if valor_imc < 40.0:
        return "Obesidade grau II", "bmi-obesity-two"
    return "Obesidade grau III", "bmi-obesity-three"


aplicar_estilos()

hero(
    "Predição de obesidade",
    "Informe os dados comportamentais do paciente para obter uma estimativa "
    "do nível de obesidade e uma leitura transparente da confiança do modelo.",
)

st.info(
    "O modelo não utiliza peso, altura ou IMC. A estimativa é baseada em "
    "idade, histórico familiar e hábitos de vida."
)

st.subheader("Avaliação corporal complementar")
st.caption(
    "Informe peso e altura para calcular o IMC. Esses dados não serão "
    "utilizados pelo modelo de Machine Learning."
)

col_peso, col_altura = st.columns(2)

peso = col_peso.number_input(
    "⚖️ Peso (kg)",
    min_value=0.0,
    max_value=350.0,
    value=0.0,
    step=0.1,
    format="%.1f",
    help="Informe o peso atual em quilogramas.",
)

altura = col_altura.number_input(
    "📏 Altura (m)",
    min_value=0.0,
    max_value=2.50,
    value=0.0,
    step=0.01,
    format="%.2f",
    help="Informe a altura em metros. Exemplo: 1,65.",
)

imc = None

if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)
    classificacao_imc, classe_visual_imc = classificar_imc(imc)
    card_imc(imc, classificacao_imc, classe_visual_imc)
else:
    placeholder_imc()

st.divider()

aceito = st.checkbox(
    "Confirmo que os dados foram revisados e compreendo que o resultado "
    "não substitui avaliação clínica."
)

with st.form("form_predicao", clear_on_submit=False):
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Dados pessoais",
            "Alimentação",
            "Estilo de vida",
            "Mobilidade",
        ]
    )

    with tab1:
        c1, c2, c3 = st.columns(3)

        sexo_label = c1.selectbox(
            TITULOS["sexo"],
            list(SEXO),
            help=HELP["sexo"],
        )

        idade = c2.number_input(
            TITULOS["idade"],
            min_value=14,
            max_value=61,
            value=25,
            step=1,
            help=HELP["idade"],
        )

        historico_label = c3.selectbox(
            TITULOS["historico"],
            list(SIM_NAO),
            help=HELP["historico"],
        )

    with tab2:
        c1, c2, c3 = st.columns(3)

        favc_label = c1.selectbox(
            TITULOS["favc"],
            list(SIM_NAO),
            help=HELP["favc"],
        )

        fcvc = c2.slider(
            TITULOS["fcvc"],
            min_value=1,
            max_value=3,
            value=2,
            step=1,
            help=HELP["fcvc"],
        )

        ncp = c3.slider(
            TITULOS["ncp"],
            min_value=1,
            max_value=4,
            value=3,
            step=1,
            help=HELP["ncp"],
        )

        c4, c5, c6 = st.columns(3)

        caec_label = c4.selectbox(
            TITULOS["caec"],
            list(FREQUENCIA),
            help=HELP["caec"],
        )

        ch2o = c5.slider(
            TITULOS["ch2o"],
            min_value=1,
            max_value=3,
            value=2,
            step=1,
            help=HELP["ch2o"],
        )

        scc_label = c6.selectbox(
            TITULOS["scc"],
            list(SIM_NAO),
            help=HELP["scc"],
        )

    with tab3:
        c1, c2, c3, c4 = st.columns(4)

        faf = c1.slider(
            TITULOS["faf"],
            min_value=0,
            max_value=3,
            value=1,
            step=1,
            help=HELP["faf"],
        )

        tue = c2.slider(
            TITULOS["tue"],
            min_value=0,
            max_value=2,
            value=1,
            step=1,
            help=HELP["tue"],
        )

        smoke_label = c3.selectbox(
            TITULOS["smoke"],
            list(SIM_NAO),
            help=HELP["smoke"],
        )

        calc_label = c4.selectbox(
            TITULOS["calc"],
            list(FREQUENCIA),
            help=HELP["calc"],
        )

    with tab4:
        mtrans_label = st.selectbox(
            TITULOS["mtrans"],
            list(TRANSPORTE),
            help=HELP["mtrans"],
        )

        st.caption(
            "Caminhada e bicicleta originam a feature de transporte ativo "
            "utilizada pelo pipeline."
        )

    enviar = st.form_submit_button(
        "🩺 Realizar predição",
        type="primary",
        use_container_width=True,
        disabled=not aceito,
    )


if enviar:
    dados_usuario = {
        "Gender": SEXO[sexo_label],
        "Age": idade,
        "family_history": SIM_NAO[historico_label],
        "FAVC": SIM_NAO[favc_label],
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": FREQUENCIA[caec_label],
        "SMOKE": SIM_NAO[smoke_label],
        "CH2O": ch2o,
        "SCC": SIM_NAO[scc_label],
        "FAF": faf,
        "TUE": tue,
        "CALC": FREQUENCIA[calc_label],
        "MTRANS": TRANSPORTE[mtrans_label],
    }

    try:
        with st.spinner("Processando os dados e consultando o modelo..."):
            time.sleep(0.35)
            resultado = prever(dados_usuario)

        classe = resultado["classe"]
        confianca = resultado["confianca"]

        st.success("Predição concluída com sucesso.")

        if imc is not None:
            st.caption(
                f"IMC complementar informado nesta avaliação: {imc:.2f} kg/m². "
                "Esse valor não foi utilizado pelo modelo."
            )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Classificação estimada",
            classe,
        )

        c2.metric(
            "Confiança da classe",
            f"{confianca:.1%}",
        )

        c3.metric(
            "Faixa de confiança",
            (
                "Alta"
                if confianca >= 0.75
                else "Moderada"
                if confianca >= 0.50
                else "Baixa"
            ),
        )

        if "Obesidade" in classe:
            estilo = "risk-high"
            interpretacao = (
                "O padrão informado foi associado pelo modelo a uma classe "
                "de obesidade. Recomenda-se avaliação profissional completa "
                "e uso do resultado apenas como sinal de apoio à priorização."
            )

        elif "Sobrepeso" in classe:
            estilo = "risk-medium"
            interpretacao = (
                "O padrão informado foi associado a sobrepeso. O resultado "
                "pode apoiar ações preventivas, mas deve ser confirmado por "
                "avaliação clínica."
            )

        elif "Peso insuficiente" in classe:
            estilo = "risk-medium"
            interpretacao = (
                "O padrão informado foi associado a baixo peso. Peso "
                "insuficiente também é clinicamente relevante e pode "
                "indicar necessidade de acompanhamento nutricional."
            )

        else:
            estilo = "risk-low"
            interpretacao = (
                "O padrão informado não foi associado a sobrepeso ou "
                "obesidade nesta estimativa. Ainda assim, o resultado não "
                "exclui a necessidade de acompanhamento individual."
            )

        st.markdown(
            (
                f'<div class="{estilo}">'
                "<b>Interpretação para apoio ao cuidado</b><br>"
                f"{interpretacao}"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

        probabilidades = resultado["probabilidades"]

        probs = pd.DataFrame(
            {
                "classe": list(probabilidades.keys()),
                "probabilidade": list(probabilidades.values()),
            }
        ).sort_values("probabilidade")

        probs["rotulo_probabilidade"] = probs["probabilidade"].map(
            lambda valor: f"{valor:.1%}"
        )

        fig = px.bar(
            probs,
            x="probabilidade",
            y="classe",
            orientation="h",
            text="rotulo_probabilidade",
            title="Distribuição das probabilidades entre as classes",
        )

        fig.update_layout(
            xaxis_tickformat=".0%",
            xaxis_title="Probabilidade",
            yaxis_title="",
            height=430,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="grafico_probabilidades_predicao",
        )

        with st.expander("Como interpretar a confiança"):
            st.write(
                "A confiança corresponde à maior probabilidade produzida "
                "pelo modelo. Ela não representa certeza clínica e pode ser "
                "menor quando diferentes classes apresentam padrões "
                "comportamentais semelhantes."
            )

        with st.expander(
            "Fatores gerais mais relevantes para o modelo"
        ):
            importancia = (
                obter_importancia_global()
                .head(10)
                .sort_values("importancia")
            )

            fig_imp = px.bar(
                importancia,
                x="importancia",
                y="variavel",
                orientation="h",
                title="Importância global agregada das variáveis",
            )

            fig_imp.update_layout(
                xaxis_title="Importância no Random Forest",
                yaxis_title="",
                height=420,
            )

            st.plotly_chart(
                fig_imp,
                use_container_width=True,
                key="grafico_importancia_global_predicao",
            )

            st.caption(
                "Esta é uma explicação global do modelo, não uma "
                "justificativa causal e individual da predição. SHAP não "
                "foi incluído para evitar adicionar uma dependência não "
                "utilizada no treinamento original."
            )

    except Exception as erro:
        st.error(
            "Não foi possível realizar a predição. Verifique os dados e a "
            "disponibilidade do modelo."
        )

        with st.expander("Detalhes técnicos do erro"):
            st.code(str(erro))


rodape()