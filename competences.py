import streamlit as st
import pandas as pd
import plotly.express as px

pd.options.plotting.backend = "plotly"


def competences_page(data: dict):
    # st.markdown('<a id="top"></a>', unsafe_allow_html=True)
    st.header("COMPETENCES")
    st.text("")

    df = pd.DataFrame(data, index=["level"]).T

    df = pd.DataFrame(dict(
        y=[k for k in data.keys()],
        x=[v for v in data.values()]
    ))

    fig = px.bar(df,
                 x="x",
                 y="y",
                 orientation='h',
                 color="y",
                 color_continuous_scale="reds",
                 #  barmode='overlay'
                 )
    fig.layout.update(showlegend=False,
                      xaxis_visible=False,
                      xaxis_showticklabels=False,
                      yaxis_title=None
                      )
    st.markdown("<h6 style='text-align: center; color: gray;'>Choisissez une catégorie</h5>",
                unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Skills", "Tools"])

    with tab1:
        st.image('img/comp_duo.jpg')

    with tab2:
        st.plotly_chart(fig, use_container_width=True)

    # top_but = st.button('Retour haut de page')
    # if top_but:
    #     st.markdown("<a id='top'></a>", unsafe_allow_html=True)
