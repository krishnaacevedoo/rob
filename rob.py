import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Rob Page",
    page_icon=":microphone:",
    layout="wide"
)

# Página principal (Home)
st.title(":monocle: Bienvenidos al sitio de Rob")

st.write(
    "Este sitio está dedicado a la trayectoria y logros de *Robleis*, "
    "uno de los músicos y creadores de contenido más influyentes de Latinoamérica."
)

# Imagen de portada
st.image("robleisportada.jpg", caption="Rob en concierto", use_container_width=True)

# Separador
st.markdown("---")

# Sección: ¿Qué encontrarás?
st.subheader("¿Qué encontrarás en este sitio?")
st.write(
    "- Su historia y primeros pasos\n"
    "- Su carrera como creador de contenido\n"
    "- Su trayectoria musical\n"
    "- La comunidad y fandom que lo sigue"
)

# GIF o imagen de presentación
st.image("gifsrobleiss.gif", caption="Momentos destacados de Robleis")


