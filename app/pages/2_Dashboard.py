import plotly.express as px
import streamlit as st
from utils.constants import ORDEM_NIVEIS, ROTULOS_NIVEIS, CORES_NIVEIS
from utils.data_loader import carregar_dados_dashboard
from utils.styles import aplicar_estilos, hero, rodape

aplicar_estilos()
hero("Dashboard analítico", "Visão exploratória dos 2.087 registros tratados, construída exclusivamente a partir das análises e variáveis presentes na EDA.")

try:
    dados = carregar_dados_dashboard()
except Exception as erro:
    st.error(f"Não foi possível carregar a base analítica: {erro}")
    st.stop()

with st.sidebar:
    st.markdown("### Filtros do dashboard")
    niveis = st.multiselect("Nível de obesidade", ORDEM_NIVEIS, default=ORDEM_NIVEIS, format_func=lambda x: ROTULOS_NIVEIS[x])
    generos = st.multiselect("Sexo", sorted(dados["ds_genero"].unique()), default=sorted(dados["ds_genero"].unique()), format_func=lambda x: "Feminino" if x == "Female" else "Masculino")
    faixa_idade = st.slider("Faixa etária", int(dados.nr_idade.min()), int(dados.nr_idade.max()), (int(dados.nr_idade.min()), int(dados.nr_idade.max())))
    st.caption("Os KPIs e gráficos são atualizados automaticamente.")

filtrado = dados[dados.ds_nivel_obesidade.isin(niveis) & dados.ds_genero.isin(generos) & dados.nr_idade.between(*faixa_idade)].copy()
if filtrado.empty:
    st.warning("Nenhum registro corresponde aos filtros selecionados.")
    st.stop()

idade_predominante = filtrado.nr_idade.round().mode().iloc[0]
k1,k2,k3,k4,k5 = st.columns(5)
k1.metric("Pacientes", f"{len(filtrado):,.0f}".replace(",", "."))
k2.metric("Idade média", f"{filtrado.nr_idade.mean():.1f} anos")
k3.metric("Idade predominante", f"{idade_predominante:.0f} anos")
k4.metric("Histórico familiar", f"{filtrado.fl_historico_familiar_sobrepeso.mean():.1%}")
k5.metric("Transporte ativo", f"{filtrado.fl_transporte_ativo.mean():.1%}")

abas = st.tabs(["Panorama", "Hábitos", "Perfil clínico", "Insights"])
with abas[0]:
    c1,c2 = st.columns([1.25,1])
    dist = filtrado.ds_nivel_obesidade.value_counts().reindex(ORDEM_NIVEIS, fill_value=0).reset_index()
    dist.columns=["nivel","pacientes"]; dist["rotulo"] = dist.nivel.map(ROTULOS_NIVEIS)
    fig = px.bar(dist, x="pacientes", y="rotulo", orientation="h", text="pacientes", color="nivel", color_discrete_map=CORES_NIVEIS, title="Distribuição dos níveis de obesidade")
    fig.update_layout(showlegend=False, yaxis_title="", xaxis_title="Pacientes", height=430)
    c1.plotly_chart(fig, use_container_width=True)
    genero = filtrado.assign(genero=filtrado.ds_genero.map({"Female":"Feminino","Male":"Masculino"})).groupby(["ds_nivel_obesidade","genero"]).size().reset_index(name="pacientes")
    genero["nivel"] = genero.ds_nivel_obesidade.map(ROTULOS_NIVEIS)
    fig2=px.bar(genero,x="nivel",y="pacientes",color="genero",barmode="group",title="Níveis de obesidade por sexo")
    fig2.update_layout(xaxis_title="",yaxis_title="Pacientes",height=430,xaxis_tickangle=-35)
    c2.plotly_chart(fig2,use_container_width=True)
    st.caption("Leitura: o primeiro gráfico apresenta o equilíbrio entre as sete classes; o segundo permite observar diferenças de composição por sexo.")

with abas[1]:
    c1,c2=st.columns(2)
    habitos=filtrado.groupby("ds_nivel_obesidade",as_index=False).agg(vegetais=("cd_consumo_de_vegetais","mean"),atividade=("cd_frequencia_atividade_fisica","mean"),agua=("cd_consumo_agua","mean"))
    habitos["nivel"]=habitos.ds_nivel_obesidade.map(ROTULOS_NIVEIS)
    longo=habitos.melt(id_vars="nivel",value_vars=["vegetais","atividade","agua"],var_name="indicador",value_name="media")
    longo["indicador"]=longo.indicador.map({"vegetais":"Consumo de vegetais","atividade":"Atividade física","agua":"Consumo de água"})
    fig=px.bar(longo,x="nivel",y="media",color="indicador",barmode="group",title="Médias das escalas de hábitos por nível")
    fig.update_layout(xaxis_title="",yaxis_title="Média da escala",xaxis_tickangle=-35,height=450)
    c1.plotly_chart(fig,use_container_width=True)
    transporte=filtrado.ds_meio_transporte.value_counts().reset_index(); transporte.columns=["transporte","pacientes"]
    mapa={"Public_Transportation":"Transporte público","Automobile":"Automóvel","Walking":"Caminhada","Motorbike":"Motocicleta","Bike":"Bicicleta"}; transporte["transporte"]=transporte.transporte.map(mapa)
    fig2=px.pie(transporte,names="transporte",values="pacientes",title="Meio de transporte habitual",hole=.55)
    fig2.update_layout(height=450)
    c2.plotly_chart(fig2,use_container_width=True)
    st.caption("As escalas seguem o dicionário da EDA: vegetais e água variam de 1 a 3; atividade física varia de 0 a 3.")

with abas[2]:
    c1,c2=st.columns(2)
    fig=px.box(filtrado.assign(nivel=filtrado.ds_nivel_obesidade.map(ROTULOS_NIVEIS)),x="nivel",y="nr_idade",title="Distribuição da idade por nível de obesidade",points=False)
    fig.update_layout(xaxis_title="",yaxis_title="Idade",xaxis_tickangle=-35,height=440)
    c1.plotly_chart(fig,use_container_width=True)
    imc=filtrado.groupby("ds_nivel_obesidade",as_index=False).nr_imc.mean(); imc["nivel"]=imc.ds_nivel_obesidade.map(ROTULOS_NIVEIS)
    fig2=px.line(imc,x="nivel",y="nr_imc",markers=True,title="IMC médio por nível — verificação diagnóstica")
    fig2.update_layout(xaxis_title="",yaxis_title="IMC médio",xaxis_tickangle=-35,height=440)
    c2.plotly_chart(fig2,use_container_width=True)
    st.info("O IMC é exibido apenas como diagnóstico exploratório. Ele não é utilizado pelo modelo comportamental em produção.")

with abas[3]:
    maior = dist.loc[dist.pacientes.idxmax()]
    pct_favc = filtrado.fl_consumo_calorico_frequente.mean()
    pct_ativo = filtrado.fl_transporte_ativo.mean()
    media_atividade = filtrado.cd_frequencia_atividade_fisica.mean()
    insights=[
        f"A classe mais frequente no recorte é **{maior['rotulo']}**, com **{int(maior['pacientes'])} pacientes**.",
        f"**{filtrado.fl_historico_familiar_sobrepeso.mean():.1%}** dos registros possuem histórico familiar de sobrepeso.",
        f"**{pct_favc:.1%}** relatam consumo frequente de alimentos muito calóricos.",
        f"A média de atividade física é **{media_atividade:.2f}** na escala de 0 a 3, enquanto **{pct_ativo:.1%}** utilizam caminhada ou bicicleta como transporte habitual.",
    ]
    for texto in insights: st.markdown(f'<div class="insight">{texto}</div>',unsafe_allow_html=True)
    st.caption("Insights descritivos calculados dinamicamente sobre o recorte filtrado; não representam causalidade.")
rodape()
