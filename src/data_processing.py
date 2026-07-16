"""Funções de leitura e tratamento de dados do projeto de previsão de obesidade."""

import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Check, Column, DataFrameSchema

VALORES_FLAG_BINARIA = {"yes": 1, "no": 0}

SCHEMA_DADOS_BRUTOS = DataFrameSchema(
    {
        "Gender": Column(str, Check.isin(["Female", "Male"]), nullable=False),
        "Age": Column(float, Check.in_range(1, 120), nullable=False),
        "Height": Column(float, Check.in_range(0.5, 2.5), nullable=False),
        "Weight": Column(float, Check.in_range(2, 300), nullable=False),
        "family_history": Column(str, Check.isin(["yes", "no"]), nullable=False),
        "FAVC": Column(str, Check.isin(["yes", "no"]), nullable=False),
        "FCVC": Column(float, Check.in_range(1, 3), nullable=False),
        "NCP": Column(float, Check.in_range(1, 4), nullable=False),
        "CAEC": Column(str, Check.isin(["no", "Sometimes", "Frequently", "Always"]), nullable=False),
        "SMOKE": Column(str, Check.isin(["yes", "no"]), nullable=False),
        "CH2O": Column(float, Check.in_range(1, 3), nullable=False),
        "SCC": Column(str, Check.isin(["yes", "no"]), nullable=False),
        "FAF": Column(float, Check.in_range(0, 3), nullable=False),
        "TUE": Column(float, Check.in_range(0, 2), nullable=False),
        "CALC": Column(str, Check.isin(["no", "Sometimes", "Frequently", "Always"]), nullable=False),
        "MTRANS": Column(
            str, Check.isin(["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"]), nullable=False
        ),
        "Obesity": Column(
            str,
            Check.isin(
                [
                    "Insufficient_Weight",
                    "Normal_Weight",
                    "Overweight_Level_I",
                    "Overweight_Level_II",
                    "Obesity_Type_I",
                    "Obesity_Type_II",
                    "Obesity_Type_III",
                ]
            ),
            nullable=False,
        ),
    },
    strict=True,
    coerce=False,
)


def validar_dados_brutos(dados: pd.DataFrame) -> pd.DataFrame:
    """
    Valida os dados exatamente como chegam da fonte, com os nomes de coluna
    originais (antes de qualquer rename), contra `SCHEMA_DADOS_BRUTOS`: as 17
    colunas do obesity.csv devem estar presentes (nenhuma faltando, nenhuma
    inesperada), com o tipo, a faixa plausível (numéricas/ordinais) ou o
    conjunto de categorias válidas (categóricas) esperados, e sem nulos. Não
    verifica duplicatas — isso é responsabilidade de `remover_duplicatas_exatas`.

    Deve ser chamada como primeiro passo de `carregar_dados_brutos`, antes do
    rename de colunas.

    Parâmetros
    ----------
    dados : pd.DataFrame
        Dados brutos recém-lidos do CSV, com os nomes de coluna originais
        (Gender, Age, Height, ...).

    Retorno
    -------
    pd.DataFrame
        O mesmo DataFrame de entrada, inalterado, caso a validação passe.

    Levanta
    -------
    pandera.errors.SchemaErrors
        Se qualquer coluna estiver faltando, houver coluna inesperada, tipo
        incompatível, valor fora da faixa esperada, categoria inválida ou
        valor nulo. A exceção lista, para cada problema, a coluna e o motivo
        da falha (`error.failure_cases`), interrompendo o pipeline em vez de
        seguir silenciosamente com dado inválido.
    """
    SCHEMA_DADOS_BRUTOS.validate(dados, lazy=True)
    return dados


def carregar_dados_brutos(caminho_arquivo: str, mapa_renomeacao_colunas: dict) -> pd.DataFrame:
    """
    Lê o CSV de dados brutos, valida seu schema (via `validar_dados_brutos`,
    ainda com os nomes de coluna originais) e só então renomeia as colunas
    para os nomes descritivos do projeto (prefixos cd_, ds_, fl_ e nr_),
    conforme `mapa_renomeacao_colunas`.

    Parâmetros
    ----------
    caminho_arquivo : str
        Caminho do arquivo CSV com os dados brutos.
    mapa_renomeacao_colunas : dict
        Mapeamento {nome_original: nome_descritivo} aplicado via `DataFrame.rename`.

    Retorno
    -------
    pd.DataFrame
        Dados brutos validados, com as colunas renomeadas.
    """
    dados_brutos = pd.read_csv(caminho_arquivo)
    validar_dados_brutos(dados_brutos)
    return dados_brutos.rename(columns=mapa_renomeacao_colunas)


def converter_flags_binarias(dados: pd.DataFrame) -> pd.DataFrame:
    """
    Converte todas as colunas com prefixo `fl_` (flags binárias) de yes/no
    para 1/0. Deve ser chamada logo após a leitura dos dados, antes de
    qualquer outra limpeza.

    Parâmetros
    ----------
    dados : pd.DataFrame
        DataFrame já com as colunas renomeadas, contendo colunas fl_ como texto.

    Retorno
    -------
    pd.DataFrame
        Cópia do DataFrame com as colunas fl_ convertidas para inteiro (1/0).
    """
    dados_convertidos = dados.copy()
    colunas_flag = [coluna for coluna in dados_convertidos.columns if coluna.startswith("fl_")]
    dados_convertidos[colunas_flag] = dados_convertidos[colunas_flag].replace(VALORES_FLAG_BINARIA).astype(int)
    return dados_convertidos


def remover_duplicatas_exatas(dados: pd.DataFrame) -> pd.DataFrame:
    """
    Remove linhas exatamente duplicadas (todas as colunas iguais) e reseta o índice.

    Parâmetros
    ----------
    dados : pd.DataFrame
        DataFrame de entrada, podendo conter duplicatas exatas.

    Retorno
    -------
    pd.DataFrame
        Cópia sem duplicatas exatas, com índice resetado.
    """
    return dados.drop_duplicates().reset_index(drop=True)


def arredondar_colunas_ordinais(dados: pd.DataFrame, colunas_ordinais: list) -> pd.DataFrame:
    """
    Arredonda para inteiro as colunas ordinais que têm ruído decimal no
    dataset original (FCVC, NCP, CH2O, FAF, TUE), conforme o dicionário de
    dados do projeto.

    Parâmetros
    ----------
    dados : pd.DataFrame
        DataFrame de entrada.
    colunas_ordinais : list
        Nomes das colunas ordinais a arredondar.

    Retorno
    -------
    pd.DataFrame
        Cópia do DataFrame com as colunas indicadas arredondadas e convertidas para inteiro.
    """
    dados_arredondados = dados.copy()
    dados_arredondados[colunas_ordinais] = dados_arredondados[colunas_ordinais].round().astype(int)
    return dados_arredondados


def criar_features_comportamentais(dados: pd.DataFrame) -> pd.DataFrame:
    """
    Cria as três novas features comportamentais da etapa de engenharia de
    atributos, todas derivadas de hábito ou demografia — nunca de altura,
    peso ou IMC, para não reforçar a circularidade do alvo com o IMC:

    - fl_transporte_ativo: 1 se o meio de transporte habitual for Walking
      ou Bike, 0 caso contrário.
    - ds_faixa_etaria: faixa etária clínica derivada de nr_idade
      (adolescente, adulto_jovem, adulto, meia_idade).
    - ds_consumo_alcool_agrupado: ds_consumo_alcool com as categorias raras
      Frequently e Always agrupadas em consumo_frequente_ou_mais.

    Parâmetros
    ----------
    dados : pd.DataFrame
        DataFrame tratado, contendo ds_meio_transporte, nr_idade e ds_consumo_alcool.

    Retorno
    -------
    pd.DataFrame
        Cópia do DataFrame com as três novas colunas adicionadas.
    """
    dados_com_features = dados.copy()

    dados_com_features["fl_transporte_ativo"] = (
        dados_com_features["ds_meio_transporte"].isin(["Walking", "Bike"]).astype(int)
    )

    dados_com_features["ds_faixa_etaria"] = pd.cut(
        dados_com_features["nr_idade"],
        bins=[13, 19, 30, 45, 61],
        labels=["adolescente", "adulto_jovem", "adulto", "meia_idade"],
    )

    dados_com_features["ds_consumo_alcool_agrupado"] = dados_com_features["ds_consumo_alcool"].replace(
        {"Frequently": "consumo_frequente_ou_mais", "Always": "consumo_frequente_ou_mais"}
    )

    return dados_com_features
