import pandas as pd

# Leer el archivo requirements.txt en un DataFrame
df = pd.read_csv("requirements.txt", delim_whitespace=True, header=None, names=["package", "version"])

# Crear una nueva columna con las dependencias en el formato correcto
df["dependency"] = df["package"] + "==" + df["version"]

# Seleccionar solo la columna "dependency" y guardar en un archivo txt
df["dependency"].to_csv("formatted_requirements.txt", index=False, header=False)

print("Archivo formateado guardado exitosamente.")