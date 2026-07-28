"""Constantes compartilhadas pela aplicação Streamlit."""
ORDEM_NIVEIS = [
    "Insufficient_Weight", "Normal_Weight", "Overweight_Level_I",
    "Overweight_Level_II", "Obesity_Type_I", "Obesity_Type_II", "Obesity_Type_III",
]
ROTULOS_NIVEIS = {
    "Insufficient_Weight": "Peso insuficiente", "Normal_Weight": "Peso normal",
    "Overweight_Level_I": "Sobrepeso I", "Overweight_Level_II": "Sobrepeso II",
    "Obesity_Type_I": "Obesidade I", "Obesity_Type_II": "Obesidade II",
    "Obesity_Type_III": "Obesidade III",
}
CORES_NIVEIS = {
    "Insufficient_Weight": "#78A9CF", "Normal_Weight": "#45A982",
    "Overweight_Level_I": "#E2B84B", "Overweight_Level_II": "#E28A3B",
    "Obesity_Type_I": "#D96952", "Obesity_Type_II": "#C84C55", "Obesity_Type_III": "#913B5B",
}
MAPEAMENTO_COLUNAS = {
    "genero": "ds_genero", "idade": "nr_idade",
    "historico_familiar": "fl_historico_familiar_sobrepeso",
    "consumo_calorico_frequente": "fl_consumo_calorico_frequente",
    "consumo_vegetais": "cd_consumo_de_vegetais",
    "numero_refeicoes": "cd_numero_refeicoes_principais",
    "lanches": "ds_lanches_entre_refeicoes", "fumante": "fl_fumante",
    "consumo_agua": "cd_consumo_agua", "monitora_calorias": "fl_monitora_calorias",
    "atividade_fisica": "cd_frequencia_atividade_fisica",
    "tempo_eletronicos": "cd_tempo_uso_eletronicos", "consumo_alcool": "ds_consumo_alcool",
    "meio_transporte": "ds_meio_transporte",
}