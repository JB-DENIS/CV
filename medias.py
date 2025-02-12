import streamlit as st
from PIL import Image


def load_images():
    """Charge toutes les images utilisées dans la page."""
    return {
        "cv": Image.open("img/media_cv2.jpg"),
        "lm": Image.open("img/media_lm.jpg"),
        "lr": Image.open("img/media_lr.jpg"),
        "git": Image.open("img/media_git.jpg"),
        "linkedin": Image.open("img/media_linkedin.jpg"),
        "podcast": Image.open("img/podcast.jpg"),
        "article": Image.open("img/article.jpg"),
        "interview": Image.open("img/interview.jpg"),
        "dojo": Image.open("img/exp_dojo.png"),
        "automl": Image.open("img/exp_automl.jpg"),
    }


def load_media_links():
    """Charge tous les liens médias."""
    return {
        "cv": "[**CV**](https://drive.google.com/file/d/124jtZ2eEXIskv2kQeBIS00vXFeShkmDz/view?usp=sharing)",
        "lm": "[**Lettre de motivation**](https://drive.google.com/file/d/1hpbAiw7URmtNtQo_BdIHHOX12_Zpb3GC/view?usp=sharing)",
        "lr": "[**Lettre de recommandation**](https://drive.google.com/file/d/1UoU_yFMkkjtdxRiluyNAN9NfIWck2mOk/view?usp=sharing)",
        "git": "[**GitHub**](https://github.com/JB-DENIS)",
        "linkedin": "[**LinkedIn**](https://www.linkedin.com/in/jbdenis/)",
        "yt": "[**YouTube**](https://www.youtube.com/channel/UC1i8IXzTvu7rhaXBCLMaDmQ)",
        "podcast": "[**Podcast**](https://youtube.com/playlist?list=PL0WJ6NGo78mzYH8U5NLUURHqR0vP5W0tm&si=djAVcOaWj9BCpo4g)",
        "article": "[**Article IA Générative**](https://kaizen-solutions.net/kaizen-insights/articles-et-conseils-de-nos-experts/7-conseils-pour-utiliser-efficacement-les-ia-generatives/)",
        "interview": "[**Interview IA**](https://intelligence-artificielle.com/expert-i-a-jean-benoit-denis-kaizen-solutions/)",
        "dojo": "[**Atelier Machine learning**](https://github.com/JB-DENIS/atelier_ML/blob/main/data_dojo.ipynb)",
        "automl": "[**Auto-Data**](https://github.com/JB-DENIS/auto-ML)",
    }


def display_media_row(columns, images, links):
    """Affiche une rangée de médias avec leurs images et leurs liens."""
    for col, (key, img) in zip(columns, images.items()):
        col.image(img.resize((125, 150)), use_container_width=True)
        col.markdown(links[key], unsafe_allow_html=True)


def medias_page():
    st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
    st.header("Médias")
    st.markdown(
        "<h6 style='text-align: center; color: gray;'>Cliquez sur un média pour accéder au contenu</h6>",
        unsafe_allow_html=True,
    )
    st.text("")

    images = load_images()
    links = load_media_links()

    # Première ligne
    cols = st.columns((0.5, 1, 0.5, 1, 0.5, 1, 0.5))
    display_media_row(
        [cols[1], cols[3], cols[5]], {k: images[k] for k in ["cv", "lm", "lr"]}, links
    )

    st.text("")

    # Deuxième ligne
    cols = st.columns(
        1, 1, 1, 1, 1, 1, 1, 1, 1
    )  # (1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1))
    display_media_row(
        [cols[i] for i in range(1, 8)],
        {
            k: images[k]
            for k in [
                "linkedin",
                "git",
                "podcast",
                "article",
                "interview",
                "dojo",
                "automl",
            ]
        },
        links,
    )

    st.text("")
    st.markdown(
        "<h6 style='text-align: center; color: gray;'>Attention, le son est automatiquement au maximum</h6>",
        unsafe_allow_html=True,
    )

    # Vidéo
    with open("video/YT.mp4", "rb") as media_yt_f:
        media_yt = media_yt_f.read()
    st.video(media_yt)

    # Lien YouTube
    col1, col2, col3 = st.columns((4, 1, 4))
    col2.markdown(links["yt"], unsafe_allow_html=True)
