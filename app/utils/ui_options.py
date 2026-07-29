"""
ui_options.py

Centraliza todas as opções, títulos e textos de ajuda utilizados
na interface Streamlit.

As CHAVES dos dicionários são exibidas ao usuário.
Os VALORES são enviados ao modelo de Machine Learning.
"""

# OPÇÕES DOS CAMPOS

SEXO = {
    "Feminino": "Female",
    "Masculino": "Male",
}

SIM_NAO = {
    "Sim": "yes",
    "Não": "no",
}

FREQUENCIA = {
    "Nunca": "no",
    "Às vezes": "Sometimes",
    "Frequentemente": "Frequently",
    "Sempre": "Always",
}

TRANSPORTE = {
    "Automóvel": "Automobile",
    "Motocicleta": "Motorbike",
    "Bicicleta": "Bike",
    "Transporte Público": "Public_Transportation",
    "Caminhada": "Walking",
}

# TÍTULOS DOS CAMPOS

TITULOS = {

    "sexo": "Sexo",

    "idade": "Idade",

    "historico":
        "Histórico familiar de sobrepeso",

    "favc":
        "Consumo frequente de alimentos calóricos",

    "fcvc":
        "Frequência de consumo de vegetais",

    "ncp":
        "Número de refeições principais",

    "caec":
        "Lanches entre refeições",

    "smoke":
        "Fumante",

    "ch2o":
        "Consumo médio diário de água",

    "scc":
        "Monitora a ingestão de calorias",

    "faf":
        "Frequência de atividade física",

    "tue":
        "Tempo diário de uso de dispositivos eletrônicos",

    "calc":
        "Consumo de bebidas alcoólicas",

    "mtrans":
        "Principal meio de transporte",
}

# TEXTOS DE AJUDA

HELP = {

    "sexo":
        "Selecione o sexo biológico informado no questionário.",

    "idade":
        "Informe a idade em anos completos.",

    "historico":
        "Indique se existe histórico familiar de sobrepeso ou obesidade.",

    "favc":
        "Indique se existe consumo frequente de alimentos ricos em calorias.",

    "fcvc":
        "Frequência de consumo de vegetais.\n\n"
        "1 = Baixa frequência\n"
        "2 = Frequência moderada\n"
        "3 = Alta frequência",

    "ncp":
        "Número médio de refeições principais realizadas diariamente.",

    "caec":
        "Frequência com que realiza lanches entre as refeições principais.",

    "smoke":
        "Informe se a pessoa é fumante.",

    "ch2o":
        "Quantidade média de água consumida diariamente.\n\n"
        "1 = Baixo consumo\n"
        "2 = Consumo moderado\n"
        "3 = Alto consumo",

    "scc":
        "Indique se costuma monitorar a ingestão diária de calorias.",

    "faf":
        "Frequência de prática de atividade física.\n\n"
        "0 = Nunca\n"
        "1 = Raramente\n"
        "2 = Frequentemente\n"
        "3 = Muito frequente",

    "tue":
        "Tempo diário dedicado ao uso de televisão, computador, celular ou videogame.\n\n"
        "0 = Baixo\n"
        "1 = Moderado\n"
        "2 = Elevado",

    "calc":
        "Frequência de consumo de bebidas alcoólicas.",

    "mtrans":
        "Principal meio de transporte utilizado nas atividades diárias.",
}

# TÍTULOS DAS SEÇÕES

SECOES = {
    "individuais": "👤 Características Individuais",
    "historico": "🧬 Histórico Familiar",
    "alimentacao": "🥗 Hábitos Alimentares",
    "estilo_vida": "🏃 Estilo de Vida",
    "mobilidade": "🚍 Mobilidade",
}