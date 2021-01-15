<h1 align="center"> ⚽ PROJETO FINAL | Jogadores - América do Sul <br></br>
  <img width="300" src="https://github.com/alexandrenussbacher/Ironhack-Projeto_Final/blob/main/imagens/bola.jpg">
  <img width="300" src="https://github.com/alexandrenussbacher/Ironhack-Projeto_Final/blob/main/imagens/conmebol.jpg">
  </h>

## TABELA DE CONTEÚDO

- [PROPOSTA](#proposta)
- [OBJETIVO](#objetivo)
- [PROCESSO](#processo)
- [RESULTADOS](#resultados)
- [MELHORIAS](#melhorias)
- [PROCESSO DE APRENDIZADO](#processo_de_aprendizado)
- [AUTOR](#autor)


<a name="proposta"></a>
## PROPOSTA

Fazer um projeto livre utilizando qualquer conteúdo aprendido durante todo o bootcamp.

<a name="objetivo"></a>
## OBJETIVO

Criar um aplicativo que recomenda jogadores que atuam atualmente nas principais ligas da América do Sul com scouts/características mais próximas ao jogador escolhido pelo usuário.

- **Motivação: análise interessante para um diretor de futebol e analista de desempenho.**

<a name="processo"></a>
## PROCESSO

**1. INTRODUÇÃO** | Busca por uma base de dados:

- **Falta de dados disponíveis e confiáveis (clubes usam Wyscout: fortuna!);**
- Utilização da API do site [rapidapi](https://rapidapi.com/api-sports/api/api-football).

**2. PYTHON** | Limpeza e manipulação dos dados.

**3. PostgreSQL** | Exporte dos Datasets limpos para o SQL.

**4. STREAMLIT** | Criação do aplicativo.

**5. TABLEAU** | Apresentação contendo uma análise exploratória.

<a name="resultados"></a>
## RESULTADOS

[TABLEAU PUBLIC](https://public.tableau.com/profile/alexandre.nussbacher#!/vizhome/RecomendaodejogadoresAmricadoSul/HISTRIA)

[APLICATIVO](http://jogadores.herokuapp.com/)

<img src="https://github.com/alexandrenussbacher/Ironhack-Projeto_Final/blob/main/imagens/aplicativo.png">

<a name="melhorias"></a>
## MELHORIAS

<ol type="1">
<b><li> Confiabilidade dos dados (buscar uma base de dados mais confiável e com mais informações);</b> </li> <p></p>

<li> Partindo desta API, unir dados de outra base (problema: coluna em comum entre as bases, pois o nome dos jogadores varia de uma base para outra):

  - Adicionar informações sobre valor de mercado;

  - Adicionar as ligas faltantes;

  - Considerar outros campeonatos;

  - Separar laterais de zagueiros e volantes de meias. </li> <p></p>

<li> Atribuir importância às variáveis, pensar na melhor distância a ser utilizada e considerar liga e nacionalidade; </li> <p></p>

<li> Exibir imagem do jogador pesquisado e o primeiro recomendado; </li> <p></p>

<li> Selecionar número de jogadores recomendados. </li> <p></p>

<a name="processo_de_aprendizado"></a>
## PROCESSO DE APRENDIZADO

### Habilidades aplicadas:

- [x] Pandas
- [x] Numpy
- [x] Standard Scaler
- [x] Recommendation System
- [x] PostgreSQL
- [x] Tableau (Exploratory Data Analysis)
- [x] Streamlit

<a name="autor"></a>
## AUTOR:

Alexandre Nussbacher
