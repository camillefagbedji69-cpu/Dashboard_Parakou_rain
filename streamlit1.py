import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("Parakou_Daily.csv", sep = ",", skiprows = 13)
df['Date'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str), format='%Y%j')

st.title("Dashboard de la pluviométrie dans la commune de Parakou (Bénin)")

fig = px.line(df, x="Date", y="mean", title="Évolution du NDVI")
st.plotly_chart(fig)
