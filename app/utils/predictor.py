import pandas as pd

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.model_loader import carregar_modelo
from src.data_processing import (
    converter_flags_binarias,
    criar_features_comportamentais,
)

MAPA_RENOMEACAO_COLUNAS = {
    "Gender": "ds_genero",
    "Age": "nr_idade",
    "family_history": "fl_historico_familiar_sobrepeso",
    "FAVC": "fl_consumo_calorico_frequente",
    "FCVC": "cd_consumo_de_vegetais",
    "NCP": "cd_numero_refeicoes_principais",
    "CAEC": "ds_lanches_entre_refeicoes",
    "SMOKE": "fl_fumante",
    "CH2O": "cd_consumo_agua",
    "SCC": "fl_monitora_calorias",
    "FAF": "cd_frequencia_atividade_fisica",
    "TUE": "cd_tempo_uso_eletronicos",
    "CALC": "ds_consumo_alcool",
    "MTRANS": "ds_meio_transporte",
}

COLUNAS_MODELO = [
    "ds_genero",
    "nr_idade",
    "fl_historico_familiar_sobrepeso",
    "fl_consumo_calorico_frequente",
    "cd_consumo_de_vegetais",
    "cd_numero_refeicoes_principais",
    "ds_lanches_entre_refeicoes",
    "fl_fumante",
    "cd_consumo_agua",
    "fl_monitora_calorias",
    "cd_frequencia_atividade_fisica",
    "cd_tempo_uso_eletronicos",
    "ds_consumo_alcool",
    "ds_meio_transporte",
    "fl_transporte_ativo",
    "ds_faixa_etaria",
    "ds_consumo_alcool_agrupado",
]

MAPA_CLASSES = {
    "Insufficient_Weight": "Peso insuficiente",
    "Normal_Weight": "Peso normal",
    "Overweight_Level_I": "Sobrepeso Grau I",
    "Overweight_Level_II": "Sobrepeso Grau II",
    "Obesity_Type_I": "Obesidade Tipo I",
    "Obesity_Type_II": "Obesidade Tipo II",
    "Obesity_Type_III": "Obesidade Tipo III",
}


def prever(dados_usuario: dict) -> dict:

    modelo = carregar_modelo()

    df = pd.DataFrame([dados_usuario])

    df = df.rename(columns=MAPA_RENOMEACAO_COLUNAS)

    df = converter_flags_binarias(df)

    df = criar_features_comportamentais(df)

    colunas_faltantes = set(COLUNAS_MODELO) - set(df.columns)

    if colunas_faltantes:

        raise ValueError(

        f"As seguintes colunas esperadas não foram geradas: {sorted(colunas_faltantes)}"

    )

    df = df[COLUNAS_MODELO]

    classe_modelo = modelo.predict(df)[0]

    probabilidades = modelo.predict_proba(df)[0]

    probabilidades = {
        MAPA_CLASSES.get(classe, classe): float(prob)
        for classe, prob in zip(modelo.classes_, probabilidades)
    }

    return {
        "classe_modelo": classe_modelo,
        "classe": MAPA_CLASSES.get(classe_modelo, classe_modelo),
        "probabilidades": probabilidades,
    }