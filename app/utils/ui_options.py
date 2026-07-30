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
        "Frequência de atividade física por semana",

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
        "Frequência de consumo de vegetais nas refeições.\n\n"
        "1 = Raramente;\n"
        "2 = Às vezes;\n"
        "3 = Sempre.",

    "ncp":
        "Número de refeições principais realizadas por dia.\n\n"
        "1 = 1;\n"
        "2 = 2;\n"
        "3 = 3;\n"
        "4 = 4 ou mais.",

    "caec":
        "Frequência com que realiza lanches entre as refeições principais.",

    "smoke":
        "Informe se a pessoa é fumante.",

    "ch2o":
        "Quantidade média de água consumida diariamente.\n\n"
        "1 = Menos de 1L;\n"
        "2 = 1 a 2L;\n"
        "3 = Mais de 2L.",

    "scc":
        "Indique se costuma monitorar a ingestão diária de calorias.",

    "faf":
        "Frequência de atividade física por semana.\n\n"
        "0 = Nenhuma;\n"
        "1 = 1 a 2 vezes;\n"
        "2 = 3 a 4 vezes;\n"
        "3 = 5 ou mais vezes.",

    "tue":
        "Tempo diário dedicado ao uso de televisão, computador, celular ou "
        "videogame.\n\n"
        "0 = 0 a 2 horas;\n"
        "1 = 3 a 5 horas;\n"
        "2 = Mais de 5 horas.",

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