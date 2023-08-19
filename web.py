import streamlit as st

#--------------------------------------------------------------------------------------------------------------------

import pandas as pd    ;import numpy as np          ;  import matplotlib.pyplot as plt    
pd.set_option('mode.chained_assignment', None)
from scipy.spatial import KDTree  


data=pd.read_csv("UNI_CORR_500_01_modificado.txt",sep="\t") #names= cuando la tabla no tiene un encabezado
with st.sidebar:
    # Titulo
    st.write("# Opciones")
    # slider
    div = st.slider('Número de bins:', 0, 130, 25)
    st.write("Bins=", div)


#--------------------------------------------------------------------------------------------------------------------
st.title("Experimentacion sobre la dinamica peatonal ")
st.write("""
El presente problema se enmarca en un experimento que busca analizar cómo la densidad de las personas y el ancho de las puertas afectan en el tiempo de evacuación en un corredor con dos accesos, correspondientes a puerta uno y puerta dos, en las cuales además se presenta una simetría entre los lados de salida y entrada realizando una gran cantidad de carreras. Ahora bien, el análisis tendrá en cuenta una carrera, la cuales tendrán una dirección de derecha a izquierda con medidas de entradas y salidas de uno a cinco metros.
""")
st.title("Graficos de histograma y dispersion")
tabla_experimento1=data[["# PersID","Velocidad"]].groupby("# PersID").agg(np.mean)

fig, ax = plt.subplots()

ax.hist(tabla_experimento1,bins=15, color='green', edgecolor='black')
ax.set_xlabel('Velocidad')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Velocidad experimento 1', loc='center')
# Desplegamos el gráfico
st.pyplot(fig)


sk = data['sk']
velocidad = data['Velocidad']

data=data.dropna(subset=['Velocidad']) #elimino valores none

fig, ax = plt.subplots(figsize=(10, 6))  # Crear la figura y los ejes

# Configurar el gráfico de dispersión
ax.scatter(sk, velocidad, alpha=0.5)  # alpha controla la transparencia de los puntos
ax.set_title('Scatter Plot entre sk y Velocidad')  # Usar 'set_title' para establecer el título
ax.set_xlabel('sk')  # Usar 'set_xlabel' para establecer la etiqueta del eje X
ax.set_ylabel('Velocidad')  # Usar 'set_ylabel' para establecer la etiqueta del eje Y
ax.grid(True)  # Agregar una cuadrícula

# Desplegar el gráfico usando Streamlit
st.pyplot(fig)




st.title("Estadisticas obtenidas sobre SK")

# Graficamos una tabla
st.table(data["sk"].describe())
st.title("Estadisticas obtenidas sobre velocidad")
st.table(data["Velocidad"].describe())