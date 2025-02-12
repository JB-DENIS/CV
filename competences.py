import streamlit as st
import pandas as pd
import plotly.express as px

pd.options.plotting.backend = "plotly"


def create_tools_chart(data_tools: dict):
    """Crée un graphique en barres horizontales pour les outils."""
    df = pd.DataFrame(
        {"Tool": list(data_tools.keys()), "Score": list(data_tools.values())}
    )

    fig = px.bar(
        df,
        x="Score",
        y="Tool",
        orientation="h",
        color="Tool",
        color_continuous_scale="reds",
    )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False, showticklabels=False),
        yaxis_title=None,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    return fig


def create_competences_chart(data_comp: dict):
    """Crée un graphique Sunburst pour les compétences."""
    fig = px.sunburst(data_comp, names="character", parents="parent", values="value")

    fig.update_layout(margin=dict(l=5, r=5, t=5, b=5))

    return fig


def competences_page(data_tools: dict, data_comp: dict, data_soft: list):
    """Affiche la page des compétences."""
    st.header("COMPÉTENCES")
    st.text("")

    # Création des graphiques
    fig_tools = create_tools_chart(data_tools)
    fig_comp = create_competences_chart(data_comp)

    # Affichage des graphiques et images dans des colonnes
    col1, _, col2 = st.columns((1.5, 0.1, 1))

    with col1:
        st.plotly_chart(fig_tools, use_container_width=True)
        st.image("img/comp_soft.jpg", caption="Compétences Soft Skills")

    with col2:
        st.image("img/comp_lang.jpg", caption="Langages de Programmation")
        st.plotly_chart(fig_comp, use_container_width=True)
