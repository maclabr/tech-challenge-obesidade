"""Página de metodologia, desempenho e interpretabilidade do modelo."""

import re
from textwrap import dedent

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


def renderizar_html(conteudo: str) -> None:
    """Renderiza componentes HTML sem interferência da indentação."""

    html_limpo = " ".join(
        linha.strip()
        for linha in dedent(conteudo).splitlines()
        if linha.strip()
    )
    html_limpo = re.sub(r">\s+<", "><", html_limpo)
    st.markdown(html_limpo, unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .model-page {
        --model-navy: #0B1538;
        --model-blue: #3157C8;
        --model-teal: #009E8E;
        --model-text: #253252;
        --model-muted: #66728A;
        --model-border: #E4E9F1;
        --model-soft: #F6F8FC;
    }

    .model-hero {
        position: relative;
        overflow: hidden;
        display: grid;
        grid-template-columns: minmax(0, 1.35fr) minmax(250px, 0.65fr);
        gap: 2rem;
        align-items: center;
        padding: 2.2rem 2.3rem;
        margin-bottom: 1.35rem;
        background:
            radial-gradient(circle at 88% 18%, rgba(0, 158, 142, 0.18), transparent 25%),
            linear-gradient(135deg, #0B1538 0%, #132758 58%, #173A63 100%);
        border-radius: 22px;
        box-shadow: 0 16px 40px rgba(11, 21, 56, 0.16);
    }

    .model-hero::after {
        content: "";
        position: absolute;
        width: 250px;
        height: 250px;
        right: -95px;
        bottom: -130px;
        border-radius: 50%;
        border: 38px solid rgba(255, 255, 255, 0.05);
    }

    .model-hero-copy {
        position: relative;
        z-index: 1;
    }

    .model-eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 0.48rem;
        margin-bottom: 0.9rem;
        padding: 0.42rem 0.7rem;
        color: #C7F5EE;
        font-size: 0.74rem;
        font-weight: 750;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background: rgba(255, 255, 255, 0.09);
        border: 1px solid rgba(255, 255, 255, 0.13);
        border-radius: 999px;
    }

    .model-eyebrow svg {
        width: 15px;
        height: 15px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-hero h1 {
        max-width: 760px;
        margin: 0 0 0.8rem;
        color: #FFFFFF;
        font-size: clamp(2rem, 4vw, 3.25rem);
        line-height: 1.08;
        letter-spacing: -0.045em;
    }

    .model-hero p {
        max-width: 720px;
        margin: 0;
        color: #DCE5F6;
        font-size: 0.98rem;
        line-height: 1.75;
    }

    .model-hero-visual {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 190px;
    }

    .model-orbit {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 168px;
        height: 168px;
        border: 1px solid rgba(255, 255, 255, 0.16);
        border-radius: 50%;
    }

    .model-orbit::before,
    .model-orbit::after {
        content: "";
        position: absolute;
        border-radius: 50%;
        border: 1px solid rgba(255, 255, 255, 0.11);
    }

    .model-orbit::before {
        width: 122px;
        height: 122px;
    }

    .model-orbit::after {
        width: 205px;
        height: 205px;
    }

    .model-brain {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 88px;
        height: 88px;
        color: #FFFFFF;
        background: linear-gradient(145deg, #00B7A5, #178A99);
        border-radius: 24px;
        box-shadow: 0 16px 35px rgba(0, 158, 142, 0.28);
    }

    .model-brain svg {
        width: 48px;
        height: 48px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.65;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.9rem;
        margin: 0 0 1.8rem;
    }

    .model-kpi {
        position: relative;
        overflow: hidden;
        min-height: 142px;
        padding: 1.1rem 1.1rem 1rem 1.2rem;
        background: #FFFFFF;
        border: 1px solid var(--model-border);
        border-radius: 16px;
        box-shadow: 0 7px 20px rgba(11, 21, 56, 0.055);
    }

    .model-kpi::before {
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 5px;
        background: var(--accent);
    }

    .model-kpi-top {
        display: flex;
        justify-content: space-between;
        gap: 0.8rem;
        align-items: flex-start;
    }

    .model-kpi-label {
        color: var(--model-muted);
        font-size: 0.75rem;
        font-weight: 760;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    .model-kpi-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        color: var(--accent);
        background: var(--icon-bg);
        border-radius: 10px;
    }

    .model-kpi-icon svg {
        width: 19px;
        height: 19px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.9;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-kpi-value {
        display: block;
        margin-top: 0.82rem;
        color: var(--model-navy);
        font-size: 1.9rem;
        font-weight: 800;
        line-height: 1;
        letter-spacing: -0.04em;
    }

    .model-kpi-note {
        display: block;
        margin-top: 0.45rem;
        color: var(--model-muted);
        font-size: 0.76rem;
        line-height: 1.45;
    }

    .model-section-title {
        margin: 2rem 0 0.9rem;
    }

    .model-section-title span {
        display: block;
        margin-bottom: 0.24rem;
        color: var(--model-teal);
        font-size: 0.71rem;
        font-weight: 800;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .model-section-title h2 {
        margin: 0;
        color: var(--model-navy);
        font-size: 1.45rem;
        letter-spacing: -0.025em;
    }

    .model-choice {
        display: grid;
        grid-template-columns: minmax(220px, 0.72fr) minmax(0, 1.28fr);
        gap: 1rem;
        margin-bottom: 1rem;
    }

    .model-choice-primary {
        padding: 1.4rem;
        color: #FFFFFF;
        background: linear-gradient(145deg, #173A63, #0B1538);
        border-radius: 18px;
        box-shadow: 0 12px 28px rgba(11, 21, 56, 0.12);
    }

    .model-choice-primary svg {
        width: 42px;
        height: 42px;
        margin-bottom: 1rem;
        fill: none;
        stroke: #72D9CC;
        stroke-width: 1.6;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-choice-primary small {
        display: block;
        color: #9FB0D1;
        font-size: 0.7rem;
        font-weight: 760;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .model-choice-primary strong {
        display: block;
        margin-top: 0.35rem;
        font-size: 1.55rem;
        letter-spacing: -0.03em;
    }

    .model-choice-primary p {
        margin: 0.75rem 0 0;
        color: #D8E2F3;
        font-size: 0.82rem;
        line-height: 1.65;
    }

    .model-choice-text {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 1.4rem 1.5rem;
        background: #FFFFFF;
        border: 1px solid var(--model-border);
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(11, 21, 56, 0.05);
    }

    .model-choice-text h3 {
        margin: 0 0 0.55rem;
        color: var(--model-navy);
        font-size: 1.06rem;
    }

    .model-choice-text p {
        margin: 0;
        color: var(--model-muted);
        font-size: 0.86rem;
        line-height: 1.72;
    }

    .model-reasons {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.8rem;
    }

    .model-reason {
        min-height: 155px;
        padding: 1.05rem;
        background: var(--model-soft);
        border: 1px solid var(--model-border);
        border-radius: 15px;
    }

    .model-reason svg {
        width: 24px;
        height: 24px;
        margin-bottom: 0.75rem;
        fill: none;
        stroke: var(--model-teal);
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-reason h4 {
        margin: 0 0 0.35rem;
        color: var(--model-navy);
        font-size: 0.86rem;
    }

    .model-reason p {
        margin: 0;
        color: var(--model-muted);
        font-size: 0.76rem;
        line-height: 1.55;
    }

    .model-specs {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.85rem;
        margin-top: 1rem;
    }

    .model-spec {
        display: flex;
        gap: 0.85rem;
        align-items: center;
        padding: 1rem 1.05rem;
        background: #FFFFFF;
        border: 1px solid var(--model-border);
        border-radius: 14px;
    }

    .model-spec-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 0 0 38px;
        width: 38px;
        height: 38px;
        color: var(--model-blue);
        background: #EEF3FF;
        border-radius: 10px;
    }

    .model-spec-icon svg {
        width: 20px;
        height: 20px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-spec small {
        display: block;
        color: var(--model-muted);
        font-size: 0.7rem;
    }

    .model-spec strong {
        display: block;
        margin-top: 0.13rem;
        color: var(--model-navy);
        font-size: 0.93rem;
    }

    .model-flow {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 0.75rem;
        margin-bottom: 1rem;
    }

    .model-flow-step {
        position: relative;
        min-height: 142px;
        padding: 1rem;
        text-align: center;
        background: #FFFFFF;
        border: 1px solid var(--model-border);
        border-radius: 15px;
    }

    .model-flow-step:not(:last-child)::after {
        content: "→";
        position: absolute;
        top: 50%;
        right: -0.64rem;
        z-index: 2;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 1.25rem;
        height: 1.25rem;
        color: var(--model-teal);
        background: #FFFFFF;
        font-weight: 800;
        transform: translateY(-50%);
    }

    .model-flow-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 27px;
        height: 27px;
        margin-bottom: 0.65rem;
        color: #FFFFFF;
        background: var(--model-teal);
        border-radius: 8px;
        font-size: 0.72rem;
        font-weight: 800;
    }

    .model-flow-step strong {
        display: block;
        color: var(--model-navy);
        font-size: 0.83rem;
    }

    .model-flow-step p {
        margin: 0.38rem 0 0;
        color: var(--model-muted);
        font-size: 0.71rem;
        line-height: 1.45;
    }

    .model-note {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 0.9rem;
        align-items: flex-start;
        padding: 1.1rem 1.2rem;
        margin-top: 0.85rem;
        background: #F1F8F7;
        border: 1px solid #CFE8E4;
        border-radius: 14px;
    }

    .model-note.warning {
        background: #FFF9EE;
        border-color: #F0DFC0;
    }

    .model-note-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 38px;
        height: 38px;
        color: #087D71;
        background: #DDF2EF;
        border-radius: 10px;
    }

    .model-note.warning .model-note-icon {
        color: #9A6815;
        background: #FFF1D2;
    }

    .model-note-icon svg {
        width: 20px;
        height: 20px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .model-note strong {
        display: block;
        margin-bottom: 0.24rem;
        color: var(--model-navy);
        font-size: 0.84rem;
    }

    .model-note p {
        margin: 0;
        color: var(--model-muted);
        font-size: 0.79rem;
        line-height: 1.6;
    }

    @media (max-width: 1050px) {
        .model-hero,
        .model-choice {
            grid-template-columns: 1fr;
        }

        .model-hero-visual {
            display: none;
        }

        .model-kpi-grid,
        .model-reasons {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        .model-flow {
            grid-template-columns: 1fr;
        }

        .model-flow-step {
            min-height: auto;
            text-align: left;
        }

        .model-flow-step:not(:last-child)::after {
            content: "↓";
            top: auto;
            right: 50%;
            bottom: -0.66rem;
            transform: translateX(50%);
        }
    }

    @media (max-width: 700px) {
        .model-hero {
            padding: 1.5rem;
        }

        .model-kpi-grid,
        .model-reasons,
        .model-specs {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

hero(
    "Modelo de Machine Learning",
    "Metodologia, desempenho e interpretabilidade do Random Forest selecionado para o cenário comportamental da aplicação.",
)

renderizar_html(
    """
    <div class="model-page">
        <section class="model-kpi-grid">
            <article class="model-kpi" style="--accent:#3157C8;--icon-bg:#EEF3FF;">
                <div class="model-kpi-top">
                    <span class="model-kpi-label">Accuracy CV</span>
                    <div class="model-kpi-icon">
                        <svg viewBox="0 0 24 24"><path d="M4 19V9"></path><path d="M10 19V5"></path><path d="M16 19v-7"></path><path d="M22 19V3"></path></svg>
                    </div>
                </div>
                <strong class="model-kpi-value">79,6%</strong>
                <span class="model-kpi-note">Média obtida na validação cruzada.</span>
            </article>

            <article class="model-kpi" style="--accent:#009E8E;--icon-bg:#E6F7F4;">
                <div class="model-kpi-top">
                    <span class="model-kpi-label">Accuracy teste</span>
                    <div class="model-kpi-icon">
                        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><path d="m9 12 2 2 4-5"></path></svg>
                    </div>
                </div>
                <strong class="model-kpi-value">79,4%</strong>
                <span class="model-kpi-note">Desempenho no conjunto de teste.</span>
            </article>

            <article class="model-kpi" style="--accent:#7B61C8;--icon-bg:#F1EEFB;">
                <div class="model-kpi-top">
                    <span class="model-kpi-label">F1-macro CV</span>
                    <div class="model-kpi-icon">
                        <svg viewBox="0 0 24 24"><path d="M5 18 10 13l3 3 6-8"></path><path d="M15 8h4v4"></path></svg>
                    </div>
                </div>
                <strong class="model-kpi-value">78,9%</strong>
                <span class="model-kpi-note">Equilíbrio médio entre as classes.</span>
            </article>

            <article class="model-kpi" style="--accent:#D68A2F;--icon-bg:#FFF4E6;">
                <div class="model-kpi-top">
                    <span class="model-kpi-label">Meta do projeto</span>
                    <div class="model-kpi-icon">
                        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><circle cx="12" cy="12" r="3"></circle><path d="M12 4V2"></path></svg>
                    </div>
                </div>
                <strong class="model-kpi-value">75,0%</strong>
                <span class="model-kpi-note">Meta de desempenho atingida.</span>
            </article>
        </section>

        <div class="model-section-title">
            <span>Escolha técnica</span>
            <h2>Por que Random Forest?</h2>
        </div>

        <section class="model-choice">
            <article class="model-choice-primary">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                    <path d="M12 3v18"></path>
                    <path d="M12 7 7 4"></path>
                    <path d="M12 10 17 6"></path>
                    <path d="M12 14 6 11"></path>
                    <path d="M12 17 18 13"></path>
                </svg>
                <small>Modelo selecionado</small>
                <strong>Random Forest</strong>
                <p>
                    Algoritmo de árvores em conjunto adotado para o cenário
                    comportamental da aplicação.
                </p>
            </article>

            <article class="model-choice-text">
                <h3>Equilíbrio entre desempenho e estabilidade</h3>
                <p>
                    Embora o XGBoost tenha alcançado a maior média de validação
                    cruzada, o Random Forest foi recomendado para produção por
                    apresentar desempenho muito próximo, menor diferença entre
                    validação e teste, treinamento mais rápido e menor sinal de
                    overfitting.
                </p>
            </article>
        </section>

        <section class="model-reasons">
            <article class="model-reason">
                <svg viewBox="0 0 24 24"><path d="m5 12 4 4L19 6"></path></svg>
                <h4>Desempenho consistente</h4>
                <p>Métricas próximas entre validação cruzada e conjunto de teste.</p>
            </article>
            <article class="model-reason">
                <svg viewBox="0 0 24 24"><path d="M5 9h14"></path><path d="m8 6-3 3 3 3"></path><path d="M19 15H5"></path><path d="m16 12 3 3-3 3"></path></svg>
                <h4>Boa generalização</h4>
                <p>Menor sinal de sobreajuste diante dos modelos comparados.</p>
            </article>
            <article class="model-reason">
                <svg viewBox="0 0 24 24"><path d="m13 2-8 12h7l-1 8 8-12h-7z"></path></svg>
                <h4>Eficiência operacional</h4>
                <p>Treinamento e inferência adequados para uma aplicação interativa.</p>
            </article>
            <article class="model-reason">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><path d="M12 8v4l3 2"></path></svg>
                <h4>Interpretabilidade</h4>
                <p>Permite analisar a contribuição global das variáveis nas árvores.</p>
            </article>
        </section>
    </div>
    """
)

try:
    pipeline = carregar_modelo()
    modelo = pipeline.named_steps["modelo"]

    renderizar_html(
        f"""
        <div class="model-page">
            <section class="model-specs">
                <article class="model-spec">
                    <div class="model-spec-icon">
                        <svg viewBox="0 0 24 24"><path d="M12 3v18"></path><path d="M12 7 7 4"></path><path d="M12 10 17 6"></path><path d="M12 14 6 11"></path></svg>
                    </div>
                    <div>
                        <small>Algoritmo</small>
                        <strong>Random Forest</strong>
                    </div>
                </article>
                <article class="model-spec">
                    <div class="model-spec-icon">
                        <svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="2"></circle><circle cx="18" cy="6" r="2"></circle><circle cx="12" cy="18" r="2"></circle><path d="M8 7.5 11 16"></path><path d="m16 7.5-3 8.5"></path></svg>
                    </div>
                    <div>
                        <small>Quantidade de árvores</small>
                        <strong>{modelo.n_estimators}</strong>
                    </div>
                </article>
                <article class="model-spec">
                    <div class="model-spec-icon">
                        <svg viewBox="0 0 24 24"><path d="M4 5h16"></path><path d="M4 12h16"></path><path d="M4 19h16"></path><circle cx="8" cy="5" r="1.5"></circle><circle cx="15" cy="12" r="1.5"></circle><circle cx="11" cy="19" r="1.5"></circle></svg>
                    </div>
                    <div>
                        <small>Features de entrada</small>
                        <strong>{len(pipeline.feature_names_in_)}</strong>
                    </div>
                </article>
            </section>
        </div>
        """
    )
except Exception as erro:
    st.warning(f"Não foi possível inspecionar a pipeline: {erro}")

renderizar_html(
    """
    <div class="model-page">
        <div class="model-section-title">
            <span>Interpretabilidade</span>
            <h2>Importância global das variáveis</h2>
        </div>
    </div>
    """
)

importancia = obter_importancia_global().head(12).sort_values("importancia")
figura = px.bar(
    importancia,
    x="importancia",
    y="variavel",
    orientation="h",
    labels={"importancia": "Importância agregada", "variavel": ""},
)
figura.update_traces(
    marker_color="#009E8E",
    texttemplate="<b>%{x:.3f}</b>",
    textposition="outside",
    cliponaxis=False,
    hovertemplate="<b>%{y}</b><br>Importância: %{x:.3f}<extra></extra>",
)
figura.update_layout(
    height=510,
    margin=dict(l=20, r=70, t=25, b=45),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#253252"),
    xaxis=dict(showgrid=True, gridcolor="#E8EDF3", zeroline=False),
    yaxis=dict(title=""),
    showlegend=False,
)
with st.container(border=True):
    st.plotly_chart(figura, use_container_width=True)

st.caption(
    "A importância global representa a contribuição agregada das variáveis "
    "nas divisões das árvores. Ela não prova causalidade e não substitui "
    "interpretação clínica."
)

renderizar_html(
    """
    <div class="model-page">
        <div class="model-section-title">
            <span>Arquitetura</span>
            <h2>Fluxo da pipeline de produção</h2>
        </div>

        <section class="model-flow">
            <article class="model-flow-step">
                <span class="model-flow-number">01</span>
                <strong>Dados de entrada</strong>
                <p>Variáveis demográficas e comportamentais informadas na aplicação.</p>
            </article>
            <article class="model-flow-step">
                <span class="model-flow-number">02</span>
                <strong>Pré-processamento</strong>
                <p>Tratamentos aplicados de forma integrada e reproduzível.</p>
            </article>
            <article class="model-flow-step">
                <span class="model-flow-number">03</span>
                <strong>Codificação</strong>
                <p>StandardScaler, preservação ordinal e OneHotEncoder.</p>
            </article>
            <article class="model-flow-step">
                <span class="model-flow-number">04</span>
                <strong>Random Forest</strong>
                <p>Conjunto de árvores estima as probabilidades por classe.</p>
            </article>
            <article class="model-flow-step">
                <span class="model-flow-number">05</span>
                <strong>Predição final</strong>
                <p>Resultado apresentado ao usuário de forma organizada.</p>
            </article>
        </section>

        <aside class="model-note">
            <div class="model-note-icon">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><path d="M12 11v5"></path><path d="M12 8h.01"></path></svg>
            </div>
            <div>
                <strong>Pipeline integrada</strong>
                <p>
                    O arquivo joblib reúne pré-processamento e modelo, reduzindo
                    o risco de inconsistência entre treinamento e predição.
                </p>
            </div>
        </aside>

        <aside class="model-note warning">
            <div class="model-note-icon">
                <svg viewBox="0 0 24 24"><path d="M10.3 4.3 2.8 17.2A2 2 0 0 0 4.5 20h15a2 2 0 0 0 1.7-2.8L13.7 4.3a2 2 0 0 0-3.4 0Z"></path><path d="M12 9v4"></path><path d="M12 16h.01"></path></svg>
            </div>
            <div>
                <strong>Limitação metodológica</strong>
                <p>
                    O alvo do dataset original está relacionado a faixas de IMC.
                    Para evitar circularidade, o modelo em produção exclui altura,
                    peso e IMC, utilizando variáveis demográficas e comportamentais.
                </p>
            </div>
        </aside>
    </div>
    """
)

rodape()