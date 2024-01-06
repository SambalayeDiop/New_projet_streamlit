import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Charger les données à partir du fichier CSV (remplacez 'nom_du_fichier.csv' par le nom de votre fichier CSV)
data = pd.read_csv('data_diass_janvier.csv')

# Afficher les données sous forme de tableau
st.write("Données brutes :")
st.write(data)

# Créer des graphes interactifs
st.write("Graphes interactifs :")

# Graphique de la consommation d'énergie en fonction du temps
st.line_chart(data['Plant Energy (kWh)'])

# Graphique de la puissance de l'usine en fonction du temps
st.line_chart(data['Plant Power (kW)'])

# Graphique de l'insolation de l'usine en fonction du temps
st.line_chart(data['Plant Insolation  (kWh/m2)'])

# Graphique de l'irradiance de l'usine en fonction du temps
st.line_chart(data['Plant Irradiance  (W/m2)'])

# Graphique de l'irradiance horizontale de l'usine en fonction du temps
st.line_chart(data['Plant Irradiance (Horizontal) (W/m2)'])

# Graphique de la température ambiante de l'usine en fonction du temps
st.line_chart(data['Plant Temperature (Ambient) (ºC)'])

# Graphique de la température des panneaux solaires de l'usine en fonction du temps
st.line_chart(data['Plant Temperature (Panel) (ºC)'])
# Ajout d'un graphique de température en fonction de l'insolation
fig_temp_insolation = px.scatter(data, x='Plant Insolation  (kWh/m2)', y='Plant Temperature (Panel) (ºC)',
                                 title='Température des panneaux solaires en fonction de l\'insolation')
st.plotly_chart(fig_temp_insolation)

# Ajout d'un graphique de température en fonction de la puissance
fig_temp_power = px.scatter(data, x='Plant Power (kW)', y='Plant Temperature (Panel) (ºC)',
                            title='Température des panneaux solaires en fonction de la puissance')
st.plotly_chart(fig_temp_power)


# Graphique interactif avec plotly
fig = px.scatter_matrix(data, dimensions=data.columns, title='Matrice de dispersion interactive')
st.plotly_chart(fig)

# Vous pouvez également créer d'autres types de graphes (bar, scatter, etc.) selon vos besoins

# Afficher le dataframe complet si l'utilisateur le souhaite
if st.checkbox('Afficher le DataFrame complet'):
    st.write(data)


