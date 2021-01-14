# importando bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# título
st.markdown("<h1 style='text-align: center; color: green;'>Jogadores similares - América do Sul</h1>", unsafe_allow_html=True)

# importando Dataframes
jogadores=pd.read_csv("/Users/alexandrenussbacher/Desktop/Ironhack/Ironhack-ProjetoFinal/data/jogadores.csv")
jogadores2=pd.read_csv("/Users/alexandrenussbacher/Desktop/Ironhack/Ironhack-ProjetoFinal/data/jogadores2.csv")
similaridade_goleiros=pd.read_csv("/Users/alexandrenussbacher/Desktop/Ironhack/Ironhack-ProjetoFinal/data/similaridade_goleiros.csv")
similaridade_defesa=pd.read_csv("/Users/alexandrenussbacher/Desktop/Ironhack/Ironhack-ProjetoFinal/data/similaridade_defesa.csv")
similaridade_meias=pd.read_csv("/Users/alexandrenussbacher/Desktop/Ironhack/Ironhack-ProjetoFinal/data/similaridade_meias.csv")
similaridade_atacantes=pd.read_csv("/Users/alexandrenussbacher/Desktop/Ironhack/Ironhack-ProjetoFinal/data/similaridade_atacantes.csv")

# opções das ligas para o usuário selecionar
liga=st.sidebar.selectbox("Escolha uma liga:", np.sort(jogadores["liga"].unique()))

# opções dos times para o usuário selecionar
time=st.sidebar.selectbox("Escolha um time:", np.sort(jogadores.loc[jogadores["liga"]==liga, "time"].unique()))

# opções das posições para o usuário selecionar
lst=jogadores.loc[jogadores["time"]==time, "posição"].unique()
lista=["Goalkeeper", "Defender", "Midfielder", "Attacker"]
ordem={key: i for i, key in enumerate(lista)}
posição=st.sidebar.selectbox("Escolha uma posição", sorted(lst, key=lambda d: ordem[d]))

# opções dos jogadores para o usuário selecionar
jogador=st.sidebar.selectbox("Escolha um jogador", np.sort(jogadores.loc[(jogadores["time"]==time) & (jogadores["posição"]==posição), "nome"].unique()))

# definindo uma variável que exibe o id do jogador escolhido pelo usuário
id=jogadores.loc[(jogadores["nome"]==jogador) & (jogadores["posição"]==posição) & (jogadores["time"]==time), "id"].values[0]

# exibindo o nome do jogador escolhido
st.write("Jogador escolhido:", jogador)
# exibindo as informações do jogador escolhido
st.dataframe(jogadores2.loc[jogadores2["id"]==id, :].set_index("nome").drop("id", axis=1))

# função do gráfico de similaridade
def grafico_similaridade(df1, similaridade):
    # gráfico de similaridade
    st.write("Gráfico de similaridade:")
    # definindo os índices do Dataframe exibido
    indexers=np.unique(df1.index.values, return_index=True)[1]
    # definindo os nomes dos jogadores a serem exibidos no eixo x
    x=[df1.index.values[index] for index in sorted(indexers)]
    # definindo o grau de similaridade a ser exibido no eixo y
    y=similaridade.set_index("id")[str(id)].sort_values(ascending=False)[1:6].values
    # plotando o gráfico
    fig, ax=plt.subplots(figsize =(14, 7))
    plot=sns.barplot(x=x, y=y)
    plt.grid()
    plt.rc('xtick',labelsize=10)
    plt.rc('ytick',labelsize=10)
    for p in plot.patches:
        plot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', size=10, xytext = (0, 10), textcoords = 'offset points')
    plt.xlabel("jogador")
    plt.ylabel("similaridade")
    plt.rcParams["axes.labelsize"] = 15
    plt.title(f"Jogador: {jogador}", color="olive", fontname="Times New Roman",fontweight="bold", fontsize=35)
    st.pyplot(fig)

# -----------------------------------------------------------------------------------------------------------------------

# goleiros
if posição=="Goalkeeper":

    # definindo uma variável que exibe o id dos 5 goleiros mais similares ao escolhido pelo usuário
    goleiros_similares=similaridade_goleiros.set_index("id")[str(id)].sort_values(ascending=False).index.unique()[1:6]

    # jogadores semelhantes
    st.write("Jogadores com características semelhantes:")
    # definindo uma variável que encontra o id dos 5 goleiros semelhantes no Dataframe a ser mostrado
    df=jogadores2.loc[jogadores2["id"].isin(goleiros_similares)]
    # definindo uma variável que exibe as informações dos goleiros semelhantes
    df1=df.set_index("nome").drop("id", axis=1).iloc[pd.Categorical(df["id"], categories=goleiros_similares, ordered=True).argsort()]
    # exibindo as informações dos goleiros semelhantes
    st.dataframe(df1)

    # gráfico de similaridade
    grafico_similaridade(df1, similaridade_goleiros)
    
# -----------------------------------------------------------------------------------------------------------------------

# defensores
if posição=="Defender":

    # definindo uma variável que exibe o id dos 5 defensores mais similares ao escolhido pelo usuário
    defesa_similares=similaridade_defesa.set_index("id")[str(id)].sort_values(ascending=False).index.unique()[1:6]
    # jogadores semelhantes
    st.write("Jogadores com características semelhantes:")
    # definindo uma variável que encontra o id dos 5 defensores semelhantes no Dataframe a ser mostrado
    df=jogadores2.loc[jogadores2["id"].isin(defesa_similares)]
    # definindo uma variável que exibe as informações dos defensores semelhantes
    df1=df.set_index("nome").drop("id", axis=1).iloc[pd.Categorical(df["id"], categories=defesa_similares, ordered=True).argsort()]
    # exibindo as informações dos defensores semelhantes
    st.dataframe(df1)

    # gráfico de similaridade
    grafico_similaridade(df1, similaridade_defesa)
    
# -----------------------------------------------------------------------------------------------------------------------

#meias
if posição=="Midfielder":

    # definindo uma variável que exibe o id dos 5 meias mais similares ao escolhido pelo usuário
    meias_similares=similaridade_meias.set_index("id")[str(id)].sort_values(ascending=False).index.unique()[1:6]

    # jogadores semelhantes
    st.write("Jogadores com características semelhantes:")
    # definindo uma variável que encontra o id dos 5 meias semelhantes no Dataframe a ser mostrado
    df=jogadores2.loc[jogadores2["id"].isin(meias_similares)]
    # definindo uma variável que exibe as informações dos meias semelhantes
    df1=df.set_index("nome").drop("id", axis=1).iloc[pd.Categorical(df["id"], categories=meias_similares, ordered=True).argsort()]
    # exibindo as informações dos defensores semelhantes
    st.dataframe(df1)

    # gráfico de similaridade
    grafico_similaridade(df1, similaridade_meias)

# -----------------------------------------------------------------------------------------------------------------------

#atacantes
if posição=="Attacker":
    # definindo uma variável que exibe o id dos 5 atacantes mais similares ao escolhido pelo usuário
    atacantes_similares=similaridade_atacantes.set_index("id")[str(id)].sort_values(ascending=False).index.unique()[1:6]

    # jogadores semelhantes
    st.write("Jogadores com características semelhantes:")
    # definindo uma variável que encontra o id dos 5 atacantes semelhantes no Dataframe a ser mostrado
    df=jogadores2.loc[jogadores2["id"].isin(atacantes_similares)]
    # definindo uma variável que exibe as informações dos atacantes semelhantes
    df1=df.set_index("nome").drop("id", axis=1).iloc[pd.Categorical(df["id"], categories=atacantes_similares, ordered=True).argsort()]
    # exibindo as informações dos atacantes semelhantes
    st.dataframe(df1)

    # gráfico de similaridade
    grafico_similaridade(df1, similaridade_atacantes)