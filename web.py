import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

    
st.write("""
# Mi primera aplicación interactiva
## Histograma sobre el eje X e Y
""")
# Using "with" notation
with st.sidebar:
    # Titulo
    st.write("# Opciones")
    # slider
    div = st.slider('Número de bins:', 0, 130, 25)
    st.write("Bins=", div)

