import streamlit as st


def load_publications():
    """Charge les informations des publications."""
    return [
        {
            "title": "Brevet",
            "link": "https://drive.google.com/file/d/1RZVpIPAJiq4zO9LPjO2_ahqiKJrSqQ2A/view?usp=sharing",
            "image": "img/publi_brevet.jpg",
            "description": "_Polymère comme matériau d'électrode pour des batteries secondaires au lithium._ Réf : **WO 2013156899 A1**",
        },
        {
            "title": "Poster",
            "link": "https://drive.google.com/file/d/1btDY31nkJ-ycOGMaT_ar9SBzTMzDSllW/view?usp=sharing",
            "image": "img/publi_poster.jpg",
            "description": "_Influence of impurities on the performance of metal hydride_. MH2014, Manchester, UK, 2014.",
        },
        {
            "title": "Thèse",
            "link": "https://drive.google.com/file/d/1-OMgCIu-agnUHLJW8uUhvnJHNP_fdg7t/view?usp=sharing",
            "image": "img/publi_these.jpg",
            "description": "_Étude de l'influence d'éléments d'addition sur les propriétés de stockage de l'hydrogène dans le système Ti-V-Fe._",
        },
        {
            "title": "Présentation Thèse",
            "link": "https://drive.google.com/file/d/143D5-Euw0HwPIUcxHw49HVQ_j2J1KKZM/view?usp=sharing",
            "image": "img/publi_prix.jpg",
            "description": "1er prix : _Présentation Thèse CEA_, organisé au Liten.",
        },
    ]


def display_publications(publications):
    """Affiche les publications sous forme de colonnes."""
    # Première rangée : Images
    cols = st.columns(len(publications))
    for col, pub in zip(cols, publications):
        col.image(pub["image"], use_container_width=True)

    # Deuxième rangée : Liens et descriptions
    cols = st.columns(len(publications))
    for col, pub in zip(cols, publications):
        col.markdown(f"[**{pub['title']}**]({pub['link']})", unsafe_allow_html=True)
        col.write(pub["description"])


def publis_page():
    """Affiche la page des publications."""
    st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
    st.header("Publications")
    st.text("")
    st.markdown(
        "<h6 style='text-align: center; color: gray;'>Cliquez sur un lien pour accéder au contenu</h6>",
        unsafe_allow_html=True,
    )
    st.text("")

    # Charger les données des publications
    publications = load_publications()

    # Affichage des publications
    display_publications(publications)
