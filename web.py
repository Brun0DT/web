import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datasets
data_01 = pd.read_csv("UNI_CORR_500_01_modificado.txt", sep="\t")
data_06 = pd.read_csv("UNI_CORR_500_06_modificado.txt", sep="\t")

# Widget para seleccionar el dataset
dataset_seleccionado = st.sidebar.selectbox("Seleccionar dataset", {
    "Dataset 01": "Dataset 01",
    "Dataset 06": "Dataset 06"
})

# Elegir el dataset correspondiente
if dataset_seleccionado == "Dataset 01":
    data = data_01
else:
    data = data_06

with st.sidebar:
    # Título
    st.write("# Opciones")
    # Slider
    div = st.slider('Número de bins:', 0, 130, 25)
    st.write("Bins=", div)
st.title("Experimentacion sobre la dinamica peatonal ")
st.write("""
El presente problema se enmarca en un experimento que busca analizar cómo la densidad de las personas y el ancho de las puertas afectan en el tiempo de evacuación en un corredor con dos accesos, correspondientes a puerta uno y puerta dos, en las cuales además se presenta una simetría entre los lados de salida y entrada realizando una gran cantidad de carreras. Ahora bien, el análisis tendrá en cuenta una carrera, la cuales tendrán una dirección de derecha a izquierda con medidas de entradas y salidas de uno a cinco metros.
""")
st.title("Graficos de histograma, dispersion y boxplot")
# Resto del código para generar los gráficos y estadísticas
# ...
tabla_experimento1=data[["# PersID","Velocidad"]].groupby("# PersID").agg(np.mean)

sk = data['sk']
velocidad = data['Velocidad']
# Histograma
fig, ax = plt.subplots()
ax.hist(tabla_experimento1, bins=div, color='green', edgecolor='black')
ax.set_xlabel('Velocidad')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Velocidad experimento 1', loc='center')
st.pyplot(fig)

# Scatter Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(sk, velocidad, alpha=0.5)
ax.set_title('Scatter Plot entre sk y Velocidad')
ax.set_xlabel('sk')
ax.set_ylabel('Velocidad')
ax.grid(True)
st.write("Nota: Velocidad en unidad de medida metros/segundo.")
st.pyplot(fig)
st.write("""Nota: El sk es calculado en base a las personas cercanas en un radio de 3 metros.
""")
# Boxplot
fig, ax = plt.subplots()
ax.boxplot([data[(data["# PersID"] == i)]["Velocidad"] for i in range(1, 11)])
ax.set_xlabel('Personas')
ax.set_ylabel('Velocidad')
ax.set_title('Boxplot por persona experimento 01', loc='center')
st.pyplot(fig)
st.write("Nota: El grafico corresponde a las primeras 10 personas en la experimentacion.")

# Estadísticas
st.title("Estadisticas obtenidas sobre SK")
st.table(data["sk"].describe())
st.title("Estadisticas obtenidas sobre velocidad")
st.table(data["Velocidad"].describe())