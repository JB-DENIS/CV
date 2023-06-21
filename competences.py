import streamlit as st
import pandas as pd
import plotly.express as px

pd.options.plotting.backend = "plotly"


def competences_page(data_tools: dict, data_comp: dict, data_soft: list):

    st.header("COMPETENCES")
    st.text("")

    df = pd.DataFrame(dict(
        y=[k for k in data_tools.keys()],
        x=[v for v in data_tools.values()]
    ))
    # TOOLS
    fig_tools = px.bar(df,
                       x="x",
                       y="y",
                       orientation='h',
                       color="y",
                       color_continuous_scale="reds",
                       #  barmode='overlay'
                       )
    fig_tools.layout.update(showlegend=False,
                            xaxis_visible=False,
                            xaxis_showticklabels=False,
                            yaxis_title=None,
                            # margin=dict(l=100, r=100, t=100, b=100)
                            )
    # COMPETENCES
    fig_comp = px.sunburst(
        data_comp,
        names='character',
        parents='parent',
        values='value'
    )
    fig_comp.update_layout(
        margin=dict(l=5, r=5, t=5, b=5)
    )

    col1, col15, col2 = st.columns((1.5, 0.1, 1))
    with col1:
        st.plotly_chart(fig_tools, use_container_width=True)
        st.image("img/comp_soft.jpg")
    with col2:
        st.image("img/comp_lang.jpg")
        st.plotly_chart(fig_comp, use_container_width=True)
