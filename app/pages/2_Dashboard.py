import plotly.express as px
import streamlit as st

from utils.constants import CORES_NIVEIS, ORDEM_NIVEIS, ROTULOS_NIVEIS
from utils.data_loader import carregar_dados_dashboard
from utils.styles import aplicar_estilos, card_kpi, configurar_grafico, hero, rodape

aplicar_estilos()
hero(
    "Dashboard analítico",
    "Visão exploratória dos 2.087 registros tratados, construída "
    "exclusivamente a partir das análises e variáveis presentes na EDA.",
)

try:
    dados = carregar_dados_dashboard()
except Exception as erro:
    st.error(f"Não foi possível carregar a base analítica: {erro}")
    st.stop()

with st.sidebar:
    st.markdown("### Filtros do dashboard")
    niveis = st.multiselect(
        "Nível de obesidade", ORDEM_NIVEIS, default=ORDEM_NIVEIS,
        format_func=lambda x: ROTULOS_NIVEIS[x],
    )
    generos_disponiveis = sorted(dados["ds_genero"].unique())
    generos = st.multiselect(
        "Sexo", generos_disponiveis, default=generos_disponiveis,
        format_func=lambda x: "Feminino" if x == "Female" else "Masculino",
    )
    idade_minima = int(dados.nr_idade.min())
    idade_maxima = int(dados.nr_idade.max())
    faixa_idade = st.slider(
        "Faixa etária", idade_minima, idade_maxima,
        (idade_minima, idade_maxima),
    )
    st.caption("Os KPIs e gráficos são atualizados automaticamente.")

filtrado = dados[
    dados.ds_nivel_obesidade.isin(niveis)
    & dados.ds_genero.isin(generos)
    & dados.nr_idade.between(*faixa_idade)
].copy()

if filtrado.empty:
    st.warning("Nenhum registro corresponde aos filtros selecionados.")
    st.stop()

idade_predominante = filtrado.nr_idade.round().mode().iloc[0]
k1, k2, k3, k4, k5 = st.columns(5)
card_kpi(k1, "pacientes", "blue", "Pacientes", f"{len(filtrado):,.0f}".replace(",", "."), "Total após os filtros")
card_kpi(k2, "idade_media", "orange", "Idade média", f"{filtrado.nr_idade.mean():.1f} anos", "Média do perfil selecionado")
card_kpi(k3, "idade_predominante", "purple", "Idade predominante", f"{idade_predominante:.0f} anos", "Moda da amostra filtrada")
card_kpi(k4, "historico_familiar", "rose", "Histórico familiar", f"{filtrado.fl_historico_familiar_sobrepeso.mean():.1%}", "Relato de sobrepeso familiar")
card_kpi(k5, "transporte_ativo", "green", "Transporte ativo", f"{filtrado.fl_transporte_ativo.mean():.1%}", "Caminhada ou bicicleta")

abas = st.tabs(["Panorama", "Hábitos", "Perfil clínico", "Insights"])

with abas[0]:
    c1, c2 = st.columns([1.25, 1])
    dist = filtrado.ds_nivel_obesidade.value_counts().reindex(ORDEM_NIVEIS, fill_value=0).reset_index()
    dist.columns = ["nivel", "pacientes"]
    dist["rotulo"] = dist.nivel.map(ROTULOS_NIVEIS)

    fig = px.bar(dist, x="pacientes", y="rotulo", orientation="h", text="pacientes", color="nivel", color_discrete_map=CORES_NIVEIS, title="Distribuição dos níveis de obesidade")
    fig.update_traces(textposition="outside", texttemplate="<b>%{text}</b>", textfont=dict(family="Arial Black, Inter, sans-serif", size=12), cliponaxis=False, hovertemplate="%{y}<br><b>%{x} pacientes</b><extra></extra>")
    fig.update_layout(showlegend=False, yaxis_title="", xaxis_title="Pacientes", bargap=0.28)
    configurar_grafico(fig, 430)
    with c1:
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    genero = filtrado.assign(genero=filtrado.ds_genero.map({"Female": "Feminino", "Male": "Masculino"})).groupby(["ds_nivel_obesidade", "genero"]).size().reset_index(name="pacientes")
    genero["nivel"] = genero.ds_nivel_obesidade.map(ROTULOS_NIVEIS)
    fig2 = px.bar(genero, x="nivel", y="pacientes", color="genero", barmode="group", text="pacientes", color_discrete_map={"Feminino": "#C45A8A", "Masculino": "#3A78B8"}, title="Níveis de obesidade por sexo")
    fig2.update_traces(textposition="outside", texttemplate="<b>%{text}</b>", textfont=dict(family="Arial Black, Inter, sans-serif", size=11), cliponaxis=False, hovertemplate="%{x}<br>%{fullData.name}: <b>%{y}</b><extra></extra>")
    fig2.update_layout(xaxis_title="", yaxis_title="Pacientes", xaxis_tickangle=-30, bargap=0.24, bargroupgap=0.08)
    configurar_grafico(fig2, 430)
    fig2.update_layout(
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.24,
            xanchor="center",
            x=0.5,
            title_text="",
            font=dict(size=11, color="#66728F"),
            bgcolor="rgba(0,0,0,0)",
        ),
        margin=dict(l=18, r=18, t=62, b=95),
    )
    with c2:
        with st.container(border=True):
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<div class="dashboard-note">Leitura: o primeiro gráfico apresenta o equilíbrio entre as sete classes; o segundo permite observar diferenças de composição por sexo.</div>', unsafe_allow_html=True)

with abas[1]:
    c1, c2 = st.columns(2)
    habitos = filtrado.groupby("ds_nivel_obesidade", as_index=False).agg(vegetais=("cd_consumo_de_vegetais", "mean"), atividade=("cd_frequencia_atividade_fisica", "mean"), agua=("cd_consumo_agua", "mean"))
    habitos["nivel"] = habitos.ds_nivel_obesidade.map(ROTULOS_NIVEIS)
    longo = habitos.melt(id_vars="nivel", value_vars=["vegetais", "atividade", "agua"], var_name="indicador", value_name="media")
    longo["indicador"] = longo.indicador.map({"vegetais": "Consumo de vegetais", "atividade": "Atividade física", "agua": "Consumo de água"})
    fig = px.bar(longo, x="nivel", y="media", color="indicador", barmode="group", text="media", color_discrete_map={"Consumo de vegetais": "#12A995", "Atividade física": "#1769E8", "Consumo de água": "#69AEE8"}, title="Médias das escalas de hábitos por nível")
    fig.update_traces(textposition="outside", texttemplate="<b>%{text:.2f}</b>", textfont=dict(family="Arial Black, Inter, sans-serif", size=10), cliponaxis=False, hovertemplate="%{x}<br>%{fullData.name}: <b>%{y:.2f}</b><extra></extra>")
    fig.update_layout(xaxis_title="", yaxis_title="Média da escala", xaxis_tickangle=-30, bargap=0.22, bargroupgap=0.07)
    configurar_grafico(fig, 470)
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.25,
            xanchor="center",
            x=0.5,
            title_text="",
            font=dict(size=11, color="#66728F"),
            bgcolor="rgba(0,0,0,0)",
        ),
        margin=dict(l=18, r=18, t=62, b=105),
    )
    with c1:
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    transporte = filtrado.ds_meio_transporte.value_counts().reset_index()
    transporte.columns = ["transporte", "pacientes"]
    mapa_transportes = {"Public_Transportation": "Transporte público", "Automobile": "Automóvel", "Walking": "Caminhada", "Motorbike": "Motocicleta", "Bike": "Bicicleta"}
    transporte["transporte"] = transporte.transporte.map(mapa_transportes)
    fig2 = px.pie(transporte, names="transporte", values="pacientes", title="Meio de transporte habitual", hole=0.58, color_discrete_sequence=["#12A995", "#1769E8", "#F0A33A", "#9650E6", "#5BBD77"])
    fig2.update_traces(textposition="inside", textinfo="percent", textfont=dict(family="Arial Black, Inter, sans-serif", size=12), marker=dict(line=dict(color="#FFFFFF", width=3)), hovertemplate="%{label}<br><b>%{value} pacientes</b> · %{percent}<extra></extra>")
    configurar_grafico(fig2, 450)
    with c2:
        with st.container(border=True):
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<div class="dashboard-note">As escalas seguem o dicionário da EDA: vegetais e água variam de 1 a 3; atividade física varia de 0 a 3.</div>', unsafe_allow_html=True)

with abas[2]:
    c1, c2 = st.columns(2)
    fig = px.box(filtrado.assign(nivel=filtrado.ds_nivel_obesidade.map(ROTULOS_NIVEIS)), x="nivel", y="nr_idade", color="nivel", color_discrete_map={ROTULOS_NIVEIS[k]: v for k, v in CORES_NIVEIS.items()}, title="Distribuição da idade por nível de obesidade", points=False)
    fig.update_traces(showlegend=False, line_width=1.5, hovertemplate="%{x}<br>Idade: <b>%{y:.1f} anos</b><extra></extra>")
    fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Idade", xaxis_tickangle=-30)
    configurar_grafico(fig, 440)
    with c1:
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    imc = filtrado.groupby("ds_nivel_obesidade", as_index=False).nr_imc.mean()
    imc["nivel"] = imc.ds_nivel_obesidade.map(ROTULOS_NIVEIS)
    fig2 = px.line(imc, x="nivel", y="nr_imc", markers=True, text="nr_imc", title="IMC médio por nível — verificação diagnóstica")
    fig2.update_traces(line=dict(color="#009E8E", width=3), marker=dict(size=9, color="#FFFFFF", line=dict(color="#009E8E", width=3)), texttemplate="<b>%{text:.1f}</b>", textposition="top center", textfont=dict(family="Arial Black, Inter, sans-serif", size=11, color="#253252"), hovertemplate="%{x}<br>IMC médio: <b>%{y:.2f}</b><extra></extra>")
    fig2.update_layout(xaxis_title="", yaxis_title="IMC médio", xaxis_tickangle=-30)
    configurar_grafico(fig2, 440)
    with c2:
        with st.container(border=True):
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
    st.info("O IMC é exibido apenas como diagnóstico exploratório. Ele não é utilizado pelo modelo comportamental em produção.")

with abas[3]:
    maior = dist.loc[dist.pacientes.idxmax()]
    pct_favc = filtrado.fl_consumo_calorico_frequente.mean()
    pct_ativo = filtrado.fl_transporte_ativo.mean()
    media_atividade = filtrado.cd_frequencia_atividade_fisica.mean()
    insights = [
        f"A classe mais frequente no recorte é {maior['rotulo']}, com {int(maior['pacientes'])} pacientes.",
        f"{filtrado.fl_historico_familiar_sobrepeso.mean():.1%} dos registros possuem histórico familiar de sobrepeso.",
        f"{pct_favc:.1%} relatam consumo frequente de alimentos muito calóricos.",
        f"A média de atividade física é {media_atividade:.2f} na escala de 0 a 3, enquanto {pct_ativo:.1%} utilizam caminhada ou bicicleta como transporte habitual.",
    ]
    for texto in insights:
        st.markdown(f'<div class="insight">{texto}</div>', unsafe_allow_html=True)
    st.caption("Insights descritivos calculados dinamicamente sobre o recorte filtrado; não representam causalidade.")

rodape()