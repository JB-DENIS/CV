
import streamlit as st
from acceuil import accueille_page
from competences import competences_page
from data_dict import COMP_DICT, EXP_DICT, SOFT_LIST, TOOLS_DICT
from experience import experience_page
from formations import formations_page
from interets import interets_page
from medias import medias_page
from publications import publis_page


def catego(option):

    if option == 'Accueil':
        accueille_page()

    elif option == 'Compétences':
        competences_page(
            data_tools=TOOLS_DICT,
            data_comp=COMP_DICT,
            data_soft=SOFT_LIST
        )

    elif option == 'Formations':
        formations_page()

    elif option == 'Expériences':
        experience_page(EXP_DICT)

    elif option == 'Intérêts':
        interets_page()

    elif option == 'Publications':
        publis_page()

    elif option == 'Médias':
        medias_page()


# Display :
st.set_page_config(page_title='CV JB DENIS',
                   layout="wide",
                   page_icon="img/profil.jpg")
st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
st.sidebar.image("img/profils2.png", width=220)
st.sidebar.title('Jean-Benoît DENIS, Ph.D')
st.sidebar.subheader("Ingénieur Data Scientice")

st.sidebar.image('img/bar.jpg', use_column_width=True)
st.sidebar.markdown(
    "<h1 style='text-align: center; color: blue;'>Navigation</h1>", unsafe_allow_html=True)
option = st.sidebar.selectbox('', ['Accueil',
                                   'Compétences',
                                   'Formations',
                                   'Expériences',
                                   'Intérêts',
                                   'Publications',
                                   'Médias'
                                   ])
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.image('img/bar.jpg', use_column_width=True)


# st.sidebar.write('31 ans - Permis B')
st.sidebar.write(':telephone_receiver: 06 29 07 69 72')
st.sidebar.write(
    ':e-mail: [jeanbenoitdenis@gmail.com](mailto:jeanbenoitdenis@gmail.com)')
st.sidebar.write(
    ':round_pushpin:[4 Rue Hector Blanchet 38500 Voiron](https://goo.gl/maps/E8iCnmAg6AetDBy76)')


st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {2560}px;
        padding-top: {0}rem;
        padding-right: {5}rem;
        padding-left: {5}rem;
        padding-bottom: {0}rem;
    }}
    .reportview-container .main {{
        color: {'black'};
        background-color: {'white'};
    }}
</style>
""",
    unsafe_allow_html=True,
)

# Pages
catego(option)
