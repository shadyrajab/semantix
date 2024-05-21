import streamlit as st


def search_summoner_bar():
    columns = st.columns((4, 1))

    summoner = columns[0].text_input(label="Username", placeholder="shadyzled006#faker")
    server = columns[1].selectbox(label="Selecione o servidor", options=["BR1"])
    
    st.session_state.summoner = summoner
    st.session_state.server = server
