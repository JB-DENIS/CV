import streamlit as st


class NewExperience():
    def __init__(self,
                 title: str,
                 date: str,
                 context: str,
                 missions: dict,
                 realisations: list,
                 picture: str
                 ):

        self.title = title
        self.date = date
        self.context = context
        self.missions = missions
        self.realisation = realisations
        self.picture = picture

    def _template_col(self):
        exp = st.container()
        with st.expander(label=self.title):
            # Title
            col1, col2, col3 = st.columns(3)
            col1.header(self.title)
            col3.header(self.date)

            # Context
            col1, col2, col3 = st.columns((2, 0.5, 1))
            col1.subheader("Contexte")
            col1.write(self.context)
            col3.image(self.picture)

            # Mission
