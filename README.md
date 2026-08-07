# Tech Challenge — Fase 4 | Predição de Níveis de Obesidade

Projeto da Pós-Tech em Data Analytics (FIAP). Solução de Machine Learning para estimar o nível de obesidade de pacientes de um hospital fictício, a partir de características demográficas, histórico familiar e hábitos de vida — apoiando ações preventivas e a priorização do cuidado.

**Aplicação publicada:** https://tech-challenge-fase04.streamlit.app/

---

## Contexto e objetivo

O dataset utilizado (*Estimation of Obesity Levels*, UCI) classifica pacientes em 7 níveis de obesidade, com rótulo derivado originalmente de uma fórmula de IMC (peso / altura²). Isso significa que altura, peso e IMC têm relação quase determinística com o alvo — se usados diretamente, o modelo tenderia a reproduzir uma fórmula matemática em vez de aprender padrões de hábitos de vida.

Por isso o projeto avaliou dois cenários de modelagem:

- **Referência** — utiliza todas as variáveis disponíveis, incluindo altura, peso e IMC.
- **Comportamental** — exclui altura, peso e IMC de propósito, restando apenas variáveis demográficas e comportamentais.

O cenário **comportamental** foi o escolhido para produção, por representar uma estimativa baseada em hábitos de vida, e não uma fórmula de IMC disfarçada de modelo preditivo.

## Metodologia

1. **Avaliação e tratamento dos dados** — validação de schema, remoção de duplicatas exatas, arredondamento das escalas ordinais e análise de distribuição/correlação das variáveis (camada Silver, 2.087 registros).
2. **Engenharia de features** — criação de variáveis comportamentais adicionais: flag de transporte ativo, faixa etária agrupada e consumo de álcool agrupado.
3. **Comparação de modelos** — vários algoritmos de classificação avaliados por validação cruzada estratificada (5 folds), com métricas reportadas na ordem clínica das 7 classes.
4. **Seleção do modelo** — Random Forest com hiperparâmetros padrão, escolhido sobre o XGBoost (que teve acurácia de validação cruzada ligeiramente maior) por apresentar menor gap entre validação e teste, menor sinal de overfitting e treinamento mais rápido.
5. **Tentativas testadas e não adotadas** — busca de hiperparâmetros (RandomizedSearchCV) para o Random Forest, sem ganho relevante sobre os parâmetros padrão que justificasse a complexidade adicional.
6. **Calibração de probabilidade** — `CalibratedClassifierCV` (method="sigmoid", validação cruzada estratificada de 5 folds) aplicado sobre o pipeline final, para corrigir o viés conhecido do Random Forest de produzir probabilidades pouco realistas. Resultado validado em teste antes da adoção (ver métricas abaixo).

## Resultados

| Métrica | Valor |
|---|---|
| Acurácia (validação cruzada) | 79,6% |
| Acurácia (teste, modelo calibrado) | 80,4% |
| F1-macro (validação cruzada) | 78,9% |
| Meta do projeto | 75,0% (superada) |

**Limitação conhecida:** a classe *Sobrepeso Grau II* é a mais difícil de prever — recall de 64% no modelo final (partiu de 16% nas primeiras versões testadas), provavelmente por ficar numa zona de transição comportamental entre classes vizinhas. Documentado como prioridade para uma próxima iteração.

## Aplicação

Aplicação Streamlit multipágina, publicada no Streamlit Community Cloud:

- **Home** — visão geral do projeto.
- **Projeto** — contexto, metodologia e stack utilizada.
- **Dashboard** — análise exploratória interativa (filtros por nível de obesidade, sexo e faixa etária).
- **Predição** — formulário em etapas para estimar o nível de obesidade a partir de dados comportamentais, com leitura de confiança e importância das variáveis.
- **Modelo** — metodologia, métricas de desempenho e interpretabilidade do Random Forest.
- **Equipe** — integrantes do projeto.

## Estrutura do repositório

```
.
├── .streamlit/        # Configuração do Streamlit (tema, config.toml)
├── app/                # Código da aplicação Streamlit (páginas e utilitários)
├── data/               # Camadas de dados (bronze/silver)
├── models/             # Modelo treinado (.joblib)
├── notebooks/          # Notebooks de EDA e modelagem
├── src/                # Módulos reutilizáveis (pré-processamento, treino, avaliação)
├── tests/              # Testes automatizados
└── requirements.txt    # Dependências do projeto
```

## Como rodar localmente

```bash
git clone https://github.com/maclabr/tech-challenge-obesidade.git
cd tech-challenge-obesidade
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
streamlit run app/app.py
```

## Próximos passos

- Monitoramento contínuo de *data drift* e retreinamento periódico do modelo à medida que novos dados forem coletados.
- Aprimoramento da experiência do usuário (UX) da aplicação.
- Investigar estratégias específicas para melhorar o recall da classe Sobrepeso Grau II.

## Equipe

- Maria Clara De Oliveira e Silva: mariaclara.os@gmail.com
- Sabrina da Silva Nascimento: sabrina.nascto@gmail.com
- Iara Rafaela Alves Portuense: iara.rafaela@hotmail.com

---

*Projeto acadêmico desenvolvido para o Tech Challenge da Fase 4 — Pós-Tech Data Analytics, FIAP. Não substitui diagnóstico, avaliação antropométrica ou decisão de profissional de saúde.*
