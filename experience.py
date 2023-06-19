import streamlit as st


class NewExperience():
    def __init__(self,
                 title: str,
                 subtitle: str,
                 date: str,
                 context: str,
                 missions: dict,
                 realisations: list,
                 picture: str
                 ):

        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.context = context
        self.missions = missions
        self.realisation = realisations
        self.picture = picture

    def _template_col(self):
        # exp = st.container()
        with st.expander(label=f"**{self.title}**"):
            # Title
            col1, col2, col3 = st.columns((2, 0.5, 1))
            col1.header(self.title)
            col3.header(self.date)
            st.subheader(f"_{self.subtitle}_")

            # Context
            col1, col3 = st.columns((2, 1))
            col1.subheader("Contexte")
            col1.markdown(
                f'<div style="text-align: justify;">{self.context}<div>', unsafe_allow_html=True)
            col3.text("")
            col3.text("")
            col3.text("")
            col3.text("")
            col3.image(self.picture, use_column_width='auto')
            st.text("")
            # Mission

            if self.missions.get("examples"):
                col1, col2 = st.columns(2)
                col1.subheader("Missions")
                st.markdown(
                    f'<div style="text-align: justify;">{self.missions.get("resume")}<div>', unsafe_allow_html=True)
                st.text("")
                col1, col2 = st.columns(2)
                n = 0
                for k, v in self.missions.get("examples").items():

                    if (n % 2) == 0:
                        col1, col2 = st.columns(2)
                        col1.write(f"**_{k}_**")
                        col1.markdown(
                            f'<div style="text-align: justify;">{v}<div>', unsafe_allow_html=True)
                        col1.text("")
                    else:
                        col2.write(f"_**{k}**_")
                        col2.markdown(
                            f'<div style="text-align: justify;">{v}<div>', unsafe_allow_html=True)
                        col2.text("")

                    n += 1
                st.text("")
            # Realisations
            st.subheader('Réalisations')
            for r in self.realisation:

                st.write(f":black_small_square: {r}")


def experience_page(exp: dict):

    st.header("EXPERIENCES")
    st.text("")
    col1, col2, col3 = st.columns(3)
    col1.image("img/exp_data.jpg", width=200)
    col2.image("img/exp_chimie.jpg", width=200)
    col3.image("img/exp_open.jpg", width=200)
    st.text("")
    st.markdown("<h6 style='text-align: center; color: gray;'>Choisissez une catégorie</h5>",
                unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(
        ["Data", "Science", "Diverses"])

    for k, v in exp.items():

        if v.get("type_exp") == "Data":
            with tab1:
                NewExperience(**v.get("body"))._template_col()

        if v.get("type_exp") == "Science":
            with tab2:
                NewExperience(**v.get("body"))._template_col()

        if v.get("type_exp") == "Diverses":
            with tab3:
                NewExperience(**v.get("body"))._template_col()
