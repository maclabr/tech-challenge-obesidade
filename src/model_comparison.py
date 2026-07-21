"""
Módulo responsável pela comparação padronizada de modelos de Machine Learning.

Este módulo executa diferentes algoritmos sobre os cenários de modelagem
definidos no projeto, consolidando as principais métricas de desempenho.

Responsabilidades
-----------------
- executar experimentos de forma padronizada;
- reutilizar as pipelines definidas em model_training;
- reutilizar a avaliação definida em model_evaluation;
- consolidar os resultados em um DataFrame.

Este módulo não realiza leitura de arquivos, geração de gráficos ou
interpretação dos resultados.
"""

from __future__ import annotations

import time
from typing import Dict

import pandas as pd

from sklearn.base import BaseEstimator

from src.model_evaluation import avaliar_modelo
from src.model_training import criar_pipeline
from src.model_training import dividir_treino_teste


def executar_comparacao(
    cenarios: Dict[str, pd.DataFrame],
    y: pd.Series,
    modelos: Dict[str, BaseEstimator],
) -> pd.DataFrame:
    """
    Executa a comparação entre diferentes algoritmos de Machine Learning.

    Para cada cenário de modelagem informado, todos os algoritmos são
    treinados, avaliados e comparados utilizando a mesma divisão
    treino/teste, garantindo uma comparação justa entre os modelos.

    Parameters
    ----------
    cenarios : Dict[str, pd.DataFrame]
        Dicionário contendo os cenários de modelagem.

    y : pd.Series
        Variável alvo.

    modelos : Dict[str, BaseEstimator]
        Dicionário contendo os algoritmos a serem avaliados.

    Returns
    -------
    pd.DataFrame
        DataFrame contendo os resultados consolidados dos experimentos.
    """

    resultados = []

    for nome_cenario, X in cenarios.items():

        X_train, X_test, y_train, y_test = dividir_treino_teste(
            X,
            y,
        )

        for nome_modelo, estimador in modelos.items():

            pipeline = criar_pipeline(
                X_train,
                estimador,
            )

            inicio_fit = time.perf_counter()

            pipeline.fit(
                X_train,
                y_train,
            )

            fim_fit = time.perf_counter()

            metricas = avaliar_modelo(
                pipeline,
                X_test,
                y_test,
            )

            resultados.append(
                {
                    "cenario": nome_cenario,
                    "modelo": nome_modelo,
                    "accuracy": metricas["accuracy"],
                    "f1_macro": metricas["f1_macro"],
                    "fit_time": fim_fit - inicio_fit,
                }
            )

    return pd.DataFrame(resultados)