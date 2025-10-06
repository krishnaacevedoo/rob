# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="page rob",
    page_icon=":yellow_heart:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo
st.logo(
    "logo_content.png",
)

pg = st.navigation(["rob.py", "historia.py", "carrera.py", "música.py", "fandom.py", "quienes somos.py"])
pg.run()