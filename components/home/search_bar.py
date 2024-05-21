import streamlit as st

from utils.regions import REGIONS


def search_summoner_bar():
    columns = st.columns((4, 1))

    summoner = columns[0].text_input(label="Username", placeholder="shadyzled006#faker")
    server = columns[1].selectbox(label="Selecione o servidor", options=["BR1"])

    button = st.columns((4, 4, 1))[0].button(label="Pesquisar")

    if button:
        game_name, tag_line = summoner.split("#")
        region = REGIONS.get(server)

        st.write(game_name)
        st.write(tag_line)
        st.write(region)
