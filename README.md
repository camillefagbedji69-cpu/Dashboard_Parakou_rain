# 🌍 Dashboard Climatologique – Parakou (Bénin)

Ce projet propose un **tableau de bord interactif** développé avec **Streamlit** et **Plotly**, permettant de visualiser et d’analyser la **pluviométrie** et l’**évapotranspiration de référence (ET₀)** à Parakou (Bénin) entre **janvier 2020 et août 2025**.

Le script calcule l’**évapotranspiration selon la méthode de Hargreaves** et identifie automatiquement les périodes de **saison sèche** (quand la demande en eau dépasse les précipitations).

## ✨ Fonctionnalités

* 📊 **Visualisation interactive** des précipitations et de l’évapotranspiration.
* 🌡️ **Calcul de la température moyenne** (Tmean) et de l’ET₀ (avec la méthode de Hargreaves).
* 🧹 **Nettoyage et imputation des données** (remplacement des valeurs aberrantes par la médiane).
* ☀️ **Détection automatique des saisons sèches** avec surbrillance en jaune sur le graphique.
* 🖥️ Interface utilisateur simple avec **Streamlit**.

## 📂 Données

* Fichier d’entrée : `Parakou_Daily.csv`
* Source : Données climatiques locales (format NASA POWER).
* Colonnes utilisées :

  * `T2M_MAX` → Température maximale (°C)
  * `T2M_MIN` → Température minimale (°C)
  * `PRECTOTCORR` → Pluviométrie (mm/jour)
  * `ALLSKY_SFC_SW_DWN` → Radiation solaire (MJ/m²/jour)
  * `QV2M` → Humidité spécifique

## URL de l'application 
https://dashboardparakourain-fzjaqrr9kg76cssg8q3f9x.streamlit.app/
## 🔧 Améliorations possibles

* Ajouter des indicateurs agroclimatiques (Indice de sécheresse, SPEI, etc.).
* Intégrer d’autres stations ou communes du Bénin.
* Comparer les saisons sèches détectées avec les observations de terrain.
