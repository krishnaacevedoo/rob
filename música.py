import streamlit as st

# Título de la página
st.title(":loop: Música de Rob")

# Descripción
st.write("Además de su carrera como creador de contenido, Robleis se ha lanzado como cantante, con temas que mezclan pop y urbano.")

# Menú de selección de canción
opción = st.selectbox("Elige tu canción favorita:", ["solo", "una noche más"])

# Mostrar la canción elegida
st.write(f"Elegiste: {opción}")

# Mostrar el video correspondiente
if opción == "solo":
    st.video("https://youtu.be/5ImpOnAzSo4?si=vtFJBQCgHV60a498")
elif opción == "una noche más":
    st.video("https://youtu.be/GpFoGiscj7k?si=0Q30240lIzQu2mnQ")
