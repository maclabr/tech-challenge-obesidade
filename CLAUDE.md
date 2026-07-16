# CLAUDE.md

## Sobre o projeto
Tech Challenge (Fase 4 — Data Analytics) da pós-graduação. Contexto: cientista de
dados contratado por um hospital, desenvolvendo um modelo de Machine Learning para
prever o nível de obesidade de pacientes a partir de hábitos alimentares, atividade
física e dados antropométricos, apoiando a decisão da equipe médica.

Prazo de entrega: 28/07/2026. Projeto em grupo.

## Entregáveis obrigatórios
- Pipeline de ML completo (feature engineering + treinamento), documentado.
- Modelo com acurácia acima de 75%.
- Deploy do modelo em app preditivo com Streamlit.
- Painel analítico com insights sobre obesidade voltado à equipe médica.
- Documento (.doc/.txt) com links do app, do painel e do repositório GitHub.
- Vídeo de 4–10 min apresentando a estratégia e o sistema em visão de negócio.

## Dataset e dicionário de dados
Arquivo: `data/raw/obesity.csv`.

Atenção — confirmar sempre com `df.columns` antes de referenciar estas colunas no
código, pois há divergência entre as fontes do desafio:
- Coluna alvo: o enunciado chama de `Obesity_level`, o dicionário detalhado chama
  de `Obesity`. Usar o nome real da coluna no arquivo.
- O enunciado chama uma coluna de `TER`; o dicionário detalhado chama a mesma
  coluna de `TUE`. Usar o nome real da coluna no arquivo.

| Coluna | Descrição | Valores |
|---|---|---|
| Gender | Sexo biológico | Female, Male |
| Age | Idade em anos | numérico contínuo (14–61) |
| Height | Altura em metros | numérico contínuo (1.45–1.98) |
| Weight | Peso em kg | numérico contínuo (39–173) |
| family_history | Histórico familiar de excesso de peso | yes, no |
| FAVC | Consumo frequente de alimentos muito calóricos | yes, no |
| FCVC | Frequência de consumo de vegetais | escala 1–3 (1 raramente, 2 às vezes, 3 sempre) — valores no arquivo têm ruído decimal, arredondar |
| NCP | Número de refeições principais/dia | escala 1–4 — arredondar valores decimais |
| CAEC | Come entre as refeições | no, Sometimes, Frequently, Always |
| SMOKE | Fuma | yes, no |
| CH2O | Consumo diário de água | escala 1–3 (1 <1L, 2 1–2L, 3 >2L) — arredondar |
| SCC | Monitora calorias ingeridas | yes, no |
| FAF | Frequência semanal de atividade física | escala 0–3 — arredondar |
| TUE | Tempo diário em dispositivos eletrônicos (dicionário chama TUE; enunciado chama TER) | escala 0–2 (0 ~0-2h, 1 ~3-5h, 2 >5h) — arredondar |
| CALC | Consumo de álcool | no, Sometimes, Frequently, Always |
| MTRANS | Meio de transporte habitual | Automobile, Motorbike, Bike, Public_Transportation, Walking |
| Obesity (alvo) | Nível de obesidade | Insufficient_Weight, Normal_Weight, Overweight_Level_I, Overweight_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III |

Nota importante de modelagem: este é o dataset público "Estimation of obesity
levels" (UCI), cujo rótulo é originalmente derivado de fórmulas de IMC
(peso/altura²). Ou seja, Height e Weight sozinhos quase determinam o target. Ao
construir features e treinar modelos, deixar essa decisão explícita e documentada
em markdown — não tratar como uma escolha neutra.

## Metodologia do projeto (seguir esta ordem de etapas)
1. Entendimento do problema de negócio: objetivo, variável alvo, métrica de sucesso.
2. Coleta e validação dos dados: duplicados, inconsistências, dados faltantes, vieses.
3. Análise exploratória (EDA): distribuições, correlações, outliers, classes desbalanceadas.
4. Limpeza e tratamento: nulos, duplicatas, padronização, outliers.
5. Engenharia de features: novas variáveis, razões, indicadores; avaliar importância e multicolinearidade.
6. Preparação para ML: encoding, normalização/padronização, balanceamento de classes, split treino/validação/teste.
7. Construção e treinamento dos modelos: testar múltiplos algoritmos com validação cruzada.
8. Avaliação dos modelos: métricas adequadas ao problema (aqui, classificação multiclasse — accuracy, precision, recall, F1, matriz de confusão), não só accuracy.
9. Interpretabilidade: quais variáveis mais pesam na decisão, o modelo faz sentido para o negócio (feature importance, SHAP se for viável).
10. Deploy: app Streamlit do modelo preditivo.
11. Monitoramento: fora do escopo obrigatório deste Tech Challenge, mas mencionar como próximo passo na conclusão/vídeo, se fizer sentido.
12. Documentação e boas práticas: markdown explicativo, storytelling, funções reutilizáveis, nomes claros, reprodutibilidade, README.

## Estrutura de notebooks (storytelling)
Todo notebook de EDA ou modelagem deve seguir esta ordem de seções, cada uma
com um título em markdown:
1. Objetivo do projeto/notebook
2. Importação das bibliotecas
3. Configurações iniciais
4. Leitura dos dados
5. Análise exploratória
6. Limpeza dos dados
7. Engenharia de atributos
8. Modelagem
9. Avaliação
10. Conclusões

## Boas práticas de código
- Usar markdown como narrativa: antes de cada bloco de transformação, uma célula
  markdown curta explicando o que será feito e por quê (o notebook deve poder ser
  lido como um relatório, não só executado).
- Nomes de variáveis sempre claros e descritivos (`clientes_ativos`,
  `base_treino`), nunca genéricos (`df1`, `temp`, `x2`).
- Nunca sobrescrever o dataframe original. Em vez de `df = df.dropna()`, usar
  `clientes_limpos = clientes.dropna()`.
- Organizar os imports em um único bloco no topo do arquivo, agrupados em:
  bibliotecas padrão, bibliotecas de terceiros, código do projeto (`src/`).
- Usar `sklearn.Pipeline`/`ColumnTransformer` sempre que houver pré-processamento,
  mesmo em notebooks exploratórios — facilita reaproveitar no deploy do Streamlit.

## Instruções específicas para o Claude Code
- Seguir a "Metodologia do projeto" (12 etapas) como referência de processo ao
  planejar qualquer tarefa nova, mesmo que a tarefa cubra só uma etapa.
- Ao criar ou editar notebooks, seguir sempre a "Estrutura de notebooks
  (storytelling)" acima, com os títulos markdown na ordem indicada.
- Aplicar as "Boas práticas de código" em qualquer código gerado, sem precisar que
  isso seja pedido de novo a cada prompt.
- Ao tratar FCVC, NCP, CH2O, FAF e TUE, aplicar o arredondamento indicado no
  dicionário de dados antes de qualquer encoding ou modelagem.
- Antes de escrever código que referencie a coluna alvo ou a coluna de tempo de
  tela, confirmar o nome real dessas colunas no CSV (ver alerta na seção do
  dataset) em vez de assumir `Obesity_level` ou `TER`.
- Salvar modelo + pipeline de pré-processamento juntos com `joblib`.
- Validar modelos com validação cruzada estratificada e reportar accuracy,
  F1-macro e matriz de confusão — nunca só accuracy, por ser problema multiclasse.
- Lógica de limpeza e feature engineering decidida em notebook (remoção de
  duplicatas, arredondamentos, novas features) deve ser extraída para funções
  em `src/` assim que estabilizada; notebooks devem importar e chamar essas
  funções em vez de reimplementar a lógica inline.
- Colunas com prefixo `fl_` (flags binárias) devem ser convertidas para 1/0
  logo na leitura dos dados, nunca mantidas como texto (`yes`/`no`).
- Todo carregamento de dado bruto novo deve passar por `validar_dados_brutos`
  (schema, tipos, faixas e categorias válidas, via pandera) antes de qualquer
  outra transformação — nunca renomear ou limpar antes de validar.

## Estrutura do repositório
- data/bronze: dado original, nunca sobrescrever
- data/silver: dados tratados (camada silver, pronta para a modelagem)
- notebooks: exploração (EDA) e testes de modelagem
- src: código reutilizável (pipeline de pré-processamento, treino, avaliação)
- app: aplicação Streamlit do modelo preditivo
- dashboard: painel analítico de insights
- docs: documentação de apoio

## Ambiente
- Python 3.11+, ambiente virtual em `venv/`
- Instalar dependências: `pip install -r requirements.txt`
- Rodar o app do modelo: `streamlit run app/app.py`
- Sempre que instalar uma nova biblioteca: `pip freeze > requirements.txt`

## Convenções de commit
Mensagens curtas no padrão `tipo: descrição` (ex.: `feat: pipeline de encoding das
categóricas`, `fix: corrige split estratificado`, `chore: atualiza requirements`).

## Fluxo de colaboração
Projeto em grupo, uma branch por tarefa, Pull Request para a main antes de
integrar. Setup completo de ambiente para o grupo está documentado à parte
(guia de setup compartilhado com as colegas).