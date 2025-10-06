import streamlit as st  # Importar la librería Streamlit

# Título de la página
st.title(":relaxed: ¿Quiénes somos?")

# Descripción del grupo
st.write("Somos un grupo ficticio que muestra la trayectoria de nuestro ídolo.")
st.write("Conformado por *Fulana* y *Floricienta*")  

# Imagen de Fulana
st.image("robl.jpg", caption="Fulana")

# Imagen de Floricienta
st.image("xs.jpg", caption="Floricienta")

# Audio final
st.audio("byee.mp3")  

