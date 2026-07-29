"""Página inicial da aplicação Obesity Care Analytics."""

import base64
import re
from pathlib import Path
from textwrap import dedent

import streamlit as st

from utils.model_loader import carregar_modelo
from utils.styles import aplicar_estilos, rodape


st.set_page_config(
    page_title="Obesity Care Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

aplicar_estilos()


def renderizar_html(conteudo: str) -> None:
    """Renderiza HTML sem interferência da formatação Markdown."""

    html_limpo = " ".join(
        linha.strip()
        for linha in dedent(conteudo).splitlines()
        if linha.strip()
    )

    html_limpo = re.sub(r">\s+<", "><", html_limpo)

    st.markdown(
        html_limpo,
        unsafe_allow_html=True,
    )


def carregar_imagem_base64(caminho: Path) -> str:
    """Converte uma imagem local para exibição segura dentro do HTML."""

    if not caminho.exists():
        raise FileNotFoundError(
            f"Imagem não encontrada: {caminho}"
        )

    extensao = caminho.suffix.lower().replace(".", "")
    tipo_mime = "jpeg" if extensao in {"jpg", "jpeg"} else extensao

    imagem_codificada = base64.b64encode(
        caminho.read_bytes()
    ).decode("utf-8")

    return f"data:image/{tipo_mime};base64,{imagem_codificada}"


CAMINHO_IMAGEM_HERO = (
    Path(__file__).resolve().parent
    / "assets"
    / "hero_obesity_analytics.png"
)

IMAGEM_HERO_BASE64 = carregar_imagem_base64(
    CAMINHO_IMAGEM_HERO
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    renderizar_html(
        """
        <div class="sidebar-brand">
            <div class="sidebar-brand-icon" aria-hidden="true">
                <svg
                    viewBox="0 0 24 24"
                    width="23"
                    height="23"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M12 4V20M4 12H20"
                        stroke="currentColor"
                        stroke-width="3"
                        stroke-linecap="round"
                    />
                </svg>
            </div>

            <div>
                <div class="sidebar-brand-name">
                    Obesity Care
                </div>

                <div class="sidebar-brand-subtitle">
                    Analytics & Machine Learning
                </div>
            </div>
        </div>
        """
    )

    st.divider()

    st.info(
        "Navegue pelas páginas para explorar os dados, realizar uma "
        "predição e consultar o desempenho do modelo."
    )


# =========================================================
# HERO PRINCIPAL
# =========================================================

renderizar_html(
    f"""
    <section class="home-hero">
        <div class="home-hero-content">

            <div class="home-eyebrow">
                <span class="home-eyebrow-dot"></span>
                Plataforma analítica em saúde
            </div>

            <h1>
                Obesity Care Analytics
            </h1>

            <p>
                Plataforma analítica para apoiar ações preventivas e a priorização do cuidado relacionado à obesidade.
            </p>

            <div class="home-hero-tags">

                <span>
                    <svg
                        viewBox="0 0 24 24"
                        width="17"
                        height="17"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M5 19V12M12 19V5M19 19V9"
                            stroke="currentColor"
                            stroke-width="2.2"
                            stroke-linecap="round"
                        />
                    </svg>
                    Dashboard executivo
                </span>

                <span>
                    <svg
                        viewBox="0 0 24 24"
                        width="17"
                        height="17"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M7 4V9C7 12 9 14 12 14C15 14 17 12 17 9V4"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                        />
                        <path
                            d="M12 14V18C12 20 13.5 21 15 21"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                        />
                        <circle
                            cx="18"
                            cy="20"
                            r="2"
                            stroke="currentColor"
                            stroke-width="2"
                        />
                    </svg>
                    Predição individual
                </span>

                <span>
                    <svg
                        viewBox="0 0 24 24"
                        width="17"
                        height="17"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M8 8C5.8 8 4 9.8 4 12C4 14.2 5.8 16 8 16"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                        />
                        <path
                            d="M16 8C18.2 8 20 9.8 20 12C20 14.2 18.2 16 16 16"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                        />
                        <path
                            d="M9 5V19M15 5V19M9 9H15M9 15H15"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                        />
                    </svg>
                    Modelo interpretável
                </span>

            </div>
        </div>

        <div class="home-hero-visual">
            <div class="hero-health-image-frame">
                <img
                    class="hero-health-image"
                    src="{IMAGEM_HERO_BASE64}"
                    alt="Ilustração de análise de dados sobre obesidade com painel, IMC, gráfico, balança, fita métrica, garrafa de água, maçã e tênis."
                />
            </div>
        </div>
    </section>
    """
)


# =========================================================
# TÍTULO DOS RECURSOS
# =========================================================

renderizar_html(
    """
    <div class="section-heading home-resources-heading">
        <div>
            <span class="section-kicker">
                Principais recursos
            </span>

            <h2>
                Uma visão completa do projeto
            </h2>

            <p>
                Navegue pelas áreas da aplicação utilizando o menu lateral.
            </p>
        </div>
    </div>
    """
)


# =========================================================
# CARDS DOS RECURSOS
# =========================================================

col1, col2, col3 = st.columns(3, gap="medium")


with col1:
    renderizar_html(
        """
        <article class="project-card project-card-dashboard">
            <div class="project-card-icon">
                <svg
                    viewBox="0 0 24 24"
                    width="31"
                    height="31"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M5 19V12M12 19V5M19 19V9"
                        stroke="currentColor"
                        stroke-width="2.1"
                        stroke-linecap="round"
                    />

                    <path
                        d="M3 20H21"
                        stroke="currentColor"
                        stroke-width="1.7"
                        stroke-linecap="round"
                    />
                </svg>
            </div>

            <div class="project-card-content">
                <h3>Dashboard</h3>

                <p>
                    Explore padrões, hábitos e características dos pacientes.
                </p>

                <div class="project-card-link">
                    Explorar
                    <span>→</span>
                </div>
            </div>
        </article>
        """
    )


with col2:
    renderizar_html(
        """
        <article class="project-card project-card-prediction">
            <div class="project-card-icon">
                <svg
                    viewBox="0 0 28 28"
                    width="31"
                    height="31"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M8 5V10C8 13.5 10.5 16 14 16C17.5 16 20 13.5 20 10V5"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                    />

                    <path
                        d="M14 16V20C14 22.2 15.8 24 18 24"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                    />

                    <circle
                        cx="21"
                        cy="23"
                        r="2.2"
                        stroke="currentColor"
                        stroke-width="2"
                    />

                    <path
                        d="M6 5H10M18 5H22"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                    />
                </svg>
            </div>

            <div class="project-card-content">
                <h3>Predição</h3>

                <p>
                    Estime o nível de obesidade a partir de dados comportamentais.
                </p>

                <div class="project-card-link">
                    Iniciar predição
                    <span>→</span>
                </div>
            </div>
        </article>
        """
    )


with col3:
    renderizar_html(
        """
        <article class="project-card project-card-model">
            <div class="project-card-icon">
                <svg
                    viewBox="0 0 24 24"
                    width="32"
                    height="32"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M9 4C6.8 4 5 5.8 5 8C3.2 8.5 2 10.1 2 12C2 14 3.3 15.7 5.2 16.2C5.1 18.3 6.8 20 9 20"
                        stroke="currentColor"
                        stroke-width="1.9"
                        stroke-linecap="round"
                    />

                    <path
                        d="M15 4C17.2 4 19 5.8 19 8C20.8 8.5 22 10.1 22 12C22 14 20.7 15.7 18.8 16.2C18.9 18.3 17.2 20 15 20"
                        stroke="currentColor"
                        stroke-width="1.9"
                        stroke-linecap="round"
                    />

                    <path
                        d="M9 4V20M15 4V20M9 9H12M12 9V6M12 15H15M12 15V18"
                        stroke="currentColor"
                        stroke-width="1.9"
                        stroke-linecap="round"
                    />
                </svg>
            </div>

            <div class="project-card-content">
                <h3>Modelo</h3>

                <p>
                    Veja desempenho, metodologia e fatores relevantes do Random Forest.
                </p>

                <div class="project-card-link">
                    Ver detalhes
                    <span>→</span>
                </div>
            </div>
        </article>
        """
    )


renderizar_html(
    """
    <div class="home-section-spacer"></div>
    """
)


# =========================================================
# STATUS E USO RESPONSÁVEL
# =========================================================

status_col, responsible_col = st.columns(
    [1.05, 1.95],
    gap="medium",
)


with status_col:
    try:
        carregar_modelo()

        renderizar_html(
            """
            <section class="system-status-card">
                <div class="system-status-illustration">
                    <div class="system-status-shield">
                        <svg
                            viewBox="0 0 24 24"
                            width="28"
                            height="28"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                d="M12 3L19 6V11C19 15.5 16.1 19.2 12 21C7.9 19.2 5 15.5 5 11V6L12 3Z"
                                stroke="currentColor"
                                stroke-width="1.8"
                                stroke-linejoin="round"
                            />

                            <path
                                d="M9 12L11 14L15.5 9.5"
                                stroke="currentColor"
                                stroke-width="1.8"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                            />
                        </svg>
                    </div>
                </div>

                <div class="system-status-content">
                    <div class="system-status-top">
                        <span class="system-status-label">
                            Status do sistema
                        </span>

                        <span class="system-status-indicator"></span>
                    </div>

                    <h3>Modelo disponível</h3>

                    <p>
                        O pipeline de Machine Learning foi carregado e está
                        pronto para realizar predições.
                    </p>
                </div>
            </section>
            """
        )

    except Exception as erro:
        st.error(
            f"Não foi possível carregar o modelo: {erro}"
        )


with responsible_col:
    renderizar_html(
        """
        <section class="responsible-use-card">
            <div class="responsible-use-icon">
                <svg
                    viewBox="0 0 24 24"
                    width="28"
                    height="28"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M12 3L19 6V11C19 15.5 16.1 19.2 12 21C7.9 19.2 5 15.5 5 11V6L12 3Z"
                        stroke="currentColor"
                        stroke-width="1.8"
                        stroke-linejoin="round"
                    />

                    <path
                        d="M9 12L11 14L15.5 9.5"
                        stroke="currentColor"
                        stroke-width="1.8"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />
                </svg>
            </div>

            <div class="responsible-use-content">
                <span class="section-kicker">
                    Uso responsável
                </span>

                <h3>
                    Apoio analítico, não diagnóstico clínico
                </h3>

                <p>
                    A classificação apresentada é uma estimativa estatística
                    de finalidade educacional e analítica. Ela não constitui
                    diagnóstico, não prescreve condutas e deve ser
                    interpretada em conjunto com uma avaliação realizada por
                    profissional de saúde.
                </p>
            </div>
        </section>
        """
    )


rodape()