import streamlit as st
from database.champions import top_champions

st.set_page_config(
    page_title="Lol Stats",
    page_icon="https://i.imgur.com/7ZKdi2h.jpeg",
    layout="wide",
)

st.title("Lol Stats")

with open("styles/main.css", "r") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

with st.container(border=True):
    containers = st.columns((4, 4, 4))
    with containers[0]:
        lanes = ["Top", "Jungle", "Mid", "Adc", "Sup"]
        tabs = st.tabs(lanes)

        for tab, lane in zip(tabs, lanes):
            champions = top_champions(lane)
            tab.dataframe(
                champions,
                hide_index=True,
                column_config={
                    "count": st.column_config.ProgressColumn(
                        label="Partidas",
                        max_value=int(champions["count"].sum()) / 2,
                        min_value=1,
                        format="%f",
                    ),
                    "icon": st.column_config.ImageColumn(label=""),
                },
            )
