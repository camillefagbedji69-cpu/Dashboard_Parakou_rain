import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("Parakou_Daily.csv", sep = ",", skiprows = 13)  ##importation de la base de données 

df['Date'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str), format='%Y%j') ## conversion en date 
df = df.rename(columns={
    "T2M_MAX":"Tmax",
    "T2M_MIN":"Tmin",
    "PRECTOTCORR":"Rain",
    "ALLSKY_SFC_SW_DWN":"Radiation",
    "QV2M":"QV"
})  ## renommer les colonnes 


col = list(df.columns)  ## liste des colonnes 
cols = col[2:7]  ## slicing des colonnes 
for p in cols : 
    df[p] = df[p].mask(df[p]<0) ##mettre NaN pour les valeurs aberrantes 
    df = df.fillna(df[df[p]>0].median()) ##imputation par la médiane des valeurs positives

df['Tmean'] = (df['Tmax'] + df['Tmin']) / 2  ##température moyenne
df['ET0'] = 0.0023 * (df['Tmax'] - df['Tmin'])**0.5 * (
    df['Tmean'] + 17.8) * df['Radiation'] ## Evapotranspiration selon Hargreaves 


st.title("Dashboard de la pluviométrie et l'évapotranspiration dans la commune de Parakou - Bénin (Janvier 2020 - Août 2025) ") ##titre du graphiques 


fig = go.Figure()

# Pluviométrie
fig.add_trace(go.Scatter(x=df["Date"], y=df["Rain"], mode='lines', name="Pluie", line=dict(color="blue")))

# Exemple d'autre courbe (ex: température moyenne)
fig.add_trace(go.Scatter(x=df["Date"], y=df["ET0"], mode='lines', name="Evapotranspiration", line=dict(color="red")))

fig.update_layout(title="Évolution de la pluie et l'évapotranspiration")
st.plotly_chart(fig)


