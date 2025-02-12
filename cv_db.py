import streamlit as st
from PIL import Image

# Initialisation des paramètres de la page
st.set_page_config(page_title="CV JB DENIS", layout="wide", page_icon="img/profil.jpg")


# Chargement des images
def load_images():
    return {
        "profil": Image.open("img/profils2.png"),
        "bar": Image.open("img/bar.jpg"),
        "comp_duo": Image.open("img/comp_duo.jpg"),
        "comp_ico": Image.open("img/comp_ico.jpg"),
        "form_road": Image.open("img/form_road2.jpg"),
        "glob_comp": Image.open("img/glob_comp2.jpg"),
        "glob_int": Image.open("img/glob_int.jpg"),
        "glob_exp": Image.open("img/glob_exp.jpg"),
        "glob_form": Image.open("img/glob_form.jpg"),
        "glob_kw": Image.open("img/glob_kw3.jpg"),
    }


images = load_images()


# Configuration de la barre latérale
def set_sidebar():
    st.sidebar.image(images["profil"], width=220)
    st.sidebar.title("Jean-Benoît DENIS, Ph.D")
    st.sidebar.subheader("Data Scientist - Ingénieur")
    st.sidebar.image(images["bar"], use_container_width=True)
    st.sidebar.markdown(
        "<h1 style='text-align: center; color: blue;'>Navigation</h1>",
        unsafe_allow_html=True,
    )
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
    st.sidebar.image(images["bar"], use_container_width=True)
    st.sidebar.write(":telephone_receiver: 06 29 07 69 72")
    st.sidebar.write(
        ":e-mail: [jeanbenoitdenis@gmail.com](mailto:jeanbenoitdenis@gmail.com)"
    )
    st.sidebar.write(
        ":round_pushpin:[4 Rue Hector Blanchet 38500 Voiron](https://goo.gl/maps/E8iCnmAg6AetDBy76)"
    )
    return option


# Sections de la page
def page_accueil():
    st.markdown(
        "<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>",
        unsafe_allow_html=True,
    )
    st.info(
        "Dans le menu déroulant **Navigation** de la barre latérale, choisissez une catégorie pour accéder au contenu."
    )
    st.subheader("Aperçu du contenu :")
    col1, _, col2 = st.columns((1, 0.2, 1))
    with col1:
        st.subheader("Compétences")
        st.image(images["glob_comp"], use_container_width=True)
    with col2:
        st.subheader("Expériences")
        st.image(images["glob_exp"], use_container_width=True)

    col1, _, col2, _, col3 = st.columns((1, 0.2, 1, 0.2, 1))
    with col1:
        st.subheader("Intérêts")
        st.image(images["glob_int"], use_container_width=True)
    with col2:
        st.subheader("Formations")
        st.image(images["glob_form"], use_container_width=True)
    with col3:
        st.subheader("Keywords")
        st.image(images["glob_kw"], use_container_width=True)


def page_competences():
    st.header("Compétences")
    st.image(images["comp_duo"], use_container_width=True)
    st.image(images["comp_ico"], use_container_width=True)


def page_formations():
    st.header("Formations")
    st.image(images["form_road"], use_container_width=True)


# Gestion des pages
def handle_pages(option):
    pages = {
        "Accueil": page_accueil,
        "Compétences": page_competences,
        "Formations": page_formations,
        # Ajoutez ici les autres pages, comme expériences, intérêts, médias, publications
    }
    page_function = pages.get(option)
    if page_function:
        page_function()


# Application principale
def main():
    option = set_sidebar()
    handle_pages(option)


if __name__ == "__main__":
    main()
