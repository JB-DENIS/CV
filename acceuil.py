import streamlit as st
from streamlit_folium import folium_static
import folium


def blank_line(nb_blank: int = 1):
    i = 1
    while i != nb_blank:
        st.text("")
        i += 1


def miles_to_meters(miles):
    return miles*1609


voiron = [45.3597, 5.5995]
st_egreve = [45.2517, 5.6633]
gre = [45.166672, 5.71667]

m = folium.Map(location=st_egreve, zoom_start=10)
folium.Marker(voiron, tooltip="Résidence").add_to(m)
folium.Circle(voiron, radius=miles_to_meters(5)).add_to(
    m)
folium.Circle(st_egreve, radius=miles_to_meters(4)).add_to(
    m)
folium.Circle(gre, radius=miles_to_meters(3)).add_to(
    m)


def accueille_page():
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>",
                unsafe_allow_html=True)

    st.info(' Dans le menu déroulant _***Navigation***_ de la barre latérale, choisissez une catégorie pour accéder au contenu.')
    blank_line(3)
    col1, col2, col3 = st.columns((2, 0.2, 1))
    with col1:
        st.subheader("Qui suis je ?")
        st.markdown("<div style='text-align: justify;'>Ingénieur Data Science et Docteur ingénieur en Physico-Chimie des Matériaux, je compte mettre à profit mes connaissances et mon savoir-faire par le développement de solutions innovantes dans le domaine de l’Intelligence Artificielle.</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns((1, 0.2, 2))
    with col1:
        blank_line(10)
        st.image("img/keyword_acc.jpg")
    with col3:
        st.subheader("Zones d'activitée")
        folium_static(m)

    blank_line(3)
    st.markdown("<h3 style='text-align: center; color: gray;'>N'hésitez pas à parcourir les différentes catégories de cette app.</h3>", unsafe_allow_html=True
                )
