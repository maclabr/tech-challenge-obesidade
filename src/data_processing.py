"""Funções de leitura e tratamento de dados do projeto de previsão de obesidade."""

import pandas as pd

VALORES_FLAG_BINARIA = {"yes": 1, "no": 0}


def carregar_dados_brutos(caminho_arquivo: str, mapa_renomeacao_colunas: dict) -> pd.DataFrame:
    """
    Lê o CSV de dados brutos e renomeia as colunas para os nomes descritivos
    do projeto (prefixos cd_, ds_, fl_ e nr_), conforme `mapa_renomeacao_colunas`.

    Parâmetros
    ----------
    caminho_arquivo : str
        Caminho do arquivo CSV com os dados brutos.
    mapa_renomeacao_colunas : dict
        Mapeamento {nome_original: nome_descritivo} aplicado via `DataFrame.rename`.

    Retorno
    -------
    pd.DataFrame
        Dados brutos com as colunas renomeadas.
    """
    return pd.read_csv(caminho_arquivo).rename(columns=mapa_renomeacao_colunas)


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
