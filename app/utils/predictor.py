"""Preparação dos dados de entrada e execução segura da predição."""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.model_loader import carregar_modelo
from src.data_processing import converter_flags_binarias, criar_features_comportamentais

MAPA_RENOMEACAO_COLUNAS = {
    "Gender":"ds_genero", "Age":"nr_idade", "family_history":"fl_historico_familiar_sobrepeso",
    "FAVC":"fl_consumo_calorico_frequente", "FCVC":"cd_consumo_de_vegetais",
    "NCP":"cd_numero_refeicoes_principais", "CAEC":"ds_lanches_entre_refeicoes",
    "SMOKE":"fl_fumante", "CH2O":"cd_consumo_agua", "SCC":"fl_monitora_calorias",
    "FAF":"cd_frequencia_atividade_fisica", "TUE":"cd_tempo_uso_eletronicos",
    "CALC":"ds_consumo_alcool", "MTRANS":"ds_meio_transporte",
}
COLUNAS_MODELO = [
    "ds_genero", "nr_idade", "fl_historico_familiar_sobrepeso",
    "fl_consumo_calorico_frequente", "cd_consumo_de_vegetais",
    "cd_numero_refeicoes_principais", "ds_lanches_entre_refeicoes", "fl_fumante",
    "cd_consumo_agua", "fl_monitora_calorias", "cd_frequencia_atividade_fisica",
    "cd_tempo_uso_eletronicos", "ds_consumo_alcool", "ds_meio_transporte",
    "fl_transporte_ativo", "ds_faixa_etaria", "ds_consumo_alcool_agrupado",
]
MAPA_CLASSES = {
    "Insufficient_Weight":"Peso insuficiente", "Normal_Weight":"Peso normal",
    "Overweight_Level_I":"Sobrepeso Grau I", "Overweight_Level_II":"Sobrepeso Grau II",
    "Obesity_Type_I":"Obesidade Tipo I", "Obesity_Type_II":"Obesidade Tipo II",
    "Obesity_Type_III":"Obesidade Tipo III",
}

def preparar_entrada(dados_usuario: dict) -> pd.DataFrame:
    ausentes = set(MAPA_RENOMEACAO_COLUNAS) - set(dados_usuario)
    if ausentes:
        raise ValueError(f"Campos obrigatórios ausentes: {sorted(ausentes)}")
    dados = pd.DataFrame([dados_usuario]).rename(columns=MAPA_RENOMEACAO_COLUNAS)
    dados = converter_flags_binarias(dados)
    dados = criar_features_comportamentais(dados)
    faltantes = set(COLUNAS_MODELO) - set(dados.columns)
    if faltantes:
        raise ValueError(f"As features esperadas não foram geradas: {sorted(faltantes)}")
    return dados[COLUNAS_MODELO]

def prever(dados_usuario: dict) -> dict:
    modelo = carregar_modelo()
    entrada = preparar_entrada(dados_usuario)
    classe_modelo = modelo.predict(entrada)[0]
    vetor = modelo.predict_proba(entrada)[0]
    probabilidades_modelo = {classe: float(prob) for classe, prob in zip(modelo.classes_, vetor)}
    probabilidades = {MAPA_CLASSES.get(classe, classe): prob for classe, prob in probabilidades_modelo.items()}
    return {
        "classe_modelo": classe_modelo,
        "classe": MAPA_CLASSES.get(classe_modelo, classe_modelo),
        "probabilidades": probabilidades,
        "probabilidades_modelo": probabilidades_modelo,
        "confianca": probabilidades_modelo[classe_modelo],
        "entrada_processada": entrada,
    }
