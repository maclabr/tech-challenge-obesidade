"""Estilos e componentes visuais compartilhados pela aplicação."""

import html

import streamlit as st


def aplicar_estilos() -> None:
    """Aplica os estilos gerais utilizados nas páginas da aplicação."""

    st.markdown(
        """
        <style>
        :root {
            --primary: #176B87;
            --secondary: #2E8B75;
            --bg: #F5F8FA;
            --text: #17324D;
            --muted: #587083;
            --border: #DFE8EE;
            --surface: #FFFFFF;
        }

        .stApp {background: var(--bg);}
        .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1400px;}
        h1, h2, h3 {color: var(--text); letter-spacing: -0.02em;}

        [data-testid="stMetric"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 16px;
            box-shadow: 0 3px 12px rgba(23, 50, 77, 0.06);
        }

        [data-testid="stMetricLabel"] {color: var(--muted);}

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border-radius: 16px;
            box-shadow: 0 3px 12px rgba(23, 50, 77, 0.05);
        }

        .hero {
            background: linear-gradient(120deg, #0F5F78, #238B7A);
            padding: 28px 32px;
            border-radius: 20px;
            color: white;
            margin-bottom: 22px;
        }

        .hero h1 {color: white; margin: 0 0 8px 0; font-size: 2.1rem;}
        .hero p {margin: 0; opacity: 0.93; font-size: 1.02rem; line-height: 1.55;}

        .insight {
            background: #ECF7F4;
            border-left: 5px solid #2E8B75;
            padding: 14px 16px;
            border-radius: 10px;
            margin: 8px 0;
        }

        .clinical-note {
            background: #EEF6FB;
            border: 1px solid #CFE3EF;
            padding: 16px;
            border-radius: 12px;
        }

        .risk-low {background: #ECF7F4; border-left: 5px solid #2E8B75; padding: 16px; border-radius: 12px;}
        .risk-medium {background: #FFF7E7; border-left: 5px solid #E3A72F; padding: 16px; border-radius: 12px;}
        .risk-high {background: #FDEEEE; border-left: 5px solid #C94A4A; padding: 16px; border-radius: 12px;}

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
            border-left: 5px solid var(--bmi-accent);
            border-radius: 16px;
            box-shadow: 0 4px 16px rgba(23, 50, 77, 0.06);
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

        .bmi-card-content {flex: 1; min-width: 0;}
        .bmi-card-label {margin-bottom: 4px; color: var(--muted); font-size: 0.82rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase;}
        .bmi-card-main {display: flex; align-items: baseline; flex-wrap: wrap; gap: 8px; margin-bottom: 4px;}
        .bmi-card-value {color: var(--text); font-size: 2rem; font-weight: 750; line-height: 1.1; letter-spacing: -0.04em;}
        .bmi-card-unit {color: var(--muted); font-size: 0.92rem; font-weight: 600;}
        .bmi-card-classification {color: var(--bmi-accent); font-size: 1rem; font-weight: 700;}
        .bmi-card-note {margin-top: 7px; color: var(--muted); font-size: 0.82rem; line-height: 1.45;}

        .bmi-low {--bmi-accent: #4D7FA3; --bmi-soft: #EDF5FA;}
        .bmi-adequate {--bmi-accent: #2E8B75; --bmi-soft: #ECF7F4;}
        .bmi-overweight {--bmi-accent: #C58A1F; --bmi-soft: #FFF7E7;}
        .bmi-obesity-one {--bmi-accent: #C56D32; --bmi-soft: #FFF1E8;}
        .bmi-obesity-two {--bmi-accent: #B95050; --bmi-soft: #FCEEEE;}
        .bmi-obesity-three {--bmi-accent: #934060; --bmi-soft: #F8EBF0;}

        .footer {text-align: center; color: #718597; font-size: 0.85rem; padding-top: 24px;}

        @media (max-width: 700px) {
            .block-container {padding-top: 1rem;}
            .hero {padding: 22px 20px; border-radius: 16px;}
            .hero h1 {font-size: 1.7rem;}
            .bmi-card {align-items: flex-start; padding: 18px;}
            .bmi-card-value {font-size: 1.7rem;}
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
            '</div>'
        ),
        unsafe_allow_html=True,
    )


def card_imc(valor_imc: float, classificacao: str, classe_visual: str) -> None:
    """Exibe o resultado complementar do IMC em um card visual."""

    classificacao_segura = html.escape(classificacao)
    classe_visual_segura = html.escape(classe_visual)

    st.markdown(
        (
            f'<div class="bmi-card {classe_visual_segura}">'
            '<div class="bmi-card-icon" aria-hidden="true">⚖️</div>'
            '<div class="bmi-card-content">'
            '<div class="bmi-card-label">Índice de Massa Corporal</div>'
            '<div class="bmi-card-main">'
            f'<span class="bmi-card-value">{valor_imc:.2f}</span>'
            '<span class="bmi-card-unit">kg/m²</span>'
            '</div>'
            f'<div class="bmi-card-classification">{classificacao_segura}</div>'
            '<div class="bmi-card-note">'
            'Indicador complementar para adultos. O IMC não é enviado ao modelo '
            'e não substitui avaliação de um profissional de saúde.'
            '</div>'
            '</div>'
            '</div>'
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
            'Tech Challenge FIAP · Aplicação educacional de apoio analítico '
            '— não substitui avaliação clínica.'
            '</div>'
        ),
        unsafe_allow_html=True,
    )