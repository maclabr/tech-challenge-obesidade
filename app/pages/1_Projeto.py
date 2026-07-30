import streamlit as st

from utils.styles import aplicar_estilos, hero, rodape


aplicar_estilos()

st.markdown(
    """
    <style>
    .project-intro-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin: 0.35rem 0 2rem 0;
    }

    .project-info-card {
        position: relative;
        min-height: 218px;
        padding: 1.45rem 1.35rem 1.35rem;
        overflow: hidden;
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 16px;
        box-shadow: var(--shadow-sm);
        transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
    }

    .project-info-card::before {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        left: 0;
        height: 4px;
    }

    .project-info-card:nth-child(1)::before {
        background: linear-gradient(90deg, #12A995, #69D3C4);
    }

    .project-info-card:nth-child(2)::before {
        background: linear-gradient(90deg, #1769E8, #6DA6F7);
    }

    .project-info-card:nth-child(3)::before {
        background: linear-gradient(90deg, #9650E6, #C18AF2);
    }

    .project-info-card:hover {
        transform: translateY(-3px);
        border-color: #C8DDDA;
        box-shadow: 0 14px 30px rgba(11, 21, 56, 0.09);
    }

    .project-card-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 46px;
        height: 46px;
        margin-bottom: 1rem;
        border-radius: 13px;
        font-size: 1.35rem;
    }

    .project-card-icon svg,
    .project-method-icon svg,
    .project-disclaimer-icon svg {
        width: 22px;
        height: 22px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.9;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .project-info-card:nth-child(1) .project-card-icon {
        color: #0B8F7E;
        background: #E8F8F5;
    }

    .project-info-card:nth-child(2) .project-card-icon {
        color: #1769E8;
        background: #EAF3FF;
    }

    .project-info-card:nth-child(3) .project-card-icon {
        color: #8A45D1;
        background: #F4EAFF;
    }

    .project-info-card h3 {
        margin: 0 0 0.7rem 0;
        color: var(--navy);
        font-size: 1.05rem;
        font-weight: 740;
    }

    .project-info-card p {
        margin: 0;
        color: var(--text);
        font-size: 0.88rem;
        line-height: 1.7;
    }

    .project-section-heading {
        margin: 0 0 1.1rem 0;
    }

    .project-section-kicker {
        margin-bottom: 0.3rem;
        color: var(--primary-dark);
        font-size: 0.73rem;
        font-weight: 760;
        letter-spacing: 0.075em;
        text-transform: uppercase;
    }

    .project-section-heading h2 {
        margin: 0;
        color: var(--navy);
        font-size: clamp(1.45rem, 2vw, 1.9rem);
    }

    .project-section-heading p {
        max-width: 780px;
        margin: 0.45rem 0 0 0;
        color: var(--muted);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .project-flow {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 0.85rem;
        margin-bottom: 2rem;
    }

    .project-flow-step {
        position: relative;
        min-height: 150px;
        padding: 1.15rem 1rem;
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 14px;
        box-shadow: var(--shadow-sm);
        text-align: center;
    }

    .project-flow-step:not(:last-child)::after {
        content: "→";
        position: absolute;
        top: 50%;
        right: -0.72rem;
        z-index: 2;
        width: 1.45rem;
        height: 1.45rem;
        transform: translateY(-50%);
        color: var(--primary);
        font-size: 1.15rem;
        font-weight: 800;
        line-height: 1.35rem;
        background: var(--bg);
        border-radius: 999px;
    }

    .project-flow-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 34px;
        height: 34px;
        margin-bottom: 0.75rem;
        color: #FFFFFF;
        font-size: 0.8rem;
        font-weight: 750;
        background: linear-gradient(145deg, var(--primary-dark), var(--primary));
        border-radius: 10px;
        box-shadow: 0 5px 12px rgba(0, 158, 142, 0.18);
    }

    .project-flow-step h4 {
        margin: 0 0 0.45rem 0;
        color: var(--navy);
        font-size: 0.93rem;
        font-weight: 720;
    }

    .project-flow-step p {
        margin: 0;
        color: var(--muted);
        font-size: 0.76rem;
        line-height: 1.5;
    }

    .project-method-card {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 1rem;
        align-items: flex-start;
        margin-bottom: 2rem;
        padding: 1.4rem 1.45rem;
        background: linear-gradient(135deg, #F7FCFB 0%, #FFFFFF 100%);
        border: 1px solid #DCEDEA;
        border-radius: 16px;
        box-shadow: var(--shadow-sm);
    }

    .project-method-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 48px;
        height: 48px;
        color: var(--primary-dark);
        background: var(--primary-soft);
        border-radius: 13px;
        font-size: 1.35rem;
    }

    .project-method-card h3 {
        margin: 0 0 0.45rem 0;
        color: var(--navy);
        font-size: 1.03rem;
    }

    .project-method-card p {
        margin: 0;
        color: var(--text);
        font-size: 0.88rem;
        line-height: 1.7;
    }

    .tech-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.65rem;
        margin: 0.2rem 0 2rem 0;
    }

    .tech-badge {
        display: inline-flex;
        align-items: center;
        min-height: 38px;
        padding: 0.55rem 0.8rem;
        color: var(--navy);
        font-size: 0.79rem;
        font-weight: 680;
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 10px;
        box-shadow: 0 2px 7px rgba(11, 21, 56, 0.035);
    }

    .project-disclaimer {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 0.9rem;
        align-items: flex-start;
        padding: 1.2rem 1.25rem;
        background: #FFF9EE;
        border: 1px solid #F0DFC0;
        border-radius: 14px;
    }

    .project-disclaimer-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 38px;
        height: 38px;
        color: #9A6815;
        background: #FFF1D2;
        border-radius: 10px;
        font-size: 1.25rem;
        line-height: 1.2;
    }

    .project-disclaimer strong {
        display: block;
        margin-bottom: 0.25rem;
        color: #7A5311;
        font-size: 0.88rem;
    }

    .project-disclaimer p {
        margin: 0;
        color: #694D20;
        font-size: 0.83rem;
        line-height: 1.6;
    }

    @media (max-width: 1050px) {
        .project-intro-grid {
            grid-template-columns: 1fr;
        }

        .project-info-card {
            min-height: auto;
        }

        .project-flow {
            grid-template-columns: 1fr;
        }

        .project-flow-step {
            min-height: auto;
            text-align: left;
        }

        .project-flow-step:not(:last-child)::after {
            content: "↓";
            top: auto;
            right: 50%;
            bottom: -0.72rem;
            transform: translateX(50%);
            text-align: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

hero(
    "Sobre o projeto",
    "Contexto de negócio, recorte metodológico e fluxo de desenvolvimento do Tech Challenge.",
)

st.markdown(
    """
    <div class="project-intro-grid">
        <div class="project-info-card">
            <div class="project-card-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"></circle><circle cx="12" cy="12" r="3"></circle><path d="M12 4V2"></path><path d="M20 12h2"></path><path d="M12 20v2"></path><path d="M4 12H2"></path></svg></div>
            <h3>Objetivo</h3>
            <p>
                Desenvolver uma solução de Machine Learning capaz de estimar o nível
                de obesidade de pacientes a partir de características individuais,
                histórico familiar e hábitos de vida, apoiando ações preventivas e a
                priorização do cuidado.
            </p>
        </div>
        <div class="project-info-card">
            <div class="project-card-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 21V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v14"></path><path d="M9 21v-4h6v4"></path><path d="M9 10h6"></path><path d="M12 7v6"></path><path d="M2 21h20"></path></svg></div>
            <h3>Cenário de produção</h3>
            <p>
                A aplicação utiliza o cenário comportamental, que exclui altura, peso
                e IMC. Essa decisão evita que o modelo apenas reproduza a fórmula usada
                originalmente para definir o alvo.
            </p>
        </div>
        <div class="project-info-card">
            <div class="project-card-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"></path><path d="M3 10h18"></path></svg></div>
            <h3>Fonte de dados</h3>
            <p>
                Dataset público <em>Estimation of Obesity Levels</em>, com informações
                demográficas, alimentares, de atividade física e estilo de vida.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="project-section-heading">
        <div class="project-section-kicker">Jornada analítica</div>
        <h2>Etapas realizadas</h2>
        <p>
            O desenvolvimento foi estruturado para transformar os dados brutos em uma
            experiência analítica e preditiva acessível dentro do Streamlit.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="project-flow">
        <div class="project-flow-step">
            <div class="project-flow-number">01</div>
            <h4>Validação</h4>
            <p>Conferência do schema, tipos de dados e consistência inicial.</p>
        </div>
        <div class="project-flow-step">
            <div class="project-flow-number">02</div>
            <h4>Tratamento</h4>
            <p>Limpeza de duplicatas e arredondamento das escalas ordinais.</p>
        </div>
        <div class="project-flow-step">
            <div class="project-flow-number">03</div>
            <h4>Engenharia</h4>
            <p>Construção e organização das variáveis comportamentais.</p>
        </div>
        <div class="project-flow-step">
            <div class="project-flow-number">04</div>
            <h4>Modelagem</h4>
            <p>Comparação de algoritmos e seleção do Random Forest.</p>
        </div>
        <div class="project-flow-step">
            <div class="project-flow-number">05</div>
            <h4>Aplicação</h4>
            <p>Deploy da predição e dos indicadores em uma interface Streamlit.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="project-method-card">
        <div class="project-method-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 4.5A3 3 0 0 0 6 7.4 3 3 0 0 0 4.5 13 3 3 0 0 0 8 17.6 3 3 0 0 0 12 20V4a3 3 0 0 0-2.5.5Z"></path><path d="M14.5 4.5A3 3 0 0 1 18 7.4a3 3 0 0 1 1.5 5.6 3 3 0 0 1-3.5 4.6A3 3 0 0 1 12 20V4a3 3 0 0 1 2.5.5Z"></path><path d="M8 9h2"></path><path d="M14 9h2"></path><path d="M8 15h2"></path><path d="M14 15h2"></path></svg></div>
        <div>
            <h3>Decisão metodológica</h3>
            <p>
                O cenário comportamental foi priorizado para que a estimativa represente
                padrões de hábitos e contexto individual, reduzindo a dependência direta
                de medidas antropométricas utilizadas na construção original do alvo.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="project-section-heading">
        <div class="project-section-kicker">Stack do projeto</div>
        <h2>Tecnologias utilizadas</h2>
        <p>
            Ferramentas utilizadas na preparação dos dados, modelagem, visualização e
            disponibilização da aplicação.
        </p>
    </div>

    <div class="tech-badges">
        <span class="tech-badge">Python</span>
        <span class="tech-badge">Pandas</span>
        <span class="tech-badge">Scikit-learn</span>
        <span class="tech-badge">Random Forest</span>
        <span class="tech-badge">Plotly</span>
        <span class="tech-badge">Streamlit</span>
        <span class="tech-badge">Joblib</span>
        <span class="tech-badge">Git &amp; GitHub</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="project-disclaimer">
        <div class="project-disclaimer-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10.3 3.6 2.4 17.5A2 2 0 0 0 4.1 20h15.8a2 2 0 0 0 1.7-2.5L13.7 3.6a2 2 0 0 0-3.4 0Z"></path><path d="M12 9v4"></path><path d="M12 17h.01"></path></svg></div>
        <div>
            <strong>Uso acadêmico e demonstrativo</strong>
            <p>
                A aplicação não substitui diagnóstico, avaliação antropométrica ou
                decisão de um profissional de saúde. Os resultados devem ser interpretados
                como apoio analítico dentro do contexto deste Tech Challenge.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

rodape()