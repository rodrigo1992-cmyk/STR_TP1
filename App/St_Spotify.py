import streamlit as st

st.title("Spotify")
st.header("As Músicas Mais Transmitidas do Spotify em 2024")
st.subheader("Conheça quais foram as músicas mais ouvidas")
st.text("Top 10")
st.markdown("**Acesse nossa** [página oficial](https://www.spotify.com/br/)")

import pandas as pd
df = pd.read_csv(r"C:\Users\RodrigoPintoMesquita\Documents\Ambientes\STR_TP1\Data\Spotify2024.csv", encoding='ISO-8859-1')
df = df.sort_values(by='Spotify Streams', ascending=False).head(10).reset_index(drop=True)
df.index += 1

st.dataframe(df)
st.table(df)

