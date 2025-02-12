import streamlit as st
from acceuil import accueille_page
from competences import competences_page
from data_dict import COMP_DICT, EXP_DICT, SOFT_LIST, TOOLS_DICT
from experience import experience_page
from formations import formations_page
from interets import interets_page
from medias import medias_page
from publications import publis_page


def set_sidebar():
    """Configure la barre latérale."""
    st.sidebar.image("img/profil.png")
    st.sidebar.title("Jean-Benoît DENIS, Ph.D")
    st.sidebar.subheader("Responsable de pôle, Ingénieur Data Scientist")
    st.sidebar.subheader("Ingénieur IA")
    st.sidebar.image("img/bar.jpg", use_container_width=True)
    st.sidebar.markdown(
        "<h1 style='text-align: center; color: blue;'>Navigation</h1>",
        unsafe_allow_html=True,
    )

    # Options de navigation
    option = st.sidebar.selectbox(
        "",
        [
            "Accueil",
            "Compétences",
            "Formations",
            "Expériences",
            "Intérêts",
            "Publications",
            "Médias",
        ],
    )

    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.image("img/bar.jpg", use_container_width=True)

    # Informations personnelles
    st.sidebar.write(":telephone_receiver: 06 29 07 69 72")
    st.sidebar.write(
        ":e-mail: [jeanbenoitdenis@gmail.com](mailto:jeanbenoitdenis@gmail.com)"
    )
    st.sidebar.write(
        ":round_pushpin:[4 Rue Hector Blanchet 38500 Voiron](https://goo.gl/maps/E8iCnmAg6AetDBy76)"
    )

    return option


def apply_custom_styles():
    """Applique des styles CSS personnalisés."""
    st.markdown(
        f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 2560px;
            padding-top: 0rem;
            padding-right: 5rem;
            padding-left: 5rem;
            padding-bottom: 0rem;
        }}
        .reportview-container .main {{
            color: black;
            background-color: white;
        }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def handle_navigation(option):
    """Gère la navigation entre les pages."""
    pages = {
        "Accueil": accueille_page,
        "Compétences": lambda: competences_page(
            data_tools=TOOLS_DICT, data_comp=COMP_DICT, data_soft=SOFT_LIST
        ),
        "Formations": formations_page,
        "Expériences": lambda: experience_page(EXP_DICT),
        "Intérêts": interets_page,
        "Publications": publis_page,
        "Médias": medias_page,
    }

    # Appelle la fonction correspondant à l'option sélectionnée
    page_function = pages.get(option)
    if page_function:
        page_function()


# Main
def main():
    """Point d'entrée principal."""
    st.set_page_config(
        page_title="CV JB DENIS",
        layout="wide",
        page_icon="img/profil.jpg",
    )
    st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)

    # Configure la barre latérale et obtient l'option sélectionnée
    option = set_sidebar()

    # Applique les styles personnalisés
    apply_custom_styles()

    # Gère la navigation
    handle_navigation(option)


if __name__ == "__main__":
    main()
