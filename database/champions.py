from database.database import DATAFRAME
import pandas as pd


def top_champions(lane: str):
    top_champions = pd.DataFrame(
        pd.concat(
            [
                DATAFRAME[f"blue_{lane.lower()}_champion"],
                DATAFRAME[f"red_{lane.lower()}_champion"],
            ]
        ).value_counts()
    ).reset_index(names="Campeão")[0:5]

    icon_url = "https://ddragon.leagueoflegends.com/cdn/14.10.1/img/champion/{}.png"
    top_champions["icon"] = top_champions["Campeão"].apply(lambda x: icon_url.format(x))

    return top_champions[["icon", "Campeão", "count"]]
