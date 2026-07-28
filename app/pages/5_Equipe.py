import streamlit as st
from utils.styles import aplicar_estilos, hero, rodape

aplicar_estilos()
hero("Equipe e entrega", "Projeto acadêmico desenvolvido no Tech Challenge da Pós-Tech Data Analytics da FIAP.")
st.markdown("## Escopo da entrega")
st.write("Análise exploratória, tratamento e engenharia de atributos, comparação de algoritmos, seleção do modelo comportamental, aplicação Streamlit e documentação para deploy.")
st.info("Inclua nesta página os nomes, funções e links profissionais dos integrantes do grupo antes da apresentação final.")
rodape()
