import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
donnees = pd.read_csv("AB_NYC_2019.csv")
donnees_clean = donnees[donnees['price'] < 500]

st.title("Analyse Airbnb New York City")

# Choix du quartier
quartier = st.selectbox("Choisissez un quartier", donnees_clean['neighbourhood_group'].unique())

# Filtrer les données selon le quartier choisi
data_filtrée = donnees_clean[donnees_clean['neighbourhood_group'] == quartier]

# Afficher un résumé
st.write(f"Nombre d'annonces dans {quartier}: {len(data_filtrée)}")
st.write(f"Prix moyen: ${data_filtrée['price'].mean():.2f}")

# Afficher la distribution des prix
fig, ax = plt.subplots()
sns.histplot(data_filtrée['price'], bins=30, ax=ax)
ax.set_title(f"Distribution des prix dans {quartier}")
st.pyplot(fig)
