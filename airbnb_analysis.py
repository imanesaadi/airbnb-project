import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Charger les données
donnees = pd.read_csv("AB_NYC_2019.csv")

# 2. Nettoyer les données (enlever les prix extrêmes)
donnees_clean = donnees[donnees['price'] < 500]

# 3. Analyse exploratoire de base

# Afficher les 5 premières lignes
print("Les 5 premières lignes :")
print(donnees_clean.head())

# Informations générales
print("\nInformations sur les colonnes :")
print(donnees_clean.info())

# Valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(donnees_clean.isnull().sum())

# Statistiques descriptives
print("\nStatistiques descriptives :")
print(donnees_clean.describe())

# 4. Visualisations

sns.set(style="whitegrid")

# Nombre d'annonces par quartier
plt.figure(figsize=(8, 5))
sns.countplot(data=donnees_clean, x='neighbourhood_group', palette='Set2')
plt.title("Nombre d'annonces par quartier")
plt.xlabel("Quartier")
plt.ylabel("Nombre d'annonces")
plt.show()

# Distribution des prix par quartier (avec limite 500)
plt.figure(figsize=(10, 6))
sns.boxplot(data=donnees_clean, x='neighbourhood_group', y='price', palette='Set3')
plt.title("Distribution des prix par quartier")
plt.xlabel("Quartier")
plt.ylabel("Prix (€)")
plt.ylim(0, 500)
plt.show()

# Répartition géographique des annonces
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=donnees_clean,
    x='longitude',
    y='latitude',
    hue='neighbourhood_group',
    alpha=0.4,
    palette='Set1'
)
plt.title("Répartition géographique des annonces Airbnb à New York")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Quartier")
plt.show()

# 5. Analyse supplémentaire: types de chambre

plt.figure(figsize=(8, 5))
sns.countplot(data=donnees_clean, x='room_type', palette='pastel')
plt.title("Distribution des types de chambre")
plt.xlabel("Type de chambre")
plt.ylabel("Nombre d'annonces")
plt.show()

# Moyenne des prix par type de chambre
prix_moyen_room = donnees_clean.groupby('room_type')['price'].mean().sort_values(ascending=False)
print("Prix moyen par type de chambre:")
print(prix_moyen_room)
