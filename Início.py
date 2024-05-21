import streamlit as st

from components.home.search_bar import search_summoner_bar

st.set_page_config(
    page_title="Lol Stats",
    page_icon="https://i.imgur.com/7ZKdi2h.jpeg",
    layout="wide",
)

with open("styles/main.css", "r") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

with st.container(border=True):
    search_summoner_bar()
