import html
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


def faixa_confianca(confianca: float) -> str:
    """Retorna a leitura visual da confiança calculada pelo modelo."""

    if confianca >= 0.75:
        return "Alta"
    if confianca >= 0.50:
        return "Moderada"
    return "Baixa"


def renderizar_resultado_lateral(
    classe: str,
    confianca: float,
    imc: float | None,
) -> None:
    """Apresenta o resumo principal da predição no painel lateral."""

    classe_normalizada = str(classe).lower()

    if "obesidade tipo iii" in classe_normalizada or "obesidade grau iii" in classe_normalizada:
        classe_visual = "prediction-result-obesity-three"
    elif "obesidade tipo ii" in classe_normalizada or "obesidade grau ii" in classe_normalizada:
        classe_visual = "prediction-result-obesity-two"
    elif "obesidade" in classe_normalizada:
        classe_visual = "prediction-result-obesity-one"
    elif "sobrepeso" in classe_normalizada:
        classe_visual = "prediction-result-overweight"
    elif "peso insuficiente" in classe_normalizada or "baixo peso" in classe_normalizada:
        classe_visual = "prediction-result-underweight"
    else:
        classe_visual = "prediction-result-healthy"

    classe_segura = html.escape(str(classe))
    imc_resumo = f"{imc:.2f} kg/m²" if imc is not None else "Não informado"
    confianca_percentual = max(0.0, min(confianca * 100, 100.0))

    st.markdown(
        (
            f'<div class="prediction-result-card {classe_visual}">'
            '<div class="prediction-result-topbar"></div>'
            '<div class="prediction-result-header">'
            '<div>'
            '<div class="prediction-result-label">Resultado da predição</div>'
            f'<div class="prediction-result-badge">{classe_segura}</div>'
            '</div>'
            '<span class="prediction-result-check" aria-hidden="true">✓</span>'
            '</div>'
            '<div class="prediction-confidence-block">'
            '<div class="prediction-confidence-heading">'
            '<span>Confiança do modelo</span>'
            f'<strong>{confianca:.1%}</strong>'
            '</div>'
            '<div class="prediction-confidence-track">'
            f'<span style="width:{confianca_percentual:.1f}%"></span>'
            '</div>'
            f'<small>Faixa de confiança: {faixa_confianca(confianca)}</small>'
            '</div>'
            '<div class="prediction-result-grid">'
            '<div class="prediction-result-item">'
            '<span>Modelo utilizado</span><strong>Random Forest</strong>'
            '</div>'
            '<div class="prediction-result-item">'
            '<span>IMC complementar</span>'
            f'<strong>{html.escape(imc_resumo)}</strong>'
            '</div>'
            '</div></div>'
        ),
        unsafe_allow_html=True,
    )


aplicar_estilos()

hero(
    "Predição de obesidade",
    "Informe os dados comportamentais do paciente para obter uma estimativa "
    "do nível de obesidade e uma leitura transparente da confiança do modelo.",
)

st.markdown(
    """
    <div class="prediction-info-card">
        <span class="prediction-info-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="9"></circle>
                <path d="M12 10v6"></path>
                <path d="M12 7h.01"></path>
            </svg>
        </span>
        <div class="prediction-info-content">
            <strong>Uso complementar e responsável</strong>
            <p>O modelo utiliza idade, histórico familiar e hábitos de vida.
            Peso, altura e IMC são apresentados como apoio complementar e não
            influenciam a predição.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

valores_padrao = {
    "pred_sexo_label": list(SEXO)[0],
    "pred_idade": 25,
    "pred_historico_label": list(SIM_NAO)[0],
    "pred_favc_label": list(SIM_NAO)[0],
    "pred_fcvc": 2,
    "pred_ncp": 3,
    "pred_caec_label": list(FREQUENCIA)[0],
    "pred_ch2o": 2,
    "pred_scc_label": list(SIM_NAO)[0],
    "pred_faf": 1,
    "pred_tue": 1,
    "pred_smoke_label": list(SIM_NAO)[0],
    "pred_calc_label": list(FREQUENCIA)[0],
    "pred_mtrans_label": list(TRANSPORTE)[0],
}

for chave, valor_padrao in valores_padrao.items():
    if chave not in st.session_state:
        st.session_state[chave] = valor_padrao

icones = {
    "user": """
        <svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="3"></circle>
        <path d="M5.5 20a6.5 6.5 0 0 1 13 0"></path></svg>
    """,
    "nutrition": """
        <svg viewBox="0 0 24 24"><path d="M12 7c-1.4-2.3-4.8-2.6-6.4-.5-2.3 3.1.2 10.8 6.4 13.5 6.2-2.7 8.7-10.4 6.4-13.5C16.8 4.4 13.4 4.7 12 7Z"></path>
        <path d="M12 7c.1-2.2 1.2-3.8 3.3-4.7"></path></svg>
    """,
    "activity": """
        <svg viewBox="0 0 24 24"><path d="M3 12h4l2-5 4 10 2-5h6"></path></svg>
    """,
    "mobility": """
        <svg viewBox="0 0 24 24"><path d="M5 17h14"></path><path d="M7 17 9 8h6l2 9"></path>
        <circle cx="8" cy="19" r="1.5"></circle><circle cx="16" cy="19" r="1.5"></circle></svg>
    """,
    "bmi": """
        <svg viewBox="0 0 24 24"><path d="M5 20h14"></path>
        <path d="M7 20 5.8 8.8A3 3 0 0 1 8.8 5.5h6.4a3 3 0 0 1 3 3.3L17 20"></path>
        <path d="M9 10a3 3 0 0 1 6 0"></path></svg>
    """,
}


def cabecalho_secao(numero: int, titulo: str, descricao: str, cor: str, icone: str) -> None:
    st.markdown(
        (
            f'<div class="prediction-flow-section" style="--section-accent:{cor}">'
            '<div class="prediction-flow-heading">'
            f'<span class="prediction-flow-number">{numero}</span>'
            f'<span class="prediction-flow-icon">{icones[icone]}</span>'
            '<div>'
            f'<h3>{titulo}</h3>'
            f'<p>{descricao}</p>'
            '</div></div></div>'
        ),
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="prediction-panel-heading prediction-main-heading">
        <span class="prediction-panel-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
                <path d="M9 11h6"></path>
                <path d="M9 15h6"></path>
                <path d="M10 3h4"></path>
                <rect x="5" y="5" width="14" height="16" rx="2"></rect>
            </svg>
        </span>
        <div>
            <h2>Dados para avaliação</h2>
            <p>Preencha as etapas abaixo em sequência. Todos os campos permanecem visíveis para facilitar a revisão.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    cabecalho_secao(
        1,
        "Dados pessoais",
        "Informações demográficas e histórico familiar.",
        "#1769E8",
        "user",
    )
    c1, c2, c3 = st.columns(3)
    c1.selectbox(TITULOS["sexo"], list(SEXO), help=HELP["sexo"], key="pred_sexo_label")
    c2.number_input(
        TITULOS["idade"], min_value=14, max_value=61, step=1,
        help=HELP["idade"], key="pred_idade"
    )
    c3.selectbox(
        TITULOS["historico"], list(SIM_NAO), help=HELP["historico"],
        key="pred_historico_label"
    )

with st.container(border=True):
    cabecalho_secao(
        2,
        "Alimentação",
        "Frequência de consumo, refeições e hidratação.",
        "#12A995",
        "nutrition",
    )
    c1, c2, c3 = st.columns(3)
    c1.selectbox(TITULOS["favc"], list(SIM_NAO), help=HELP["favc"], key="pred_favc_label")
    c2.slider(TITULOS["fcvc"], 1, 3, step=1, help=HELP["fcvc"], key="pred_fcvc")
    c3.slider(TITULOS["ncp"], 1, 4, step=1, help=HELP["ncp"], key="pred_ncp")

    c4, c5, c6 = st.columns(3)
    c4.selectbox(TITULOS["caec"], list(FREQUENCIA), help=HELP["caec"], key="pred_caec_label")
    c5.slider(TITULOS["ch2o"], 1, 3, step=1, help=HELP["ch2o"], key="pred_ch2o")
    c6.selectbox(TITULOS["scc"], list(SIM_NAO), help=HELP["scc"], key="pred_scc_label")

with st.container(border=True):
    cabecalho_secao(
        3,
        "Estilo de vida",
        "Atividade física, tempo de tela e outros hábitos.",
        "#8754C9",
        "activity",
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.slider(TITULOS["faf"], 0, 3, step=1, help=HELP["faf"], key="pred_faf")
    c2.slider(TITULOS["tue"], 0, 2, step=1, help=HELP["tue"], key="pred_tue")
    c3.selectbox(TITULOS["smoke"], list(SIM_NAO), help=HELP["smoke"], key="pred_smoke_label")
    c4.selectbox(TITULOS["calc"], list(FREQUENCIA), help=HELP["calc"], key="pred_calc_label")

with st.container(border=True):
    cabecalho_secao(
        4,
        "Mobilidade",
        "Meio de transporte utilizado com maior frequência.",
        "#D8832F",
        "mobility",
    )
    st.selectbox(
        TITULOS["mtrans"], list(TRANSPORTE), help=HELP["mtrans"],
        key="pred_mtrans_label"
    )
    st.caption(
        "Caminhada e bicicleta originam a feature de transporte ativo utilizada pelo pipeline."
    )

with st.container(border=True):
    cabecalho_secao(
        5,
        "Avaliação complementar",
        "Peso, altura e IMC apoiam a leitura do resultado, mas não são enviados ao modelo.",
        "#0B7A75",
        "bmi",
    )

    col_medidas, col_imc = st.columns([1.05, 1], gap="large")

    with col_medidas:
        col_peso, col_altura = st.columns(2)
        peso = col_peso.number_input(
            "Peso (kg)", min_value=0.0, max_value=350.0, value=0.0,
            step=0.1, format="%.1f", help="Informe o peso atual em quilogramas."
        )
        altura = col_altura.number_input(
            "Altura (m)", min_value=0.0, max_value=2.50, value=0.0,
            step=0.01, format="%.2f", help="Informe a altura em metros. Exemplo: 1,65."
        )
        st.markdown(
            """
            <div class="prediction-complement-note">
                <strong>Por que este cálculo é complementar?</strong>
                <p>O alvo original foi derivado do IMC. Por isso, peso e altura ficam fora do modelo comportamental para evitar uma resposta automática baseada na própria fórmula.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    imc = None
    with col_imc:
        if peso > 0 and altura > 0:
            imc = peso / (altura**2)
            classificacao_imc, classe_visual_imc = classificar_imc(imc)
            card_imc(imc, classificacao_imc, classe_visual_imc)
        else:
            placeholder_imc()

st.markdown(
    """
    <div class="prediction-review-heading">
        <strong>Revisão e envio</strong>
        <span>Confira os dados antes de executar a avaliação.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

aceito = st.checkbox(
    "Confirmo que os dados foram revisados e compreendo que o resultado não substitui avaliação clínica.",
    key="pred_aceito",
)

_, col_enviar, _ = st.columns([1, 1.35, 1])
enviar = col_enviar.button(
    "Avaliar Paciente",
    type="primary",
    use_container_width=True,
    disabled=not aceito,
    key="realizar_predicao",
)

st.markdown('<div class="prediction-result-divider"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="prediction-panel-heading prediction-result-heading">
        <span class="prediction-panel-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
                <path d="M4 19V9"></path><path d="M10 19V5"></path>
                <path d="M16 19v-7"></path><path d="M22 19V3"></path>
            </svg>
        </span>
        <div>
            <h2>Resultado da avaliação</h2>
            <p>A estimativa aparece aqui após o envio, seguida da interpretação e dos detalhes do modelo.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

resultado = None

if enviar:
    dados_usuario = {
        "Gender": SEXO[st.session_state.pred_sexo_label],
        "Age": st.session_state.pred_idade,
        "family_history": SIM_NAO[st.session_state.pred_historico_label],
        "FAVC": SIM_NAO[st.session_state.pred_favc_label],
        "FCVC": st.session_state.pred_fcvc,
        "NCP": st.session_state.pred_ncp,
        "CAEC": FREQUENCIA[st.session_state.pred_caec_label],
        "SMOKE": SIM_NAO[st.session_state.pred_smoke_label],
        "CH2O": st.session_state.pred_ch2o,
        "SCC": SIM_NAO[st.session_state.pred_scc_label],
        "FAF": st.session_state.pred_faf,
        "TUE": st.session_state.pred_tue,
        "CALC": FREQUENCIA[st.session_state.pred_calc_label],
        "MTRANS": TRANSPORTE[st.session_state.pred_mtrans_label],
    }

    try:
        with st.spinner("Processando os dados e consultando o modelo..."):
            time.sleep(0.35)
            resultado = prever(dados_usuario)

        classe = resultado["classe"]
        confianca = resultado["confianca"]

        col_resultado, col_resumo = st.columns([1.25, 1], gap="large")
        with col_resultado:
            renderizar_resultado_lateral(classe, confianca, imc)

        with col_resumo:
            st.markdown(
                (
                    '<div class="prediction-summary-card prediction-summary-main">'
                    '<strong>Resumo dos dados informados</strong>'
                    f'<p>{html.escape(str(st.session_state.pred_sexo_label))} · {st.session_state.pred_idade} anos<br>'
                    f'{html.escape(str(st.session_state.pred_historico_label))} para histórico familiar<br>'
                    f'{html.escape(str(st.session_state.pred_mtrans_label))} como transporte principal.</p>'
                    '</div>'
                ),
                unsafe_allow_html=True,
            )
            st.success("Predição concluída com sucesso.")
            if imc is not None:
                st.caption(
                    f"IMC complementar: {imc:.2f} kg/m². Esse valor não foi utilizado pelo modelo."
                )

        if "Obesidade" in classe:
            estilo = "risk-high"
            interpretacao = (
                "O padrão informado foi associado pelo modelo a uma classe de obesidade. "
                "Recomenda-se avaliação profissional completa e uso do resultado apenas "
                "como sinal de apoio à priorização."
            )
        elif "Sobrepeso" in classe:
            estilo = "risk-medium"
            interpretacao = (
                "O padrão informado foi associado a sobrepeso. O resultado pode apoiar "
                "ações preventivas, mas deve ser confirmado por avaliação clínica."
            )
        elif "Peso insuficiente" in classe:
            estilo = "risk-medium"
            interpretacao = (
                "O padrão informado foi associado a baixo peso. Peso insuficiente também "
                "é clinicamente relevante e pode indicar necessidade de acompanhamento nutricional."
            )
        else:
            estilo = "risk-low"
            interpretacao = (
                "O padrão informado não foi associado a sobrepeso ou obesidade nesta estimativa. "
                "Ainda assim, o resultado não exclui a necessidade de acompanhamento individual."
            )

        st.markdown(
            (
                f'<div class="clinical-interpretation-card {estilo}">'
                '<div class="clinical-interpretation-icon" aria-hidden="true">'
                '<svg viewBox="0 0 24 24"><path d="M9 11h6"></path>'
                '<path d="M9 15h4"></path><path d="M10 3h4"></path>'
                '<rect x="5" y="5" width="14" height="16" rx="2"></rect></svg>'
                '</div><div class="clinical-interpretation-content">'
                '<span>Interpretação clínica</span><h3>Apoio à priorização do cuidado</h3>'
                f'<p>{html.escape(interpretacao)}</p></div></div>'
            ),
            unsafe_allow_html=True,
        )

        probabilidades = resultado["probabilidades"]
        probs = pd.DataFrame(
            {"classe": list(probabilidades.keys()), "probabilidade": list(probabilidades.values())}
        ).sort_values("probabilidade")
        probs["rotulo_probabilidade"] = probs["probabilidade"].map(lambda valor: f"{valor:.1%}")

        fig = px.bar(
            probs, x="probabilidade", y="classe", orientation="h",
            text="rotulo_probabilidade",
            title="Distribuição das probabilidades entre as classes",
        )
        fig.update_layout(xaxis_tickformat=".0%", xaxis_title="Probabilidade", yaxis_title="", height=430)
        st.plotly_chart(fig, use_container_width=True, key="grafico_probabilidades_predicao")

        with st.expander("Como interpretar a confiança"):
            st.write(
                "A confiança corresponde à maior probabilidade produzida pelo modelo. "
                "Ela não representa certeza clínica e pode ser menor quando diferentes "
                "classes apresentam padrões comportamentais semelhantes."
            )

        with st.expander("Fatores gerais mais relevantes para o modelo"):
            importancia = obter_importancia_global().head(10).sort_values("importancia")
            fig_imp = px.bar(
                importancia, x="importancia", y="variavel", orientation="h",
                title="Importância global agregada das variáveis",
            )
            fig_imp.update_layout(xaxis_title="Importância no Random Forest", yaxis_title="", height=420)
            st.plotly_chart(fig_imp, use_container_width=True, key="grafico_importancia_global_predicao")
            st.caption(
                "Esta é uma explicação global do modelo, não uma justificativa causal e individual da predição. "
                "SHAP não foi incluído para evitar adicionar uma dependência não utilizada no treinamento original."
            )

    except Exception as erro:
        st.error(
            "Não foi possível realizar a predição. Verifique os dados e a disponibilidade do modelo."
        )
        with st.expander("Detalhes técnicos do erro"):
            st.code(str(erro))
else:
    st.markdown(
        """
        <div class="prediction-placeholder-card prediction-placeholder-wide">
            <span class="prediction-placeholder-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24">
                    <path d="M4 19V9"></path><path d="M10 19V5"></path>
                    <path d="M16 19v-7"></path><path d="M22 19V3"></path>
                </svg>
            </span>
            <div>
                <strong>Resultado aguardando predição</strong>
                <p>Preencha as etapas acima, revise os dados e clique em “Realizar a predição”.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

rodape()