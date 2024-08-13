
import streamlit as st
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
import countryflag

def header():
    st.image(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\Header.png", use_column_width=True)

def importar_dfs():
    #Importar e tratar dados que serão utilizados
    df = pd.read_csv(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\Spotify2024.csv", encoding='ISO-8859-1')
    df['Spotify Streams']= df['Spotify Streams'].str.replace(',', '').fillna(0).astype(int)
    df['YouTube Views']= df['YouTube Views'].str.replace(',', '').fillna(0).astype(int)
    df['TikTok Likes']= df['TikTok Likes'].str.replace(',', '').fillna(0).astype(int)

    #Classificar por Streams
    df = df.sort_values(by='Spotify Streams', ascending=False).reset_index(drop=True)
    df.index += 1

    #Artistas mais ouvidos
    df_top_artista = df[['Artist', 'Spotify Streams','YouTube Views','TikTok Likes']].copy().groupby('Artist').sum()
    df_top_artista = df_top_artista.sort_values(by='Spotify Streams', ascending=False).reset_index()

    #latinas
    df_latinas = pd.DataFrame({
    'Artista': ['Karol G', 'Anitta', 'Rosalía'],
    'Idade': ["32 anos", "30 anos", "30 anos"],
    'Último álbum': ["Mañana Será Bonito (2023)", "Funk Generation (2024)", "Motomami (2022)"],
    'País': ["Colombia", "Brazil", "Spain"]
    }).set_index('Artista')

    return df, df_top_artista, df_latinas

def top_10_streaming(df):
    st.dataframe(df.head(10))

def trends(musica):
    lista_musicas = [musica]
    df_trend = df[df['Track'].isin(lista_musicas)].copy()
    df_trend['Spotify Streams']= round(df_trend['Spotify Streams']/1000000,2)

    for index, row in df_trend.iterrows():
        st.metric(label= f"{row['Artist']}\n\n{row['Track']}", value=f"{row['Spotify Streams']} Mi", delta=f"{index}° posição")

def top_3_artistas(df):
    st.write(df_top_artista.head(3).set_index('Artist'))


def latinas(nome):
    df_row = df_latinas.loc[nome]
    flag = countryflag.getflag([df_row['País']])
    st.markdown(f"<H3 style='color:#121212;display:inline;'>{flag} {nome}</H3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#121212;display:inline;'>{df_row['Idade']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#121212;display:inline;'>Último álbum: {df_row['Último álbum']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p margin-bottom: 20px'></p>", unsafe_allow_html=True)

#--------------------------------------------APP--------------------------------------------

#---------------------HEADER---------------------
st.markdown(" <style> div[class^='st-emotion-cache-1n76uvr'] { gap: 0px; } </style> ", unsafe_allow_html=True)

df, df_top_artista, df_latinas = importar_dfs()
header()

#---------------------TOP 10---------------------
with stylable_container(
    key="black",
    css_styles="""{
        background-color: #393939;
        padding-top: 30px;
        padding-bottom: 50px;
    }""",
):
    #A tabela não estava respeitando o padding lateral, então usei colunas no lugar
    _,center,_ = st.columns([1,14,1])
    with center:
        st.header("TOP 10 STREAMINGS 2024")
        top_10_streaming(df)

#---------------------TRENDS---------------------
with stylable_container(
    key="green",
    css_styles="""{
        background-color: #31E794;
        padding-left: 40px;  
        padding-right: 20px;
        padding-top: 30px;
        padding-bottom: 50px;
    }""",
):
    #Usei markdown para trocar a cor do texto
    st.markdown("<H2 style='color:#121212;'>TOP TRENDS</H2>", unsafe_allow_html=True)
    col_a,col_b,col_c = st.columns([1,1,1])
    with col_a: 
        trends('CHIHIRO')
        st.audio(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\CHIHIRO.mp3")

    with col_b: 
        trends('BIRDS OF A FEATHER')
        st.audio(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\BIRDS.mp3")

    with col_c: 
        trends('Please Please Please')
        st.audio(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\PLEASE.mp3")

#---------------------TOP ARTISTAS---------------------
with stylable_container(
    key="white",
    css_styles="""{
        background-color: #FFFFFF;
        padding-top: 30px;
        padding-bottom: 50px;
    }""",
):
    st.markdown("<H2 style='color:#121212; padding-left: 40px; padding-bottom: 30px'>TOP 3 ARTISTAS</H2>", unsafe_allow_html=True)
    _,center,_ = st.columns([1,3,1])
    with center:
        top_3_artistas(df_top_artista)

#---------------------TRENDS LATINAS---------------------

with stylable_container(
    key="pink",
    css_styles="""{
        background-color: #ED5F6B;
        padding-left: 40px;  
        padding-right: 40px;
        padding-top: 30px;
        padding-bottom: 50px;
    }""",
):
    st.markdown("<H2 style='color:#121212;margin-bottom:20px;'>TOP LATINAS</H2>", unsafe_allow_html=True)
    col_a,col_b,col_c = st.columns([1,1,1])
    with col_a: 
        latinas('Karol G')
        st.video("https://www.youtube.com/watch?v=orNpRKOfjzY")
    with col_b: 
        latinas('Anitta')
        st.video("https://www.youtube.com/watch?v=uoCIS30VmHE")
    with col_c: 
        latinas('Rosalía')
        st.video("https://www.youtube.com/watch?v=5g2hT4GmAGU")

#---------------------FOOTER---------------------
"""*Este projeto foi feito com Python e Streamlit por Rodrigo Mesquita*"""
