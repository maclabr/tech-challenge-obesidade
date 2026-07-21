"""
Script de validação do módulo model_training.py.

Este arquivo executa uma sequência de verificações para garantir que
todas as funções responsáveis pela preparação dos dados para Machine
Learning estejam funcionando corretamente antes do início dos
experimentos de modelagem.

As validações incluem:

- carregamento da camada Silver;
- separação entre atributos e variável alvo;
- divisão entre treino e teste;
- identificação automática dos grupos de variáveis;
- construção do pré-processador;
- construção da Pipeline.

Este script não realiza treinamento de modelos.
"""

from pathlib import Path
import sys
import pandas as pd

# Adiciona a raiz do projeto ao PYTHONPATH
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from sklearn.linear_model import LogisticRegression

from src.model_training import (
    carregar_dados_silver,
    criar_pipeline,
    criar_preprocessador,
    dividir_treino_teste,
    obter_grupos_variaveis,
    separar_features_target,
)

SEPARADOR = "=" * 70

def main():
    """Executa as validações do módulo model_training."""

    print(SEPARADOR)
    print("Validação do módulo model_training.py")
    print(SEPARADOR)

    # =====================================================================
    # Validação 1 - Carregamento da camada Silver
    # =====================================================================

    dados = carregar_dados_silver()

    if dados.empty:
        raise ValueError(
            "A camada Silver foi carregada, mas está vazia."
        )

    print("\n✓ Camada Silver carregada com sucesso.")

    print(f"  Registros : {dados.shape[0]}")
    print(f"  Colunas   : {dados.shape[1]}")
    print(f"  Memória   : {dados.memory_usage(deep=True).sum() / 1024:.2f} KB")

    # =====================================================================
    # Validação 2 - Separação entre atributos e variável alvo
    # =====================================================================

    X, y = separar_features_target(dados)

    if y.name not in dados.columns:
        raise ValueError(
            "A variável alvo não foi encontrada na base original."
        )

    if y.name in X.columns:
        raise ValueError(
            "A variável alvo ainda está presente nos atributos."
        )

    print("\n✓ Variável alvo separada com sucesso.")

    print(f"  Atributos : {X.shape[1]}")
    print(f"  Registros : {X.shape[0]}")
    print(f"  Target    : {y.name}")
    print("\nDistribuição percentual:")
    print((y.value_counts(normalize=True) * 100).round(2))
 
    # =====================================================================
    # Validação 3 - Divisão entre treino e teste
    # =====================================================================

    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    print("\n✓ Divisão treino/teste realizada com sucesso.")

    print(f"  X_train : {X_train.shape}")
    print(f"  X_test  : {X_test.shape}")

    print(f"  y_train : {y_train.shape}")
    print(f"  y_test  : {y_test.shape}")

    print("\nQuantidade absoluta por classe:")

    print(
        pd.DataFrame(
            {
            "Original": y.value_counts().sort_index(),
            "Treino": y_train.value_counts().sort_index(),
            "Teste": y_test.value_counts().sort_index(),
            }
    )
)
    print("\nDistribuição das classes (%)")
    distribuicao = (
        pd.DataFrame(
            {
                "Original": y.value_counts(normalize=True),
                "Treino": y_train.value_counts(normalize=True),
                "Teste": y_test.value_counts(normalize=True),
            }
        )
        .fillna(0)
        .sort_index()
        * 100
    )

    print(distribuicao.round(2))

    diferenca = (
    distribuicao["Original"] - distribuicao["Teste"]
    ).abs()

    maior_diferenca = diferenca.max()

    print(
        f"\nMaior diferença entre a distribuição original "
        f"e o conjunto de teste: {maior_diferenca:.2f}%"
    )

    # =====================================================================
    # Validação 4 - Identificação dos grupos de variáveis
    # =====================================================================

    grupos = obter_grupos_variaveis(X)

    print("\n✓ Grupos de variáveis identificados com sucesso.")

    print("\nVariáveis numéricas:")
    for coluna in grupos["numericas"]:
        print(f"  • {coluna}")

    print("\nVariáveis ordinais:")
    for coluna in grupos["ordinais"]:
        print(f"  • {coluna}")

    print("\nVariáveis categóricas:")
    for coluna in grupos["categoricas"]:
        print(f"  • {coluna}")

    total_classificadas = (
        len(grupos["numericas"])
        + len(grupos["ordinais"])
        + len(grupos["categoricas"])
    )

    print("\nResumo da classificação")

    print(f"  Colunas classificadas : {total_classificadas}")
    print(f"  Colunas esperadas     : {X.shape[1]}")

    if total_classificadas != X.shape[1]:
        raise ValueError(
            "Nem todas as colunas foram classificadas corretamente."
        )

    print("  ✓ Todas as colunas foram classificadas.")

    duplicadas = (
        (set(grupos["numericas"]) & set(grupos["ordinais"]))
        | (set(grupos["numericas"]) & set(grupos["categoricas"]))
        | (set(grupos["ordinais"]) & set(grupos["categoricas"]))
    )

    if duplicadas:
        raise ValueError(
            "As seguintes colunas aparecem em mais de um grupo: "
            f"{sorted(duplicadas)}"
        )

    print("  ✓ Não existem colunas duplicadas entre os grupos.") 

    # =====================================================================
    # Validação 5 - Construção do pré-processador
    # =====================================================================

    preprocessador = criar_preprocessador(X)

    print("\n✓ Pré-processador criado com sucesso.")

    print(f"Tipo do objeto: {type(preprocessador).__name__}")

    if preprocessador.__class__.__name__ != "ColumnTransformer":
        raise TypeError(
            "O objeto retornado não é um ColumnTransformer."
        )

    print(f"\nQuantidade de transformadores: "
          f"{len(preprocessador.transformers)}")

    print("\nTransformadores configurados:")

    for nome, transformador, colunas in preprocessador.transformers:
        print(f"\n• Nome        : {nome}")
        print(f"  Transformador : {transformador}")
        print(f"  Colunas ({len(colunas)}):")

        for coluna in colunas:
            print(f"    - {coluna}")

    if len(preprocessador.transformers) != 3:
        raise ValueError(
            "O ColumnTransformer deve possuir exatamente "
            "3 transformadores."
        )

    if preprocessador.remainder != "drop":
        raise ValueError(
            "O parâmetro remainder deveria ser 'drop'."
        )

    print("\n✓ Estrutura do ColumnTransformer validada.")

    # =====================================================================
    # Validação 5.1 - Execução do pré-processador
    # =====================================================================

    X_transformado = preprocessador.fit_transform(X)

    print("\n✓ Pré-processador executado com sucesso.")

    print(f"Formato original      : {X.shape}")
    print(f"Formato transformado  : {X_transformado.shape}")

    if X_transformado.shape[0] != X.shape[0]:
        raise ValueError(
            "O número de registros foi alterado após o pré-processamento."
        )

    print("✓ Quantidade de registros preservada.")

    import numpy as np

    if np.isnan(X_transformado).any():
        raise ValueError(
            "Foram encontrados valores NaN após o pré-processamento."
        )

    print("✓ Não existem valores ausentes após a transformação.")

    if not np.issubdtype(X_transformado.dtype, np.number):
        raise TypeError(
            "A saída do pré-processador não é totalmente numérica."
        )

    print("✓ Todas as variáveis transformadas são numéricas.")

    novas_colunas = (
        X_transformado.shape[1] - X.shape[1]
    )

    print(
        f"Novas colunas criadas pelo One-Hot Encoding: "
        f"{novas_colunas}"
    )

        # =====================================================================
    # Validação 6 - Construção da Pipeline
    # =====================================================================

    modelo = LogisticRegression(
        max_iter=1000,
        random_state=42,
    )

    pipeline = criar_pipeline(
        X_train,
        modelo,
    )

    print("\n✓ Pipeline criada com sucesso.")

    print(f"Tipo do objeto: {type(pipeline).__name__}")

    if pipeline.__class__.__name__ != "Pipeline":
        raise TypeError(
            "O objeto retornado não é uma Pipeline."
        )

    print("\nEtapas da Pipeline:")

    for nome, etapa in pipeline.steps:
        print(f"  • {nome:<15} -> {type(etapa).__name__}")

    if len(pipeline.steps) != 2:
        raise ValueError(
            "A Pipeline deve possuir exatamente duas etapas."
        )

    if pipeline.steps[0][0] != "preprocessador":
        raise ValueError(
            "A primeira etapa deveria ser 'preprocessador'."
        )

    if pipeline.steps[1][0] != "modelo":
        raise ValueError(
            "A segunda etapa deveria ser 'modelo'."
        )

    pipeline.fit(
        X_train,
        y_train,
    )

    print("\n✓ Pipeline treinada com sucesso.")

    if not hasattr(
        pipeline.named_steps["modelo"],
        "classes_",
    ):
        raise RuntimeError(
            "O modelo não foi treinado corretamente."
        )

    print(
        f"Número de classes aprendidas: "
        f"{len(pipeline.named_steps['modelo'].classes_)}"
    )

    print("✓ Modelo treinado e pronto para predição.")

    print(SEPARADOR)
    print("Todas as validações foram concluídas com sucesso.")
    print(SEPARADOR)


if __name__ == "__main__":
    main()
