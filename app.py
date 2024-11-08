import streamlit as st
import pydeck as pdk
from utils.database import fetch_murals

# Inicjalizacja bazy danych (przy pierwszym uruchomieniu)

# Ustawienia tytułu strony
st.set_page_config(page_title="Mapa Murali Warszawy", layout="wide")

# Nagłówek aplikacji
st.title("Mapa Murali Warszawy")

# Pobranie danych murali
murals_data  = fetch_murals()

# Sprawdzenie, czy dane zostały poprawnie załadowane
if murals_data.empty:
    st.warning("Brak murali w bazie danych.")
else:
    # Konfiguracja warstwy IconLayer z markerami
    murals_data["icon_data"] = {
        "url": "https://img.icons8.com/emoji/48/000000/round-pushpin-emoji.png",  # URL ikony markera
        "width": 128,
        "height": 128,
        "anchorY": 128
    }

    layer = pdk.Layer(
        "IconLayer",
        murals_data,
        get_position=["lon", "lat"],
        get_icon="icon_data",
        get_size=5,
        size_scale=15,
        pickable=True  # Dzięki temu ikony są "klikalne" i wyświetlają informacje
    )

    # Konfiguracja podglądu mapy
    view_state = pdk.ViewState(
        latitude=52.2297,  # Centralny punkt Warszawy
        longitude=21.0122,
        zoom=12,
        pitch=40,
    )

    # Konfiguracja okienka z informacjami (tooltip)
    tooltip = {
        "html": """
        <b>{name}</b><br>
        <img src="{image_url}" width="150"><br>
        <p>{description}</p>
        """,
        "style": {
            "backgroundColor": "steelblue",
            "color": "white",
            "font-family": "Arial",
            "padding": "10px"
        }
    }

    # Dodanie mapy do aplikacji Streamlit
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip  # Ustawienie tooltipa
    ))