import streamlit as st

#Exercício 5 - Títulos e textos formatados
st.title("Spotify")
st.header("As Músicas Mais Transmitidas do Spotify em 2024")
st.subheader("Conheça quais foram as músicas mais ouvidas")
st.text("Top 10")
st.markdown("**Acesse nossa** [página oficial](https://www.spotify.com/br/)")

#Exercício 6 - Exibir DataFrame com pandas
import pandas as pd
df = pd.read_csv(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\Spotify2024.csv", encoding='ISO-8859-1')
df['Spotify Streams']= df['Spotify Streams'].str.replace(',', '').fillna(0).astype(int)
df['YouTube Views']= df['YouTube Views'].str.replace(',', '').fillna(0).astype(int)
df['TikTok Likes']= df['TikTok Likes'].str.replace(',', '').fillna(0).astype(int)

df = df.sort_values(by='Spotify Streams', ascending=False).reset_index(drop=True)
df.index += 1

st.dataframe(df.head(10))
st.table(df.head(10))

#Exercício 7 - Exibir métricas
lista_musicas = ['CHIHIRO', 'BIRDS OF A FEATHER','Please Please Please']
df_filtrado = df[df['Track'].isin(lista_musicas)]

for index, row in df_filtrado.iterrows():
    st.metric(label= f"{row['Artist']} - {row['Track']}", value=f"{row['Spotify Streams']} Streams", delta=f"{index}° posição")

#Exercício 8 - Utilizar a função write()
df_artista = df[['Artist', 'Spotify Streams','YouTube Views','TikTok Likes']].copy().groupby('Artist').sum()
df_artista = df_artista.sort_values(by='Spotify Streams', ascending=False).reset_index()

st.write("**Top 3 Artistas:**")
st.write(f"""
    1. {df_artista.iloc[0,0]} 
    2. {df_artista.iloc[1,0]} 
    3. {df_artista.iloc[2,0]} 
    """)
st.write("*Saiba Mais*")
st.write(df_artista.head(3).set_index('Artist'))


#Exercício 9 - Comandos Magic

"**Revelações do Pop Latino**"
df_latinas = pd.DataFrame({
    'Artista': ['Karol G', 'Anitta', 'Rosalía'],
    'Idade': ["32 anos", "30 anos", "30 anos"],
    'Último álbum': ["Mañana Será Bonito (2023)", "Funk Generation (2024)", "Motomami (2022)"],
    'Nacionalidade': ["Colombiana", "Brasileira", "Espanhola"]
}).set_index('Artista')

df_latinas
"""
*Seguidores no Instagram*:
- Karol G [70,1M]
- Anitta [64,4M]
- Rosalía [27,6M]
"""

#Exercício 10 - Incorporar multimídia
st.markdown("## Conheça o Remix de Ta OK de Karol G")
st.image("https://i.scdn.co/image/ab67616d0000b27382de1ca074ae63cb18fce335", width=100)
st.audio(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\KarolG_audio.mp3")
st.video("https://www.youtube.com/watch?v=Ttrt3F-rmhA")

#Exercício 11 - Utilizar animações e emojis
st.image(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\gif_like.gif")

st.button("Curtir :heart:")
