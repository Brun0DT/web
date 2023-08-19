import streamlit as st

#--------------------------------------------------------------------------------------------------------------------

import pandas as pd    ;import numpy as np          ;  import matplotlib.pyplot as plt    
pd.set_option('mode.chained_assignment', None)
from scipy.spatial import KDTree  

# inicio_memoria = psutil.virtual_memory().used   

# tiempo_inicio=time.time()

data=pd.read_csv("UNI_CORR_500_01.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado
data["sk"]=0

#--------------------------------------------------------------------------------------------------------------------

#Velocidad primer txt
def Obtener_velocidad(datax):
    return (((datax["X"].diff(periods=1))**2+(datax["Y"].diff(periods=1))**2)**(1/2))/(1/25)

Dataframe_velocidades = data.groupby("# PersID").apply(Obtener_velocidad) #dataframe_velocidad se convirtio en una serie

data["Velocidad"]=Dataframe_velocidades.values #agrego la serie que tiene propiedad index y value al dataframe original
#en este caso values contiene un total de las filas de datos

#--------------------------------------------------------------------------------------------------------------------

def Encontrar_coordenada_vecina():

    data_filtrado["indice matriz"] = [i for i in range(len(data_filtrado))]

    for indice in data_filtrado["indice matriz"].values:
        
        Coordenda_a_evaluar=Coordenadas_X_Y[indice] #coordenadas del peaton de interes, usare siempre el primero del dataframe entregado

        indice_vecino=arbol.query_ball_point(Coordenda_a_evaluar,3.0) #entrega los indices de la matriz, es decir 0 1 2 3 4 5

        indice_vecino=[index for index in indice_vecino if index!=indice] #todos los indices menos el de referencia
        
        #agrego la lista de indices que tendra la matriz
        indices_filtrados = data_filtrado.index[data_filtrado["indice matriz"]==indice].values #obtener indice del dataframe original donde agregar
        #el valor del sk , entrega la fila del idpersona 18 en el frame 10 por ejemplo

        if len(indice_vecino):
            #calculo de la distancia
            distances, indices = arbol.query(Coordenda_a_evaluar, k=len(indice_vecino)+1)
            inicial=distances[0]
            # Calcular la media de las distancias excluyendo 'inicial'
            distances_sin_inicial = [i for i in distances if i != inicial]
            media_distancias = np.mean(distances_sin_inicial)
            data["sk"].loc[(indices_filtrados[0])]= media_distancias

#--------------------------------------------------------------------------------------------------------------------

for frame in data["Frame"]:

    data_filtrado=data[data["Frame"]==frame].copy() #filtro de data por el frame que se encuentre en el for, .copy para no alterar al dataframe original
    #cuando agregue los indices de la matriz
    Coordenadas_X_Y=data_filtrado[["X","Y"]].values #creo matriz con valores x e y del dataframe filtrado cada fila es una coordenada xy por persona
    arbol=KDTree(Coordenadas_X_Y) #crea arbol con opciones
    Encontrar_coordenada_vecina()

#hacer scarter plot sf en y velocidad en el y
# print(data["sk"].mean())

#--------------------------------------------------------------------------------------------------------------------
st.write("""
#Analisis de velocidad con Sk
""")
tabla_experimento1=Dataframe_velocidades.groupby("# PersID").agg(np.mean)
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

fig, ax = plt.subplots()
plt.figure(figsize=(10, 6))
plt.scatter(sk,velocidad)  # alpha controla la transparencia de los puntos
plt.title('Scatter Plot entre sk y Velocidad')
plt.xlabel('sk')
plt.ylabel('Velocidad')
plt.grid(True)
# Desplegamos el gráfico
st.pyplot(fig)
# fin_memoria = psutil.virtual_memory().used;           fin_tiempo = time.time()
# # plt.show()
# # plt.show()
# tiempo_transcurrido = fin_tiempo - tiempo_inicio
# print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")
# memoria_utilizada = fin_memoria - inicio_memoria
# print("Memoria utilizada: ", memoria_utilizada/ (1048576)," MB")
# Using "with" notation
with st.sidebar:
    # Titulo
    st.write("# Opciones")
    # slider
    div = st.slider('Número de bins:', 0, 130, 25)
    st.write("Bins=", div)

st.write("""
## Bases de datos
""")

st.title("Abrir Archivo desde URL")

import webbrowser

st.title("Archivo del experimento numero ")

# Define la ruta del archivo de texto
ruta_archivo = "UNI_CORR_500_01.txt"

# Botón para abrir el archivo en una nueva pestaña
if st.button("Abrir Archivo"):
    nueva_url = f"data:text/plain;base64,{open(ruta_archivo).read()}"
    webbrowser.open_new_tab(nueva_url)