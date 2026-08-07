"""Utilitários de interpretabilidade compatíveis com a pipeline treinada."""
import pandas as pd
from utils.model_loader import carregar_modelo, obter_pipelines_base

TRADUCAO_FEATURES = {
    "nr_idade":"Idade", "fl_historico_familiar_sobrepeso":"Histórico familiar",
    "fl_consumo_calorico_frequente":"Consumo calórico frequente", "fl_fumante":"Tabagismo",
    "fl_monitora_calorias":"Monitoramento de calorias", "fl_transporte_ativo":"Transporte ativo",
    "cd_consumo_de_vegetais":"Consumo de vegetais", "cd_numero_refeicoes_principais":"Refeições principais",
    "cd_consumo_agua":"Consumo de água", "cd_frequencia_atividade_fisica":"Atividade física",
    "cd_tempo_uso_eletronicos":"Tempo em dispositivos", "ds_genero":"Sexo",
    "ds_lanches_entre_refeicoes":"Lanches entre refeições", "ds_consumo_alcool":"Consumo de álcool",
    "ds_meio_transporte":"Meio de transporte", "ds_faixa_etaria":"Faixa etária",
    "ds_consumo_alcool_agrupado":"Consumo de álcool agrupado",
}

def _nome_base(nome_transformado: str) -> str:
    limpo = nome_transformado.split("__", 1)[-1]
    for base in sorted(TRADUCAO_FEATURES, key=len, reverse=True):
        if limpo == base or limpo.startswith(base + "_"):
            return TRADUCAO_FEATURES[base]
    return limpo.replace("_", " ").title()

def obter_importancia_global() -> pd.DataFrame:
    pipelines_base = obter_pipelines_base(carregar_modelo())

    # Quando o modelo carregado é um CalibratedClassifierCV, existe um
    # Random Forest por fold de validação cruzada interna, cada um treinado
    # em ~80% dos dados de treino. Categorias raras (ex.: consumo de álcool
    # "Always") podem não aparecer em algum fold, gerando uma coluna a menos
    # após o OneHotEncoder — por isso a média é feita alinhando por NOME da
    # variável transformada (não por posição), preenchendo com 0 a
    # importância nos folds em que a categoria não existiu.
    series_por_fold = []
    for pipeline in pipelines_base:
        preprocessador = pipeline.named_steps["preprocessador"]
        modelo = pipeline.named_steps["modelo"]
        nomes = preprocessador.get_feature_names_out()
        series_por_fold.append(pd.Series(modelo.feature_importances_, index=nomes))

    importancias = pd.concat(series_por_fold, axis=1).fillna(0).mean(axis=1)

    tabela = importancias.rename("importancia").rename_axis("variavel_transformada").reset_index()
    tabela["variavel"] = tabela["variavel_transformada"].map(_nome_base)
    return (tabela.groupby("variavel", as_index=False)["importancia"].sum()
            .sort_values("importancia", ascending=False).reset_index(drop=True))
