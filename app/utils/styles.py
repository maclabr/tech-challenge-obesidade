"""Estilos e componentes visuais compartilhados pela aplicação."""
import streamlit as st


def aplicar_estilos() -> None:
    st.markdown(
        """
        <style>
        :root {--primary:#176B87;--secondary:#2E8B75;--bg:#F5F8FA;--text:#17324D;}
        .stApp {background: var(--bg);}
        .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1400px;}
        h1,h2,h3 {color: var(--text); letter-spacing:-0.02em;}
        [data-testid="stMetric"] {background:white;border:1px solid #DFE8EE;border-radius:16px;padding:16px;box-shadow:0 3px 12px rgba(23,50,77,.06);}
        [data-testid="stMetricLabel"] {color:#587083;}
        div[data-testid="stVerticalBlockBorderWrapper"] {background:white;border-radius:16px;box-shadow:0 3px 12px rgba(23,50,77,.05);}
        .hero {background:linear-gradient(120deg,#0F5F78,#238B7A);padding:28px 32px;border-radius:20px;color:white;margin-bottom:22px;}
        .hero h1 {color:white;margin:0 0 8px 0;font-size:2.1rem;}
        .hero p {margin:0;opacity:.93;font-size:1.02rem;line-height:1.55;}
        .insight {background:#ECF7F4;border-left:5px solid #2E8B75;padding:14px 16px;border-radius:10px;margin:8px 0;}
        .clinical-note {background:#EEF6FB;border:1px solid #CFE3EF;padding:16px;border-radius:12px;}
        .risk-low {background:#ECF7F4;border-left:5px solid #2E8B75;padding:16px;border-radius:12px;}
        .risk-medium {background:#FFF7E7;border-left:5px solid #E3A72F;padding:16px;border-radius:12px;}
        .risk-high {background:#FDEEEE;border-left:5px solid #C94A4A;padding:16px;border-radius:12px;}
        .footer {text-align:center;color:#718597;font-size:.85rem;padding-top:24px;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(titulo: str, subtitulo: str) -> None:
    st.markdown(
        f'<div class="hero"><h1>{titulo}</h1><p>{subtitulo}</p></div>',
        unsafe_allow_html=True,
    )


def rodape() -> None:
    st.markdown(
        '<div class="footer">Tech Challenge FIAP · Aplicação educacional de apoio analítico — não substitui avaliação clínica.</div>',
        unsafe_allow_html=True,
    )