import streamlit as st


def publis_page():
    st.markdown("""<a id="top"></a>""", unsafe_allow_html=True)
    st.header('Publications')
    st.text('')
    br = ('[**Brevet**](https://drive.google.com/file/d/1RZVpIPAJiq4zO9LPjO2_ahqiKJrSqQ2A/view?usp=sharing)')
    po = ('[**Poster**](https://drive.google.com/file/d/1btDY31nkJ-ycOGMaT_ar9SBzTMzDSllW/view?usp=sharing)')
    th = ('[**Thèse**](https://drive.google.com/file/d/1-OMgCIu-agnUHLJW8uUhvnJHNP_fdg7t/view?usp=sharing)')
    pr = ('[**Présentation Thèse**](https://drive.google.com/file/d/143D5-Euw0HwPIUcxHw49HVQ_j2J1KKZM/view?usp=sharing)')

    st.markdown("<h6 style='text-align: center; color: gray;'>Cliquez sur un lien pour accéder au contenu</h5>",
                unsafe_allow_html=True)
    st.text('')
    st.text('')

    # col4, col5, col6,col7,col8 = st.columns(5)
    col4, col5, col6, col7, col8, col9, col10 = st.columns(
        (0.5, 1, 0.5, 1, 0.5, 1, 0.5))  # ((0.6,1,0.9,1,0.9,1,0.9,1,0.0001))
    col5.image('img/publi_brevet.jpg', use_column_width=True)
    col7.image('img/publi_poster.jpg', use_column_width=True)
    col9.image('img/publi_these.jpg', use_column_width=True)

    col4, col5, col6, col7, col8, col9, col10 = st.columns(
        (0.5, 1, 0.5, 1, 0.5, 1, 0.5))  # ((0.6,1,0.9,1,0.9,1,0.9,1,0.0001))
    col5.write(br, unsafe_allow_html=True)
    col7.write(po, unsafe_allow_html=True)
    col9.write(th, unsafe_allow_html=True)
    col5.write('_Polymère comme matériau d\'électrode pour des batteries secondaires au lithium._ Réf : **WO 2013156899 A1**')
    col7.write(
        '_Influence of impurities on the performance of metal hydride_. MH2014, Manchester, UK, 2014.')
    col9.write('_Étude de l\'influence d\'éléments d\'addition sur les propriétés de stockage de l\'hydrogène dans le système Ti-V-Fe._')

    st.text('')
    st.text('')
    st.text('')
    st.text('')
    col1, col2, col3 = st.columns(3)
    col2.image('img/publi_prix.jpg', use_column_width=True)  # width=220)
    col2.write(pr)
    col2.write('1er prix : _Présentation Thèse CEA_, organisé au Liten')
    st.text('')
    st.text('')
