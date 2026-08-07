"""Carregamento centralizado da pipeline de Machine Learning."""
from pathlib import Path
import joblib
import streamlit as st

CAMINHO_MODELO = Path(__file__).resolve().parents[2] / "models" / "random_forest_comportamental_calibrado.joblib"

@st.cache_resource(show_spinner=False)
def carregar_modelo():
    if not CAMINHO_MODELO.exists():
        raise FileNotFoundError(f"Modelo não encontrado em: {CAMINHO_MODELO}")
    return joblib.load(CAMINHO_MODELO)


def obter_pipelines_base(modelo=None) -> list:
    """Retorna o(s) Pipeline(s) internos (preprocessador + modelo de árvore).

    Funciona tanto para uma Pipeline simples (retorna lista com 1 item)
    quanto para um CalibratedClassifierCV (retorna 1 Pipeline por fold de
    validação cruzada interna, já que cada fold treina sua própria cópia
    do estimador base). Centraliza essa distinção para que páginas de
    inspeção/explicabilidade não precisem conhecer o tipo exato do objeto
    retornado por carregar_modelo().
    """

    if modelo is None:
        modelo = carregar_modelo()

    if hasattr(modelo, "named_steps"):
        return [modelo]

    if hasattr(modelo, "calibrated_classifiers_"):
        return [
            classificador_calibrado.estimator
            for classificador_calibrado in modelo.calibrated_classifiers_
        ]

    raise TypeError(
        f"Tipo de modelo não suportado para inspeção: {type(modelo)!r}"
    )