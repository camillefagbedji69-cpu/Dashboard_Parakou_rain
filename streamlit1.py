import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("Parakou_Daily.csv", sep = ",", skiprows = 13)  ##importation de la base de données 

df['Date'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str), format='%Y%j') ## conversion en date 
df = df.rename(columns={
    "T2M_MAX":"Tmax",
    "T2M_MIN":"Tmin",
    "PRECTOTCORR":"Rain",
    "ALLSKY_SFC_SW_DWN":"Radiation",
    "QV2M":"QV"
})

st.title("Dashboard de la pluviométrie dans la commune de Parakou (Bénin)")

fig = px.line(df, x="Date", y="Rain", title="Évolution de la pluviométrie")
st.plotly_chart(fig)

