"""Estilos e componentes visuais compartilhados pela aplicação."""

import html

import streamlit as st


def aplicar_estilos() -> None:
    """Aplica a identidade visual global utilizada em todas as páginas."""

    st.markdown(
        """
        <style>
        :root {
            --primary: #009E8E;
            --primary-dark: #007E73;
            --primary-soft: #EAF8F6;
            --navy: #0B1538;
            --text: #253252;
            --muted: #66728F;
            --bg: #F7F9FC;
            --surface: #FFFFFF;
            --surface-soft: #F9FBFD;
            --border: #E5EAF1;
            --border-strong: #D7DEE9;
            --info: #1976D2;
            --warning: #E79A18;
            --danger: #C94A4A;
            --shadow-sm: 0 2px 8px rgba(11, 21, 56, 0.05);
            --shadow-md: 0 8px 24px rgba(11, 21, 56, 0.07);
            --radius-sm: 10px;
            --radius-md: 14px;
            --radius-lg: 18px;
        }

        html,
        body,
        [class*="css"] {
            font-family: Inter, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        .stApp {
            background:
                radial-gradient(
                    circle at 48% 0%,
                    rgba(0, 158, 142, 0.035),
                    transparent 28rem
                ),
                var(--bg);
            color: var(--text);
        }

        .block-container {
            max-width: 1440px;
            padding-top: 1.35rem;
            padding-bottom: 3rem;
            padding-left: 1.6rem;
            padding-right: 1.6rem;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        [data-testid="stHeadingWithActionElements"] {
            color: var(--navy);
            letter-spacing: -0.025em;
        }

        h1 {
            font-weight: 760;
        }

        h2 {
            font-weight: 720;
        }

        h3 {
            font-weight: 680;
        }

        p,
        li,
        label,
        .stCaption {
            color: var(--text);
        }

        [data-testid="stCaptionContainer"] p,
        small {
            color: var(--muted);
        }

        hr {
            border-color: var(--border);
        }

        /* Barra superior */

        [data-testid="stHeader"] {
            background: rgba(247, 249, 252, 0.88);
            backdrop-filter: blur(10px);
        }

        [data-testid="stToolbar"] {
            right: 0.75rem;
        }

        /* Sidebar */

        [data-testid="stSidebar"] {
            background: var(--surface);
            border-right: 1px solid var(--border);
            box-shadow: 5px 0 18px rgba(11, 21, 56, 0.025);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 1.15rem;
        }

        [data-testid="stSidebar"] h3 {
            color: var(--navy);
            font-size: 1rem;
            font-weight: 750;
        }

        [data-testid="stSidebarNav"] {
            padding-top: 0.45rem;
        }

        [data-testid="stSidebarNav"] ul {
            gap: 0.28rem;
        }

        [data-testid="stSidebarNav"] a {
            min-height: 2.75rem;
            border-radius: 11px;
            color: var(--text);
            font-weight: 580;
            transition:
                background-color 150ms ease,
                color 150ms ease,
                transform 150ms ease;
        }

        [data-testid="stSidebarNav"] a:hover {
            background: #F0F7F6;
            color: var(--primary-dark);
            transform: translateX(2px);
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: var(--primary-soft);
            color: var(--primary-dark);
            font-weight: 700;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] svg {
            color: var(--primary);
        }

        [data-testid="stSidebar"] [data-testid="stAlert"] {
            box-shadow: none;
        }

        /* Superfícies e cards */

        [data-testid="stMetric"],
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetric"] {
            min-height: 118px;
            padding: 17px 18px;
            transition:
                border-color 160ms ease,
                box-shadow 160ms ease,
                transform 160ms ease;
        }

        [data-testid="stMetric"]:hover {
            border-color: #D6E8E5;
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted);
            font-size: 0.82rem;
            font-weight: 650;
        }

        [data-testid="stMetricValue"] {
            color: var(--navy);
            font-size: 1.65rem;
            font-weight: 760;
            letter-spacing: -0.035em;
        }

        [data-testid="stMetricDelta"] {
            color: var(--primary-dark);
            font-weight: 650;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            overflow: hidden;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] > div {
            padding: 0.15rem;
        }

        /* Hero global */

        .hero {
            position: relative;
            overflow: hidden;
            min-height: 150px;
            padding: 30px 34px;
            margin-bottom: 22px;
            background:
                radial-gradient(
                    circle at 88% 18%,
                    rgba(0, 158, 142, 0.14),
                    transparent 12rem
                ),
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #FBFEFE 58%,
                    #F0FAF8 100%
                );
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-sm);
        }

        .hero::after {
            content: "";
            position: absolute;
            right: 38px;
            top: 30px;
            width: 112px;
            height: 112px;
            border-radius: 50%;
            background:
                radial-gradient(
                    circle,
                    rgba(0, 158, 142, 0.14) 0 2px,
                    transparent 3px
                ) 0 0 / 17px 17px;
            opacity: 0.55;
            pointer-events: none;
        }

        .hero h1 {
            position: relative;
            z-index: 1;
            max-width: 760px;
            margin: 0 0 10px 0;
            color: var(--navy);
            font-size: clamp(2rem, 3vw, 2.55rem);
            line-height: 1.12;
        }

        .hero p {
            position: relative;
            z-index: 1;
            max-width: 780px;
            margin: 0;
            color: var(--text);
            font-size: 1rem;
            line-height: 1.65;
        }

        /* Abas */

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 1.1rem;
            border-bottom: 1px solid var(--border);
        }

        [data-testid="stTabs"] [data-baseweb="tab"] {
            height: 3rem;
            padding: 0 0.15rem;
            color: var(--muted);
            font-weight: 620;
        }

        [data-testid="stTabs"] [aria-selected="true"] {
            color: var(--primary-dark);
        }

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
            background-color: var(--primary);
            height: 2px;
        }

        /* Botões */

        .stButton > button,
        .stFormSubmitButton > button,
        .stDownloadButton > button {
            min-height: 2.8rem;
            border-radius: 10px;
            border: 1px solid var(--border-strong);
            font-weight: 700;
            transition:
                transform 150ms ease,
                box-shadow 150ms ease,
                border-color 150ms ease;
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover,
        .stDownloadButton > button:hover {
            border-color: var(--primary);
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(0, 158, 142, 0.12);
        }

        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            background: linear-gradient(
                90deg,
                var(--primary-dark),
                var(--primary)
            );
            border-color: transparent;
            color: #FFFFFF;
        }

        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            background: linear-gradient(
                90deg,
                #007268,
                #009E8E
            );
            color: #FFFFFF;
        }

        /* Campos de formulário */

        [data-baseweb="input"] > div,
        [data-baseweb="select"] > div,
        [data-baseweb="textarea"] > div {
            border-color: var(--border-strong);
            border-radius: 10px;
            background: var(--surface);
        }

        [data-baseweb="input"] > div:focus-within,
        [data-baseweb="select"] > div:focus-within,
        [data-baseweb="textarea"] > div:focus-within {
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(0, 158, 142, 0.10);
        }

        [data-testid="stNumberInput"] button {
            border-color: var(--border);
            color: var(--primary-dark);
        }

        [data-testid="stCheckbox"] svg,
        [data-testid="stRadio"] svg {
            color: var(--primary);
        }

        /* Alertas */

        [data-testid="stAlert"] {
            border-radius: 12px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow-sm);
        }

        /* Expanders */

        [data-testid="stExpander"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow-sm);
            overflow: hidden;
        }

        [data-testid="stExpander"] summary {
            color: var(--navy);
            font-weight: 650;
        }

        /* Gráficos e tabelas */

        [data-testid="stPlotlyChart"],
        [data-testid="stDataFrame"] {
            overflow: hidden;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        /* Componentes semânticos da aplicação */

        .insight {
            margin: 8px 0;
            padding: 14px 16px;
            background: var(--primary-soft);
            border: 1px solid #D5EFEB;
            border-left: 4px solid var(--primary);
            border-radius: 10px;
            color: var(--text);
        }

        .clinical-note {
            padding: 16px 18px;
            background: #F5F9FD;
            border: 1px solid #DCE9F4;
            border-left: 4px solid var(--info);
            border-radius: 12px;
            color: var(--text);
            line-height: 1.6;
        }

        .risk-low,
        .risk-medium,
        .risk-high {
            padding: 16px 18px;
            border-radius: 12px;
            line-height: 1.55;
        }

        .risk-low {
            background: var(--primary-soft);
            border: 1px solid #D5EFEB;
            border-left: 4px solid var(--primary);
        }

        .risk-medium {
            background: #FFF8EB;
            border: 1px solid #F3E1B9;
            border-left: 4px solid var(--warning);
        }

        .risk-high {
            background: #FFF2F2;
            border: 1px solid #F1D5D5;
            border-left: 4px solid var(--danger);
        }

        .bmi-card {
            display: flex;
            align-items: center;
            gap: 18px;
            width: 100%;
            min-height: 132px;
            margin: 0.45rem 0 1rem 0;
            padding: 20px 22px;
            box-sizing: border-box;
            background: var(--surface);
            border: 1px solid var(--border);
            border-left: 4px solid var(--bmi-accent);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        .bmi-card-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 52px;
            width: 52px;
            height: 52px;
            border-radius: 14px;
            background: var(--bmi-soft);
            color: var(--bmi-accent);
            font-size: 1.55rem;
        }

        .bmi-card-content {
            flex: 1;
            min-width: 0;
        }

        .bmi-card-label {
            margin-bottom: 4px;
            color: var(--muted);
            font-size: 0.78rem;
            font-weight: 750;
            letter-spacing: 0.055em;
            text-transform: uppercase;
        }

        .bmi-card-main {
            display: flex;
            align-items: baseline;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 4px;
        }

        .bmi-card-value {
            color: var(--navy);
            font-size: 2rem;
            font-weight: 780;
            line-height: 1.1;
            letter-spacing: -0.04em;
        }

        .bmi-card-unit {
            color: var(--muted);
            font-size: 0.92rem;
            font-weight: 600;
        }

        .bmi-card-classification {
            color: var(--bmi-accent);
            font-size: 1rem;
            font-weight: 720;
        }

        .bmi-card-note {
            margin-top: 7px;
            color: var(--muted);
            font-size: 0.82rem;
            line-height: 1.45;
        }

        .bmi-low {
            --bmi-accent: #4D7FA3;
            --bmi-soft: #EDF5FA;
        }

        .bmi-adequate {
            --bmi-accent: #009E8E;
            --bmi-soft: #EAF8F6;
        }

        .bmi-overweight {
            --bmi-accent: #C58A1F;
            --bmi-soft: #FFF7E7;
        }

        .bmi-obesity-one {
            --bmi-accent: #C56D32;
            --bmi-soft: #FFF1E8;
        }

        .bmi-obesity-two {
            --bmi-accent: #B95050;
            --bmi-soft: #FCEEEE;
        }

        .bmi-obesity-three {
            --bmi-accent: #934060;
            --bmi-soft: #F8EBF0;
        }

        .footer {
            margin-top: 1.5rem;
            padding-top: 1.35rem;
            border-top: 1px solid var(--border);
            color: var(--muted);
            text-align: center;
            font-size: 0.82rem;
        }

        @media (max-width: 900px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .hero {
                min-height: auto;
                padding: 24px 22px;
            }

            .hero::after {
                display: none;
            }
        }

        @media (max-width: 700px) {
            .block-container {
                padding-top: 0.85rem;
            }

            .hero {
                border-radius: 15px;
            }

            .hero h1 {
                font-size: 1.8rem;
            }

            .hero p {
                font-size: 0.95rem;
            }

            [data-testid="stMetric"] {
                min-height: 102px;
            }

            .bmi-card {
                align-items: flex-start;
                padding: 18px;
            }

            .bmi-card-value {
                font-size: 1.7rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(titulo: str, subtitulo: str) -> None:
    """Exibe o cabeçalho principal da página."""

    titulo_seguro = html.escape(titulo)
    subtitulo_seguro = html.escape(subtitulo)

    st.markdown(
        (
            '<div class="hero">'
            f'<h1>{titulo_seguro}</h1>'
            f'<p>{subtitulo_seguro}</p>'
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def card_imc(
    valor_imc: float,
    classificacao: str,
    classe_visual: str,
) -> None:
    """Exibe o resultado complementar do IMC em um card visual."""

    classificacao_segura = html.escape(classificacao)
    classe_visual_segura = html.escape(classe_visual)

    st.markdown(
        (
            f'<div class="bmi-card {classe_visual_segura}">'
            '<div class="bmi-card-icon" aria-hidden="true">⚖️</div>'
            '<div class="bmi-card-content">'
            '<div class="bmi-card-label">'
            "Índice de Massa Corporal"
            "</div>"
            '<div class="bmi-card-main">'
            f'<span class="bmi-card-value">{valor_imc:.2f}</span>'
            '<span class="bmi-card-unit">kg/m²</span>'
            "</div>"
            '<div class="bmi-card-classification">'
            f"{classificacao_segura}"
            "</div>"
            '<div class="bmi-card-note">'
            "Indicador complementar para adultos. "
            "O IMC não é enviado ao modelo e não substitui "
            "avaliação de um profissional de saúde."
            "</div>"
            "</div>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def placeholder_imc() -> None:
    """Exibe orientação enquanto peso e altura não foram informados."""

    st.info(
        "⚖️ **Preencha peso e altura para visualizar o IMC**\n\n"
        "O resultado será calculado automaticamente e servirá somente "
        "como informação complementar."
    )


def rodape() -> None:
    """Exibe o rodapé padrão da aplicação."""

    st.markdown(
        (
            '<div class="footer">'
            "Tech Challenge FIAP · Aplicação educacional de apoio analítico "
            "— não substitui avaliação clínica."
            "</div>"
        ),
        unsafe_allow_html=True,
    )