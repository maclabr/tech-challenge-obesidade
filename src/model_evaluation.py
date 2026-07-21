"""
Módulo responsável pela avaliação de modelos de Machine Learning.

Este módulo concentra funções reutilizáveis utilizadas durante a etapa
de avaliação de modelos do Tech Challenge.

Responsabilidades
-----------------
- calcular métricas de desempenho de um modelo já treinado sobre um
  conjunto de teste (accuracy, F1-macro, classification_report e matriz
  de confusão).

Este módulo não treina modelos nem decide entre cenários de modelagem.
Essas atividades pertencem aos notebooks de modelagem.
"""

from __future__ import annotations

from typing import Any
from typing import Dict

import pandas as pd

from sklearn.base import BaseEstimator
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)

# =============================================================================
# Avaliação de modelos
# =============================================================================


def avaliar_modelo(
    pipeline: BaseEstimator,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    labels: list[str] | None = None,
) -> Dict[str, Any]:
    """
    Avalia um pipeline/estimador já treinado sobre o conjunto de teste.

    A função é genérica o suficiente para qualquer pipeline ou estimador
    compatível com a API do Scikit-Learn, não sendo específica de nenhum
    algoritmo. Como o problema é de classificação multiclasse, métricas
    além da accuracy são reportadas, conforme definido na metodologia do
    projeto.

    Parameters
    ----------
    pipeline : BaseEstimator
        Pipeline ou estimador já treinado (`fit` realizado previamente),
        compatível com a API do Scikit-Learn (deve implementar `predict`).

    X_test : pd.DataFrame
        Conjunto de atributos preditores de teste.

    y_test : pd.Series
        Variável alvo do conjunto de teste.

    labels : list[str] | None, default=None
        Ordem das classes a ser usada no `classification_report` e na
        matriz de confusão. Se `None`, o scikit-learn utiliza a ordem
        alfabética padrão das classes observadas em `y_test`/`y_pred`.
        Nos notebooks de modelagem, deve-se informar
        `ORDEM_NIVEIS_OBESIDADE` para preservar a ordem clínica dos
        níveis de obesidade (do mais leve ao mais grave) em vez da
        ordem alfabética.

    Returns
    -------
    Dict[str, Any]
        Dicionário contendo:

        - "accuracy": acurácia (float);
        - "f1_macro": F1-score macro (float);
        - "classification_report": relatório de classificação (str),
          com precision, recall e F1 por classe;
        - "matriz_confusao": matriz de confusão (np.ndarray).
    """

    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    f1_macro = f1_score(y_test, y_pred, average="macro")

    relatorio_classificacao = classification_report(y_test, y_pred, labels=labels)

    matriz_confusao = confusion_matrix(y_test, y_pred, labels=labels)

    return {
        "accuracy": accuracy,
        "f1_macro": f1_macro,
        "classification_report": relatorio_classificacao,
        "matriz_confusao": matriz_confusao,
    }
