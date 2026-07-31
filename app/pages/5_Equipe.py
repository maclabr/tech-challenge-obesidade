import html
from textwrap import dedent

import streamlit as st

from utils.styles import aplicar_estilos, hero, rodape


EQUIPE = [
    {
        "nome": "Maria Clara Silva",
        "papel": "Análise de dados, modelagem e deploy",
        "descricao": (
            "Atuação na análise exploratória dos dados, desenvolvimento e avaliação "
            "dos modelos de Machine Learning, seleção do Random Forest e definição "
            "do cenário comportamental utilizado na aplicação. Também participou da "
            "preparação e publicação da solução."
        ),
        "icone": "modelo",
    },
    {
        "nome": "Sabrina Nascimento",
        "papel": "Modelagem e consolidação técnica",
        "descricao": (
            "Atuação na continuidade da etapa de modelagem, organização dos "
            "experimentos e consolidação do notebook final. Contribuiu para a "
            "documentação das análises, resultados e decisões técnicas adotadas "
            "no desenvolvimento do modelo."
        ),
        "icone": "processo",
    },
    {
        "nome": "Iara Portuense",
        "papel": "Dashboard analítico e aplicação Streamlit",
        "descricao": (
            "Responsável pelo desenvolvimento do dashboard analítico e pela "
            "construção da interface da aplicação em Streamlit. Atuou na organização "
            "das páginas, experiência do usuário, identidade visual, apresentação "
            "dos indicadores e integração do fluxo de predição."
        ),
        "icone": "dashboard",
    },
]


ICONES = {
    "modelo": """
        <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M4 19V9"></path>
            <path d="M10 19V5"></path>
            <path d="M16 19v-7"></path>
            <path d="M22 19V3"></path>
            <path d="M2 19h22"></path>
        </svg>
    """,
    "processo": """
        <svg viewBox="0 0 24 24" aria-hidden="true">
            <rect x="3" y="3" width="6" height="6" rx="1.5"></rect>
            <rect x="15" y="3" width="6" height="6" rx="1.5"></rect>
            <rect x="9" y="15" width="6" height="6" rx="1.5"></rect>
            <path d="M6 9v2a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V9"></path>
            <path d="M12 13v2"></path>
        </svg>
    """,
    "dashboard": """
        <svg viewBox="0 0 24 24" aria-hidden="true">
            <rect x="3" y="3" width="18" height="18" rx="2"></rect>
            <path d="M8 17v-5"></path>
            <path d="M12 17V7"></path>
            <path d="M16 17v-8"></path>
        </svg>
    """,
}

ICONES = {chave: dedent(valor).strip() for chave, valor in ICONES.items()}


def criar_card_integrante(integrante: dict[str, str]) -> str:
    """Monta o cartão individual de uma integrante da equipe."""

    return dedent(
        f"""
        <article class="team-card">
            <div class="team-card-icon">
                {ICONES[integrante['icone']]}
            </div>
            <div class="team-card-content">
                <h3>{html.escape(integrante['nome'])}</h3>
                <div class="team-card-role">{html.escape(integrante['papel'])}</div>
                <p>{html.escape(integrante['descricao'])}</p>
            </div>
        </article>
        """
    ).strip()


aplicar_estilos()

st.markdown(
    """
    <style>
    .team-intro {
        max-width: 980px;
        margin: 0.2rem auto 2rem;
        text-align: center;
    }

    .team-intro-kicker,
    .team-section-kicker {
        margin-bottom: 0.45rem;
        color: var(--primary-dark);
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .team-intro h2,
    .team-section-heading h2 {
        margin: 0;
        color: var(--navy);
        font-size: clamp(1.45rem, 2.1vw, 1.9rem);
        line-height: 1.2;
    }

    .team-intro p,
    .team-section-heading p {
        margin: 0.75rem auto 0;
        color: var(--muted);
        font-size: 0.96rem;
        line-height: 1.72;
    }

    .team-intro p {
        max-width: 860px;
    }

    .team-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1.15rem;
        align-items: stretch;
        margin: 0 0 2.65rem;
    }

    .team-card {
        position: relative;
        display: flex;
        min-height: 350px;
        flex-direction: column;
        overflow: hidden;
        padding: 1.55rem;
        border: 1px solid transparent;
        border-radius: 20px;
        box-shadow: 0 10px 28px rgba(15, 35, 52, 0.08);
        transition:
            transform 170ms ease,
            box-shadow 170ms ease;
    }

    .team-card:nth-child(1) {
        border-color: #CFE4F7;
        background: linear-gradient(145deg, #F4F9FF 0%, #E4F1FC 100%);
    }

    .team-card:nth-child(2) {
        border-color: #CDE8DD;
        background: linear-gradient(145deg, #F4FBF8 0%, #E2F3EB 100%);
    }

    .team-card:nth-child(3) {
        border-color: #DDD0F5;
        background: linear-gradient(145deg, #FAF7FF 0%, #EEE5FC 100%);
    }

    .team-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
    }

    .team-card:nth-child(1)::before {
        background: linear-gradient(90deg, #2E6FA3, #65A7D8);
    }

    .team-card:nth-child(2)::before {
        background: linear-gradient(90deg, #23785D, #61B495);
    }

    .team-card:nth-child(3)::before {
        background: linear-gradient(90deg, #6B46C1, #9C7AE0);
    }

    .team-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 34px rgba(15, 35, 52, 0.13);
    }

    .team-card-icon {
        display: inline-flex;
        width: 52px;
        height: 52px;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.08rem;
        border: 1px solid rgba(255, 255, 255, 0.82);
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.88);
        box-shadow: 0 7px 18px rgba(15, 35, 52, 0.08);
    }

    .team-card:nth-child(1) .team-card-icon {
        color: #245F8E;
    }

    .team-card:nth-child(2) .team-card-icon {
        color: #1F7057;
    }

    .team-card:nth-child(3) .team-card-icon {
        color: #6B46C1;
    }

    .team-card-icon svg {
        width: 24px;
        height: 24px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .team-card-content {
        flex: 1;
    }

    .team-card h3 {
        margin: 0;
        color: var(--navy);
        font-size: 1.18rem;
        line-height: 1.28;
    }

    .team-card-role {
        min-height: 2.7rem;
        margin-top: 0.48rem;
        font-size: 0.82rem;
        font-weight: 760;
        line-height: 1.45;
    }

    .team-card:nth-child(1) .team-card-role {
        color: #245F8E;
    }

    .team-card:nth-child(2) .team-card-role {
        color: #1F7057;
    }

    .team-card:nth-child(3) .team-card-role {
        color: #6B46C1;
    }

    .team-card p {
        margin: 1rem 0 0;
        color: var(--muted);
        font-size: 0.89rem;
        line-height: 1.68;
    }

    .team-section-heading {
        margin: 0 0 1.15rem;
        text-align: left;
    }

    .team-section-heading p {
        margin-left: 0;
        max-width: 820px;
    }

    .team-tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 0.62rem;
        margin-bottom: 2.35rem;
    }

    .team-tech-badge {
        display: inline-flex;
        align-items: center;
        min-height: 36px;
        padding: 0.48rem 0.82rem;
        border: 1px solid #DCE8E6;
        border-radius: 999px;
        background: #F2FAF8;
        color: #146C64;
        font-size: 0.8rem;
        font-weight: 720;
    }

    .team-closing {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 1rem;
        align-items: start;
        margin: 0.1rem 0 1.6rem;
        padding: 1.35rem 1.45rem;
        border: 1px solid #DCEBE8;
        border-radius: var(--radius-md);
        background:
            linear-gradient(
                135deg,
                rgba(234, 248, 246, 0.94),
                rgba(255, 255, 255, 0.95)
            );
    }

    .team-closing-icon {
        display: inline-flex;
        width: 42px;
        height: 42px;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: var(--primary);
        color: #FFFFFF;
        box-shadow: 0 7px 16px rgba(0, 158, 142, 0.20);
    }

    .team-closing-icon svg {
        width: 21px;
        height: 21px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .team-closing strong {
        display: block;
        margin-bottom: 0.3rem;
        color: var(--navy);
        font-size: 0.95rem;
    }

    .team-closing p {
        margin: 0;
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.65;
    }

    .team-academic-info {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        overflow: hidden;
        margin-bottom: 1.7rem;
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        background: var(--surface);
        box-shadow: var(--shadow-sm);
    }

    .team-academic-item {
        min-height: 88px;
        padding: 1rem 1.1rem;
        border-right: 1px solid var(--border);
    }

    .team-academic-item:last-child {
        border-right: 0;
    }

    .team-academic-label {
        margin-bottom: 0.35rem;
        color: #8A94A8;
        font-size: 0.66rem;
        font-weight: 800;
        letter-spacing: 0.10em;
        text-transform: uppercase;
    }

    .team-academic-value {
        color: var(--navy);
        font-size: 0.84rem;
        font-weight: 680;
        line-height: 1.45;
    }

    @media (max-width: 980px) {
        .team-grid {
            grid-template-columns: 1fr;
        }

        .team-card {
            min-height: auto;
        }

        .team-card-role {
            min-height: auto;
        }

        .team-academic-info {
            grid-template-columns: 1fr 1fr;
        }

        .team-academic-item:nth-child(2) {
            border-right: 0;
        }

        .team-academic-item:nth-child(-n + 2) {
            border-bottom: 1px solid var(--border);
        }
    }

    @media (max-width: 620px) {
        .team-academic-info {
            grid-template-columns: 1fr;
        }

        .team-academic-item,
        .team-academic-item:nth-child(2) {
            border-right: 0;
            border-bottom: 1px solid var(--border);
        }

        .team-academic-item:last-child {
            border-bottom: 0;
        }

        .team-closing {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

hero(
    "Equipe do projeto",
    "Conheça as integrantes responsáveis pelo desenvolvimento da solução, da análise dos dados à implementação da aplicação analítica em Streamlit.",
)

st.markdown(
    """
    <section class="team-intro">
        <div class="team-intro-kicker">Desenvolvimento colaborativo</div>
        <h2>Conhecimentos integrados em uma única solução</h2>
        <p>
            O projeto reuniu competências em Ciência de Dados, Machine Learning,
            visualização de dados e desenvolvimento de aplicações analíticas. Cada
            integrante contribuiu em etapas específicas para garantir uma entrega
            consistente e alinhada aos objetivos do Tech Challenge.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

cards = "".join(criar_card_integrante(integrante) for integrante in EQUIPE)
st.markdown(
    f'<section class="team-grid">{cards}</section>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="team-section-heading">
        <div class="team-section-kicker">Stack do projeto</div>
        <h2>Tecnologias utilizadas</h2>
        <p>
            Ferramentas utilizadas na preparação dos dados, modelagem, visualização,
            versionamento e disponibilização da aplicação.
        </p>
    </section>

    <div class="team-tech-stack">
        <span class="team-tech-badge">Python</span>
        <span class="team-tech-badge">Pandas</span>
        <span class="team-tech-badge">Scikit-learn</span>
        <span class="team-tech-badge">Random Forest</span>
        <span class="team-tech-badge">Plotly</span>
        <span class="team-tech-badge">Streamlit</span>
        <span class="team-tech-badge">Joblib</span>
        <span class="team-tech-badge">Git &amp; GitHub</span>
    </div>

    <section class="team-closing">
        <div class="team-closing-icon">
            <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12 3v18"></path>
                <path d="M3 12h18"></path>
                <circle cx="12" cy="12" r="9"></circle>
            </svg>
        </div>
        <div>
            <strong>Uma solução integrada de dados e Machine Learning</strong>
            <p>
                Este projeto demonstra a aplicação prática de técnicas de Ciência de
                Dados e Machine Learning para apoiar a análise relacionada à obesidade,
                reunindo modelagem preditiva, visualização de dados e desenvolvimento
                de aplicações analíticas em um único ambiente.
            </p>
        </div>
    </section>

    <section class="team-academic-info">
        <div class="team-academic-item">
            <div class="team-academic-label">Instituição</div>
            <div class="team-academic-value">FIAP</div>
        </div>
        <div class="team-academic-item">
            <div class="team-academic-label">Formação</div>
            <div class="team-academic-value">Pós-Tech em Data Analytics</div>
        </div>
        <div class="team-academic-item">
            <div class="team-academic-label">Entrega</div>
            <div class="team-academic-value">Tech Challenge — Fase 4</div>
        </div>
        <div class="team-academic-item">
            <div class="team-academic-label">Tema</div>
            <div class="team-academic-value">Machine Learning aplicado à saúde</div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

rodape()