"""
Módulo responsável pela comparação padronizada de modelos de Machine Learning.

Este módulo executa diferentes algoritmos sobre os cenários de modelagem
definidos no projeto, consolidando as principais métricas de desempenho.

Responsabilidades
-----------------
- executar experimentos de forma padronizada, para todas as combinações
  de cenário x algoritmo informadas;
- reutilizar as pipelines definidas em model_training;
- reutilizar a avaliação definida em model_evaluation, preservando a
  ordem clínica das classes (ORDEM_NIVEIS_OBESIDADE);
- validar cada combinação cenário/modelo com validação cruzada
  estratificada (accuracy e F1-macro, média e desvio-padrão), estimativa
  que deve ser usada para escolher o melhor modelo;
- avaliar também no conjunto de teste, como informação complementar —
  nunca como critério de seleção do melhor modelo, para não arriscar
  overfitting via comparação repetida sobre o mesmo conjunto de teste;
- preservar, por cenário/modelo, a pipeline treinada e o diagnóstico
  completo de teste (classification_report e matriz de confusão), para
  que o notebook possa inspecionar qualquer candidato sem re-treinar nada;
- garantir que todos os cenários comparados compartilham exatamente a
  mesma divisão de linhas em treino/teste, para que a comparação entre
  eles seja justa;
- consolidar os resultados resumidos em um DataFrame.

Este módulo não realiza leitura de arquivos, geração de gráficos ou
interpretação dos resultados.
"""

from __future__ import annotations

import time
from typing import Any
from typing import Dict
from typing import Tuple

import pandas as pd

from sklearn.base import BaseEstimator
from sklearn.base import clone
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate

from src.model_evaluation import avaliar_modelo
from src.model_training import N_SPLITS_CV
from src.model_training import ORDEM_NIVEIS_OBESIDADE
from src.model_training import RANDOM_STATE
from src.model_training import criar_pipeline
from src.model_training import dividir_treino_teste

METRICAS_CV = ["accuracy", "f1_macro"]


def executar_comparacao(
    cenarios: Dict[str, pd.DataFrame],
    y: pd.Series,
    modelos: Dict[str, BaseEstimator],
    n_splits_cv: int = N_SPLITS_CV,
) -> Tuple[pd.DataFrame, Dict[Tuple[str, str], Dict[str, Any]]]:
    """
    Executa a comparação entre diferentes algoritmos de Machine Learning.

    Para cada cenário de modelagem informado, todos os algoritmos são
    treinados e avaliados de duas formas complementares:

    1. Validação cruzada estratificada (`StratifiedKFold`, `n_splits_cv`
       folds) sobre `X_train`/`y_train`, reportando média e desvio-padrão
       de accuracy e F1-macro. **É esta a estimativa que deve ser usada
       para escolher o melhor modelo**, por ser calculada sobre múltiplos
       folds de dados não vistos durante o próprio treino.
    2. Treino final em `X_train`/`y_train` e avaliação em `X_test`/`y_test`
       (via `avaliar_modelo`, com `labels=ORDEM_NIVEIS_OBESIDADE`). Essas
       métricas de teste são retornadas apenas como informação
       complementar — **nunca devem ser usadas como critério de seleção**,
       já que decidir o melhor modelo a partir do desempenho no mesmo
       conjunto de teste, repetidamente, arrisca overfitting à amostra de
       teste.

    Como os cenários compartilham o mesmo `y`, a função valida
    explicitamente (via `assert`) que todos os cenários informados caem
    exatamente na mesma divisão de treino/teste, garantindo que a
    comparação entre eles seja justa.

    Parameters
    ----------
    cenarios : Dict[str, pd.DataFrame]
        Dicionário contendo os cenários de modelagem.

    y : pd.Series
        Variável alvo.

    modelos : Dict[str, BaseEstimator]
        Dicionário contendo os algoritmos a serem avaliados.

    n_splits_cv : int, default=5
        Número de folds utilizados na validação cruzada estratificada.

    Returns
    -------
    Tuple[pd.DataFrame, Dict[Tuple[str, str], Dict[str, Any]]]
        Tupla contendo:

        - um DataFrame resumo, com uma linha por combinação
          cenário/modelo e as colunas: "cenario", "modelo",
          "accuracy_cv_media", "accuracy_cv_desvio", "f1_macro_cv_media",
          "f1_macro_cv_desvio", "accuracy_teste", "f1_macro_teste" e
          "fit_time";
        - um dicionário indexado por `(nome_cenario, nome_modelo)`,
          contendo:

          - "pipeline": a pipeline já treinada em `X_train`/`y_train`;
          - "avaliacao_teste": o dicionário completo retornado por
            `avaliar_modelo` (accuracy, f1_macro, classification_report
            e matriz_confusao), permitindo inspecionar qualquer
            candidato sem re-treinar nada.

    Raises
    ------
    AssertionError
        Caso os cenários informados não compartilhem exatamente a mesma
        divisão de linhas em treino/teste.
    """

    splits = {
        nome_cenario: dividir_treino_teste(X_cenario, y)
        for nome_cenario, X_cenario in cenarios.items()
    }

    nomes_cenarios = list(splits.keys())
    _, X_test_referencia, _, y_test_referencia = splits[nomes_cenarios[0]]

    for nome_cenario in nomes_cenarios[1:]:
        _, X_test_cenario, _, y_test_cenario = splits[nome_cenario]

        assert X_test_referencia.index.equals(X_test_cenario.index), (
            f"Os índices de teste do cenário '{nome_cenario}' divergem do "
            f"cenário '{nomes_cenarios[0]}' — a comparação entre os "
            "cenários não seria justa."
        )
        assert y_test_referencia.index.equals(y_test_cenario.index), (
            f"Os índices de teste do cenário '{nome_cenario}' divergem do "
            f"cenário '{nomes_cenarios[0]}' — a comparação entre os "
            "cenários não seria justa."
        )

    validacao_cruzada = StratifiedKFold(
        n_splits=n_splits_cv,
        shuffle=True,
        random_state=RANDOM_STATE,
    )

    resumo = []
    detalhes: Dict[Tuple[str, str], Dict[str, Any]] = {}

    for nome_cenario, (X_train, X_test, y_train, y_test) in splits.items():

        for nome_modelo, estimador in modelos.items():

            # A validação cruzada é a base para escolher o melhor modelo:
            # é calculada inteiramente sobre X_train/y_train, nunca
            # utilizando o conjunto de teste.
            pipeline_cv = criar_pipeline(X_train, clone(estimador))

            scores_cv = cross_validate(
                pipeline_cv,
                X_train,
                y_train,
                cv=validacao_cruzada,
                scoring=METRICAS_CV,
            )

            pipeline_final = criar_pipeline(X_train, clone(estimador))

            inicio_fit = time.perf_counter()

            pipeline_final.fit(X_train, y_train)

            fim_fit = time.perf_counter()

            # Avaliação no teste: apenas informação complementar, não
            # deve ser usada para escolher o melhor modelo.
            avaliacao_teste = avaliar_modelo(
                pipeline_final,
                X_test,
                y_test,
                labels=ORDEM_NIVEIS_OBESIDADE,
            )

            resumo.append(
                {
                    "cenario": nome_cenario,
                    "modelo": nome_modelo,
                    "accuracy_cv_media": scores_cv["test_accuracy"].mean(),
                    "accuracy_cv_desvio": scores_cv["test_accuracy"].std(),
                    "f1_macro_cv_media": scores_cv["test_f1_macro"].mean(),
                    "f1_macro_cv_desvio": scores_cv["test_f1_macro"].std(),
                    "accuracy_teste": avaliacao_teste["accuracy"],
                    "f1_macro_teste": avaliacao_teste["f1_macro"],
                    "fit_time": fim_fit - inicio_fit,
                }
            )

            detalhes[(nome_cenario, nome_modelo)] = {
                "pipeline": pipeline_final,
                "avaliacao_teste": avaliacao_teste,
            }

    return pd.DataFrame(resumo), detalhes
