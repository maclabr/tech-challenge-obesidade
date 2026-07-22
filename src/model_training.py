"""
Módulo responsável pela preparação dos dados para Machine Learning.

Este módulo concentra funções reutilizáveis utilizadas durante a etapa
de modelagem do Tech Challenge.

Responsabilidades
-----------------
- carregar a camada Silver;
- separar atributos e variável alvo;
- criar os cenários de modelagem;
- dividir dados em treino e teste;
- identificar automaticamente os grupos de variáveis;
- construir o pré-processador;
- construir pipelines de Machine Learning;
- centralizar as constantes de configuração compartilhadas do projeto
  (RANDOM_STATE, TEST_SIZE, TARGET, ORDEM_NIVEIS_OBESIDADE, N_SPLITS_CV,
  META_ACCURACY) — decisão deliberada de manter tudo em um único lugar
  em vez de fragmentar a configuração em múltiplos módulos.

Este módulo não executa experimentos nem compara algoritmos.
Essas atividades pertencem aos notebooks de modelagem.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict
from typing import List
from typing import Tuple

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
)

# =============================================================================
# Configurações gerais
# =============================================================================

RANDOM_STATE = 42

TEST_SIZE = 0.2

TARGET = "ds_nivel_obesidade"

ORDEM_NIVEIS_OBESIDADE = [
    "Insufficient_Weight",
    "Normal_Weight",
    "Overweight_Level_I",
    "Overweight_Level_II",
    "Obesity_Type_I",
    "Obesity_Type_II",
    "Obesity_Type_III",
]

N_SPLITS_CV = 5

META_ACCURACY = 0.75

# =============================================================================
# Caminhos do projeto
# =============================================================================

CAMINHO_ARQUIVO_SILVER = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "silver"
    / "obesity_tratado.csv"
)

# =============================================================================
# Cenários de modelagem
# =============================================================================

COLUNAS_EXCLUIR_MODELO_COMPORTAMENTAL = [
    "nr_altura",
    "nr_peso",
    "nr_imc",
]


def criar_cenarios_modelagem(
    X: pd.DataFrame,
) -> Dict[str, pd.DataFrame]:
    """
    Cria os cenários de modelagem utilizados no Tech Challenge.

    Como o rótulo do dataset é originalmente derivado de fórmulas de IMC
    (peso/altura²), as variáveis Height e Weight quase determinam o
    target sozinhas. Para permitir uma leitura honesta da capacidade
    preditiva dos hábitos alimentares e de atividade física, dois
    cenários são avaliados:

    - "referencia": utiliza todos os atributos disponíveis, incluindo
      altura, peso e IMC;
    - "comportamental": remove as colunas listadas em
      ``COLUNAS_EXCLUIR_MODELO_COMPORTAMENTAL``, restando apenas
      hábitos e dados comportamentais.

    Parameters
    ----------
    X : pd.DataFrame
        Conjunto de atributos preditores.

    Returns
    -------
    Dict[str, pd.DataFrame]
        Dicionário contendo os dois cenários de modelagem:

        - "referencia": X completo;
        - "comportamental": X sem as colunas antropométricas.

    Raises
    ------
    ValueError
        Caso alguma coluna de ``COLUNAS_EXCLUIR_MODELO_COMPORTAMENTAL``
        não exista em X.
    """

    colunas_ausentes = [
        coluna
        for coluna in COLUNAS_EXCLUIR_MODELO_COMPORTAMENTAL
        if coluna not in X.columns
    ]

    if colunas_ausentes:
        raise ValueError(
            "As seguintes colunas não foram encontradas em X: "
            f"{colunas_ausentes}"
        )

    referencia = X.copy()

    comportamental = X.drop(
        columns=COLUNAS_EXCLUIR_MODELO_COMPORTAMENTAL
    ).copy()

    return {
        "referencia": referencia,
        "comportamental": comportamental,
    }


# =============================================================================
# Variáveis ordinais
# =============================================================================

COLUNAS_ORDINAIS = [
    "cd_consumo_de_vegetais",
    "cd_numero_refeicoes_principais",
    "cd_consumo_agua",
    "cd_frequencia_atividade_fisica",
    "cd_tempo_uso_eletronicos",
]

# =============================================================================
# Leitura dos dados
# =============================================================================


def carregar_dados_silver() -> pd.DataFrame:
    """
    Carrega a camada Silver do projeto.

    A camada Silver contém os dados já tratados, validados e enriquecidos
    durante a etapa de Engenharia de Dados, estando pronta para utilização
    na modelagem de Machine Learning.

    Returns
    -------
    pd.DataFrame
        DataFrame contendo a camada Silver.

    Raises
    ------
    FileNotFoundError
        Caso o arquivo da camada Silver não seja encontrado.
    """

    if not CAMINHO_ARQUIVO_SILVER.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {CAMINHO_ARQUIVO_SILVER}"
        )

    return pd.read_csv(CAMINHO_ARQUIVO_SILVER)


# =============================================================================
# Preparação dos dados
# =============================================================================


def separar_features_target(
    dados: pd.DataFrame,
    target: str = TARGET,
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Separa os atributos preditores da variável alvo.

    Esta função centraliza a definição da variável alvo do projeto,
    evitando que notebooks e outros módulos realizem essa separação
    manualmente.

    Parameters
    ----------
    dados : pd.DataFrame
        Base de dados utilizada na etapa de modelagem.

    target : str, default=TARGET
        Nome da variável alvo.

    Returns
    -------
    Tuple[pd.DataFrame, pd.Series]
        Tupla contendo:

        - X: atributos preditores;
        - y: variável alvo.

    Raises
    ------
    KeyError
        Caso a variável alvo não exista no DataFrame.
    """

    if target not in dados.columns:
        raise KeyError(
            f"A variável alvo '{target}' não foi encontrada na base de dados."
        )

    X = dados.drop(columns=[target]).copy()

    y = dados[target].copy()

    return X, y


def dividir_treino_teste(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> Tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.Series,
    pd.Series,
]:
    """
    Divide os dados em conjuntos de treino e teste.

    A divisão é realizada utilizando a estratégia Hold-out
    estratificada, preservando a distribuição das classes da
    variável alvo em ambos os conjuntos.

    Parameters
    ----------
    X : pd.DataFrame
        Conjunto de atributos preditores.

    y : pd.Series
        Variável alvo.

    test_size : float, default=TEST_SIZE
        Proporção destinada ao conjunto de teste.

    random_state : int, default=RANDOM_STATE
        Semente utilizada para garantir a reprodutibilidade.

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]
        Tupla contendo:

        - X_train
        - X_test
        - y_train
        - y_test

    Raises
    ------
    ValueError
        Caso o parâmetro ``test_size`` esteja fora do intervalo (0, 1).
    """

    if not 0 < test_size < 1:
        raise ValueError(
            "O parâmetro 'test_size' deve estar entre 0 e 1."
        )

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

# =============================================================================
# Pré-processamento
# =============================================================================


def obter_grupos_variaveis(
    X: pd.DataFrame,
) -> Dict[str, List[str]]:
    """
    Identifica os grupos de variáveis utilizados no pré-processamento.

    As variáveis são classificadas em três grupos:

    - numéricas contínuas;
    - categóricas ordinais;
    - categóricas nominais.

    Parameters
    ----------
    X : pd.DataFrame
        Conjunto de atributos preditores.

    Returns
    -------
    Dict[str, List[str]]
        Dicionário contendo os grupos de variáveis.
    """

    colunas_numericas = [
        coluna
        for coluna in X.select_dtypes(include="number").columns
        if coluna not in COLUNAS_ORDINAIS
    ]

    colunas_ordinais = [
        coluna
        for coluna in COLUNAS_ORDINAIS
        if coluna in X.columns
    ]

    colunas_categoricas = list(
        X.select_dtypes(include="object").columns
    )

    return {
        "numericas": colunas_numericas,
        "ordinais": colunas_ordinais,
        "categoricas": colunas_categoricas,
    }


def criar_preprocessador(
    X: pd.DataFrame,
) -> ColumnTransformer:
    """
    Constrói o pré-processador utilizado na etapa de Machine Learning.

    O pré-processador aplica transformações específicas conforme o tipo
    de variável:

    - variáveis numéricas contínuas recebem padronização;
    - variáveis ordinais são mantidas sem transformação;
    - variáveis categóricas nominais recebem One-Hot Encoding.

    Parameters
    ----------
    X : pd.DataFrame
        Conjunto de atributos preditores.

    Returns
    -------
    ColumnTransformer
        Objeto configurado para utilização nas pipelines de Machine
        Learning.
    """

    grupos = obter_grupos_variaveis(X)

    preprocessador = ColumnTransformer(
        transformers=[
            (
                "numericas",
                StandardScaler(),
                grupos["numericas"],
            ),
            (
                "ordinais",
                "passthrough",
                grupos["ordinais"],
            ),
            (
                "categoricas",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False,
                ),
                grupos["categoricas"],
            ),
        ],
        remainder="drop",
    )

    return preprocessador


def criar_pipeline(
    X: pd.DataFrame,
    estimador: BaseEstimator,
) -> Pipeline:
    """
    Constrói a Pipeline de Machine Learning.

    A Pipeline é composta por duas etapas:

    1. Pré-processamento dos dados.
    2. Algoritmo de Machine Learning.

    Parameters
    ----------
    X : pd.DataFrame
        Conjunto de atributos preditores.

    estimador : BaseEstimator
        Algoritmo compatível com a API do Scikit-Learn.

    Returns
    -------
    Pipeline
        Pipeline configurada para treinamento e predição.
    """

    preprocessador = criar_preprocessador(X)

    pipeline = Pipeline(
        steps=[
            ("preprocessador", preprocessador),
            ("modelo", estimador),
        ]
    )

    return pipeline