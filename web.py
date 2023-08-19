import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("UNI_CORR_500_01.txt", 
                 skiprows=4, 
                 sep="\t", 
                 names=["ID", "frames", "X", "Y", "Z"])
    
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

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["X"], bins=div, color= "lightcoral")
ax[0].set_xlabel('Posición en metros')
ax[0].set_ylabel('Frecuencia')
ax[0].set_title('Histograma posiciónes en el eje X')

ax[1].hist(df["Y"], bins=div, color= "indianred")
ax[1].set_xlabel('Posición en metros')
ax[1].set_ylabel('Frecuencia')
ax[1].set_title('Histograma posiciónes en el eje Y')

# Desplegamos el gráfico
st.pyplot(fig)

st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())