#cada ambiente parte vacio
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("UNI_CORR_500_01.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado 
data["xpixel"]=round((data["X"])*35.6)+320
data["ypixel"]=round(data["Y"]*(-96))+480
fig, ax=plt.subplots()
ax.hist2d(data["xpixel"],data["ypixel"],bins=(60,50),cmap="inferno")
ax.set_title('Mapa de calor experimento 1', loc = "center")
ax.set_xlabel("Largo pasillo")
ax.set_ylabel("Ancho pasillo")

st.pyplot(fig)
