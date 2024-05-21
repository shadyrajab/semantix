import streamlit as st

from components.home.summoner import search_summoner_bar

st.set_page_config(
    page_title="Lol Stats",
    page_icon="https://i.imgur.com/7ZKdi2h.jpeg",
    layout="centered",
)

with open("styles/main.css", "r") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

search_summoner_bar()