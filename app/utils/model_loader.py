from functools import lru_cache
from pathlib import Path

import joblib


@lru_cache(maxsize=1)
def carregar_modelo():
    """
    Carrega a Pipeline treinada.

    O modelo é carregado apenas uma vez durante a execução
    da aplicação.
    """

    caminho_modelo = (
        Path(__file__).resolve().parents[2]
        / "models"
        / "random_forest_comportamental.joblib"
    )

    return joblib.load(caminho_modelo)