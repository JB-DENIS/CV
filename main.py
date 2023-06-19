
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from experience import NewExperience


# Chargement des images :

img_size = (150, 150)
icone_img = Image.open('img/profil.jpg')
profil_img = Image.open('img/profils2.png')
bar_img = Image.open('img/bar.jpg')

comp_duo = Image.open('img/comp_duo.jpg')
comp_ico = Image.open('img/comp_ico.jpg')

form_road = Image.open('img/form_road2.jpg')

exp_data = Image.open('img/exp_data.jpg').resize(img_size)
exp_chimie = Image.open('img/exp_chimie.jpg').resize(img_size)
exp_open = Image.open('img/exp_open.jpg').resize(img_size)
exp_data_oc = Image.open('img/exp_data_oc.jpg').resize((240, 180))
exp_sc_broyeur = Image.open('img/exp_sc_broy.jpg').resize(img_size)
exp_sc_four = Image.open('img/exp_sc_four.jpg').resize(img_size)
exp_sc_laser = Image.open('img/exp_sc_laser.jpg')
exp_sc_bat = Image.open('img/exp_sc_bat.jpg')
exp_sc_enz = Image.open('img/exp_sc_enz.jpg').resize((40, 80))
exp_diver_maison = Image.open('img/exp_diver_maison.jpg')
exp_diver_cart = Image.open('img/exp_diver_cart.jpg').resize(img_size)
exp_diver_jap = Image.open('img/exp_diver_jap.jpg')

interet_mot = Image.open('img/interet_mot.jpg')

publi_brevet = Image.open('img/publi_brevet.jpg')
publi_poster = Image.open('img/publi_poster.jpg')
publi_these = Image.open('img/publi_these.jpg')
publi_prix = Image.open('img/publi_prix.jpg')

media_cv = Image.open('img/media_cv2.jpg')
media_lm = Image.open('img/media_lm.jpg')
media_lr = Image.open('img/media_lr.jpg')
media_git = Image.open('img/media_git.jpg')
media_linkedin = Image.open('img/media_linkedin.jpg')

glob_comp = Image.open('img/glob_comp2.jpg')
glob_int = Image.open('img/glob_int.jpg')
glob_exp = Image.open('img/glob_exp.jpg')
glob_form = Image.open('img/glob_form.jpg')
glob_kw2 = Image.open('img/glob_kw3.jpg')

media_yt_f = open('video/YT.mp4', 'rb')
media_yt = media_yt_f.read()


# Display :
st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
st.sidebar.image(profil_img, width=220)
st.sidebar.title('Jean-Benoît DENIS, Ph.D')
st.sidebar.subheader("Data Scientist - Ingénieur")

st.sidebar.image(bar_img, use_column_width=True)
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
st.sidebar.image(bar_img, use_column_width=True)


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

EXP_APPR_DATA = {
    "title": "Apprenti Data Scientist",
    "date": "2020-2021",
    "context": "La volonté de partir en formation Data Scientist vient du constat, fait lors de mes diverses expériences professionnelles, que les datas ont investi tous les cœurs de métier. La pertinence et la puissance d’utiliser ces datas pour comprendre et prédire des comportements sont apparues comme une suite logique à mon parcours professionnel et ainsi acquérir un nouvel outil polyvalent.",
    "missions": {
        "resume": "La formation se décline sous forme de 7 projets professionnels utilisant des données terrain. L’environnement mis en place pour ces projets est le language Python et la méthodologie de travail appliquée est la méthode S.M.A.R.T.",
        "examples": {
            "Anticipation de la consommation et des émissions de bâtiments": "Utiliser des données recueillies auprès d’immeubles de nouvelle génération afin de modéliser et prédire les consommations énergétiques et émissions de gaz à effet de serres en fonction du type de bâtiment.",
            "Segmentation des clients d'un site d'e-commerce": "Réaliser un clustering d’utilisateurs d’un site d’e-commerce afin d’établir des actions commerciales ciblées.",
            "Classification automatique de biens de consommation": "Mise en place d’un outil de classification automatique de produits de consommation en fonction de leurs descriptifs (texte) et de leurs photos (visuel).",
            "Implémentation d’une métrique métier pour le secteur bancaire": "Construire une métrique métier pour la modélisation d’un score d’attribution de prêt bancaire, interprétation sur Dashboard et déploiement de l'API."
        }
    },
    "realisations": ["Data Mining, Etude statistique",
                     "Pre-processing, feature engineering, réduction dimensionnelle (ACP)",
                     "Machine learning supervisé : régression, kNN, SVM, Random Forest, XGBoost, LightGBM",
                     "Machine learning non supervisé : Kmeans, DBScan, HAC, GMM",
                     "Métrique métier, optimisation bayésienne, stacking",
                     "Deep Learning, NLP (BoW, Tf-IDF, Embedding), visuel (BoVW, CNN, Transfert learning)",
                     "Spark, AWS",
                     "Déploiement API, Dashboard",
                     "Analyse de résultats, reporting et vulgarisation",
                     "GitHub rassemblant tous les projets"
                     ],
    "picture": "img/exp_data_oc.jpg"
}
exp_app_data = NewExperience(**EXP_APPR_DATA)

exp_app_data._template_col()
