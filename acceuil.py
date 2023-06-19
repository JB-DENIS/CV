import streamlit as st
from competences import competences_page
from data_dict import EXP_DICT, TOOLS_DICT

from experience import experience_page
from formations import formations_page
from interets import interets_page
from medias import medias_page
from publications import publis_page


def accueille_page():
    st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>",
                unsafe_allow_html=True)

    st.info(' Dans le menu déroulant _***Navigation***_ de la sidebar, choisissez une catégorie pour accéder au contenu.')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("img/ico_form.jpg", use_column_width="always")

    with col2:
        st.image("img/ico_comp.jpg", use_column_width="always")

    with col3:
        st.image("img/ico_exp.jpg", use_column_width="always")

    col1, col2, col3 = st.columns(3)
    with col1:

        formation = st.button("FORMATIONS")
    with col2:

        comp = st.button("COMPETENCES")
    with col3:

        exp = st.button("EXPERIENCES")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("img/ico_int.jpg", use_column_width="always")

    with col2:
        st.image("img/ico_pub.jpg", use_column_width="always")

    with col3:
        st.image("img/ico_med.jpg", use_column_width="always")

    col1, col2, col3 = st.columns(3)
    with col1:

        interet = st.button("INTERES")
    with col2:

        pub = st.button("PUBLICATIONS")
    with col3:

        med = st.button("MEDIAS")

    if comp:
        competences_page(data=TOOLS_DICT)

    elif formation:
        formations_page()

    elif exp:
        experience_page(EXP_DICT)

    elif interet:
        interets_page()

    elif pub:
        publis_page()

    elif med:
        medias_page()

    # st.button("COMPETENCE", on_click=competences_page(data=TOOLS_DICT))
