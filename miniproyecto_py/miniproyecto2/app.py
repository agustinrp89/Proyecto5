import requests
from bs4 import BeautifulSoup
import csv

# Definir la URL de la página que deseas raspar
url = "https://www.macworld.com/article/1451512/mejores-maquinas-virtuales-windows-mac.html"

# Hacer una solicitud HTTP GET a la URL
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Crear una instancia de BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Raspar la información deseada de la página
    # Por ejemplo, obtener todos los títulos y enlaces de los artículos
    articulos = soup.find_all("article")

    # Crear un archivo CSV para almacenar los datos
    with open("datos.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Título", "Enlace"])  # Escribir encabezados de columna

        # Iterar sobre los artículos y extraer títulos y enlaces
        for articulo in articulos:
            titulo = articulo.find("h2").text.strip()
            enlace = articulo.find("a")["href"].strip()
            writer.writerow([titulo, enlace])  # Escribir datos en el archivo CSV

    print("Datos raspados y almacenados en datos.csv")
else:
    print("No se pudo acceder a la página:", response.status_code)
