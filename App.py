from PIL import Image
import streamlit as st
import os
ruta_actual = os.path.abspath("prueba.ipynb")
carpeta=os.path.dirname(ruta_actual)
# Cargar la imagen
logo_image = Image.open(carpeta+"/logoia.jpeg")

# Dividir la página en dos columnas (2/3 para la primera columna)
col1, col2 = st.columns([2, 3])
col1.title("Prototipo Myriam asistente")
col2.image(logo_image, width=180)

custom_styles = """
    <style>
        .container {
            display: flex;
            align-items: center;
        }
        .title {
            text-align: center;
            flex: 1;
        }
        .sidebar {
            flex-shrink: 0;
            margin-left: 20px;
        }
    </style>
"""
st.markdown(custom_styles, unsafe_allow_html=True)
st.markdown('<div class="sidebar">', unsafe_allow_html=True)
st.sidebar.image(Image.open(carpeta+"/Imagen1.png"))

def chat():
    st.title("Consulte a la IA")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        if msg["user"]:
            st.text(f"You: {msg['message']}")
        else:
            st.text(msg["message"])
    pregunta = st.text_input("Ingresa tu mensaje:")
    if st.button("Enviar"):
        if pregunta:
            

            #Generacion respuesta modulo preguntas chatgpt
            from langchain.embeddings import HuggingFaceEmbeddings
            from langchain.chat_models import ChatOpenAI
            from langchain.chains.question_answering import load_qa_chain
            import pinecone
            from langchain.vectorstores import Pinecone

            def llamadabase():
                PINECONE_API_KEY = "47b09e36-ecb7-4716-8e29-c472f2a4d9c0"
                PINECONE_ENV = "gcp-starter"
                INDEX_NAME = 'protoch'
                return PINECONE_API_KEY,PINECONE_ENV,INDEX_NAME
            API_PINECONE,AMBIENTE,NOMBRE_BASE=llamadabase()
            pinecone.init(
                    api_key=API_PINECONE,
                    environment=AMBIENTE
            )
                #PARA OBTENER BASE DE DATOS DE PINECONE
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
            Base_conocimiento = Pinecone.from_existing_index(NOMBRE_BASE, embeddings)
                #llm es el modeo de lenguaje cargado el cual utiliza la llave correspondiente al modelo 3.5 solo para texto
            llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key="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")
            chain = load_qa_chain(llm, chain_type="stuff")
            llm.temperature = 0.5
            busqueda_distancia = Base_conocimiento.similarity_search(pregunta, 3) 
            respuesta = chain.run(input_documents=busqueda_distancia, question=pregunta)



            st.session_state.messages.append({"user": True, "message": pregunta})
            st.session_state.messages.append({"user": False, "message": f"Myriam: {respuesta}"})


def carga_archivos():
    st.title("Carga de Nueva Información tecnica")
    uploaded_file = st.file_uploader("Selecciona un archivo", type=["txt", "csv", "xlsx","pdf"])
    if uploaded_file is not None:
        from ModuloDatos import transformar
        transformar(uploaded_file)
        st.success("Archivo cargado exitosamente.")

def Entrega_archivo_predicciones():
    st.title("Ingrese datos a predecir")
    uploaded_file = st.file_uploader("Selecciona un archivo", type=["txt", "csv", "xlsx","pdf"])
    if uploaded_file is not None:
        st.success("Archivo cargado exitosamente.")

seccion_actual = st.sidebar.radio("Seleccionar Sección", ["Consultas tecnicas", "Actualizacion Base tecnica", "Modelos Predictivos"])

# Mostrar la sección correspondiente según el botón seleccionado
if seccion_actual == "Consultas tecnicas":
    chat()
elif seccion_actual == "Actualizacion Base tecnica":
    carga_archivos()
elif seccion_actual == "Modelos Predictivos":
    Entrega_archivo_predicciones()

#Secciones formato paginas 
# import streamlit as st

# def pagina_inicio():
#     st.title("Página de Inicio")
#     st.write("Bienvenido a la página de inicio.")
#     # Puedes agregar contenido adicional para esta sección

# def seccion_uno():
#     st.title("Sección Uno")
#     st.write("Esta es la primera sección.")
#     # Puedes agregar contenido adicional para esta sección

# def seccion_dos():
#     st.title("Sección Dos")
#     st.write("Esta es la segunda sección.")
#     # Puedes agregar contenido adicional para esta sección

# # # Menú de navegación
# # menu = ["Inicio", "Sección Uno", "Sección Dos"]
# # opcion = st.sidebar.selectbox("Selecciona una sección", menu)

# # # Renderizar la sección correspondiente
# # if opcion == "Inicio":
# #     pagina_inicio()
# # elif opcion == "Sección Uno":
# #     seccion_uno()
# # elif opcion == "Sección Dos":
# #     seccion_dos()