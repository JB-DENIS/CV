import streamlit as st
from PIL import Image

media_cv = Image.open('img/media_cv2.jpg')
media_lm = Image.open('img/media_lm.jpg')
media_lr = Image.open('img/media_lr.jpg')
media_git = Image.open('img/media_git.jpg')
media_linkedin = Image.open('img/media_linkedin.jpg')

media_yt_f = open('video/YT.mp4', 'rb')
media_yt = media_yt_f.read()


def medias_page():
    st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
    st.header('Médias')
    st.text('')

    cv = ('[**CV**](https://drive.google.com/file/d/1oSBKeLdvIjgydBnC_t6o01fb9ucCaomL/view?usp=sharing)')
    lm = ('[**Lettre de motivation**](https://drive.google.com/file/d/1hpbAiw7URmtNtQo_BdIHHOX12_Zpb3GC/view?usp=sharing)')
    lr = ('[**Lettre de recommandation**](https://drive.google.com/file/d/1UoU_yFMkkjtdxRiluyNAN9NfIWck2mOk/view?usp=sharing)')
    git = ('[**GitHub**](https://github.com/JB-DENIS)')
    lin = ('[**LinkedIn**](https://linkedin.com/in/jean-benoît-denis-38000)')
    yt = ('[**YouTube**](https://www.youtube.com/channel/UC1i8IXzTvu7rhaXBCLMaDmQ)')
    nb_nutriscore = (
        '[**Atelier Data**](https://github.com/JB-DENIS/atelier_ML)')
    automl = ('[**Auto-Data**](https://github.com/JB-DENIS/auto-ML)')

    st.markdown("<h6 style='text-align: center; color: gray;'>Cliquez sur un média pour accéder au contenu</h5>",
                unsafe_allow_html=True)
    st.text('')
    st.text('')

    col4, col5, col6, col7, col8, col9, col10 = st.columns(
        (0.5, 1, 0.5, 1, 0.5, 1, 0.5))
    col5.image(media_cv.resize((125, 150)),
               use_column_width=True)  # ,width=125)
    col7.image(media_lm.resize((125, 150)),
               use_column_width=True)  # ,width=125)
    col9.image(media_lr.resize((125, 150)),
               use_column_width=True)  # ,width=125)

    # col4, col5, col6, col7, col8, col9, col10 = st.columns((0.5,1,0.5,1,0.5,1,0.5))
    col5.markdown(cv, unsafe_allow_html=True)
    col7.markdown(lm, unsafe_allow_html=True)
    col9.markdown(lr, unsafe_allow_html=True)

    st.text('')
    st.text('')

    col32, col4, col5, col6, col7, col33 = st.columns(
        (1, 0.5, 0.5, 0.5, 0.5, 1))
    col4.image(media_linkedin, use_column_width=True)
    col5.image(media_git, use_column_width=True)
    col6.image("img/exp_dojo.png", use_column_width=True)
    col7.image("img/exp_automl.jpg")  # , use_column_width=True)

    # col4, col5, col6, col7, col8= st.columns((1,0.5,1,0.5,1))
    col4.markdown(lin, unsafe_allow_html=True)
    col5.markdown(git, unsafe_allow_html=True)
    col6.markdown(nb_nutriscore, unsafe_allow_html=True)
    col7.markdown(automl, unsafe_allow_html=True)

    st.text('')
    st.text('')
    st.markdown("<h6 style='text-align: center; color: gray;'>Attention, le son est automatiquement au maximum</h5>", unsafe_allow_html=True)
    st.video(media_yt)
    col1, col2, col3 = st.columns((4, 1, 4))
    col2.markdown(yt, unsafe_allow_html=True)
