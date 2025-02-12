import streamlit as st


class NewExperience:
    def __init__(
        self,
        title: str,
        subtitle: str,
        date: str,
        context: str,
        missions: dict,
        realisations: list,
        picture: str,
    ):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.context = context
        self.missions = missions
        self.realisations = realisations
        self.picture = picture

    def _render_missions(self):
        """Affiche les missions sous un format structuré."""
        if not self.missions.get("examples"):
            return

        col1, col2 = st.columns(2)
        col1.subheader("Missions")
        st.markdown(
            f'<div style="text-align: justify;">{self.missions.get("resume")}</div>',
            unsafe_allow_html=True,
        )
        st.text("")

        col1, _, col2 = st.columns((1, 0.2, 1))
        for i, (mission, description) in enumerate(
            self.missions.get("examples").items()
        ):
            target_col = col1 if i % 2 == 0 else col2
            target_col.write(f"**_{mission}_**")
            target_col.markdown(
                f'<div style="text-align: justify;">{description}</div>',
                unsafe_allow_html=True,
            )
            target_col.text("")

    def _render_realisations(self):
        """Affiche les réalisations sous forme de liste."""
        st.subheader("Réalisations")
        for realisation in self.realisations:
            st.write(f":black_small_square: {realisation}")

    def render(self):
        """Affiche l'expérience avec son template."""
        with st.expander(label=f"**{self.title}**"):
            col1, _, col3 = st.columns((2, 0.8, 1))
            col1.header(self.title)
            col3.header(self.date)
            st.subheader(f"_{self.subtitle}_")

            # Contexte
            col1, _, col3 = st.columns((2, 0.2, 1))
            col1.subheader("Contexte")
            col1.markdown(
                f'<div style="text-align: justify;">{self.context}</div>',
                unsafe_allow_html=True,
            )
            if self.picture:
                col3.image(self.picture, use_container_width=True)

            st.text("")
            # Missions
            self._render_missions()
            st.text("")

            # Réalisations
            self._render_realisations()


def experience_page(exp: dict):
    """Affiche la page des expériences."""
    st.header("EXPÉRIENCES")
    st.text("")

    # Section d'aperçu
    col1, col2, col3 = st.columns(3)
    col1.image("img/exp_data.jpg")  # , width=200)
    col2.image("img/exp_chimie.jpg")  # , width=200)
    col3.image("img/exp_open.jpg")  # , width=200)
    st.text("")
    st.markdown(
        "<h6 style='text-align: center; color: gray;'>Choisissez une catégorie</h6>",
        unsafe_allow_html=True,
    )

    # Onglets pour les catégories
    tab1, tab2, tab3 = st.tabs(["IA", "Sciences", "Projets personnels"])

    # Affichage des expériences dans les onglets correspondants
    categories = {
        "IA": tab1,
        "Science": tab2,
        "Diverses": tab3,
    }

    for key, value in exp.items():
        type_exp = value.get("type_exp")
        if type_exp in categories:
            with categories[type_exp]:
                NewExperience(**value.get("body")).render()
