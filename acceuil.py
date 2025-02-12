import streamlit as st
from streamlit_folium import folium_static
import folium


def blank_line(nb_blank: int = 1):
    """Ajoute des lignes vides dans l'interface."""
    for _ in range(nb_blank):
        st.text("")


def miles_to_meters(miles: float) -> float:
    """Convertit des miles en mètres."""
    return miles * 1609


def create_map():
    """Crée une carte interactive avec les zones définies."""
    locations = {
        "Résidence": ([45.3597, 5.5995], 5),
        "Saint-Égrève": ([45.2517, 5.6633], 4),
        "Grenoble": ([45.166672, 5.71667], 3),
    }

    # Initialisation de la carte
    st_egreve_coords = [45.2517, 5.6633]
    m = folium.Map(location=st_egreve_coords, zoom_start=10)

    # Ajout des marqueurs et cercles
    for name, (coords, radius) in locations.items():
        folium.Marker(coords, tooltip=name).add_to(m)
        folium.Circle(coords, radius=miles_to_meters(radius)).add_to(m)

    return m


def display_intro_section():
    """Affiche la section d'introduction."""
    st.markdown(
        "<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>",
        unsafe_allow_html=True,
    )
    st.info(
        "Dans le menu déroulant _***Navigation***_ de la barre latérale, "
        "choisissez une catégorie pour accéder au contenu."
    )
    blank_line(3)

    col1, _, col2 = st.columns((2, 0.2, 1))
    with col1:
        st.subheader("Qui suis-je ?")
        st.markdown(
            "<div style='text-align: justify;'>"
            "Ingénieur IA et Docteur ingénieur en Physico-Chimie des Matériaux, je mets à profit "
            "mes connaissances et mon savoir-faire pour développer des solutions innovantes dans le domaine "
            "de l’Intelligence Artificielle."
            "</div>",
            unsafe_allow_html=True,
        )


def display_activity_section(m):
    """Affiche la section des zones d'activités."""
    col1, _, col2 = st.columns((1, 0.2, 2))
    with col1:
        blank_line(10)
        st.image("img/keyword_acc.jpg")
    with col2:
        st.subheader("Zones d'activités")
        folium_static(m)


def display_footer():
    """Affiche le pied de page."""
    blank_line(3)
    st.markdown(
        "<h3 style='text-align: center; color: gray;'>N'hésitez pas à parcourir les différentes catégories de cette app.</h3>",
        unsafe_allow_html=True,
    )


def accueille_page():
    """Affiche la page d'accueil."""
    display_intro_section()
    map_object = create_map()
    display_activity_section(map_object)
    display_footer()
