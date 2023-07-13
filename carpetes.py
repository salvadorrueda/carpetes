import xml.etree.ElementTree as ET
import os
import sys

def crear_carpetas(directori, ruta_actual=''):
    nom_directori = directori.get('nom')
    ruta_completa = os.path.join(ruta_actual, nom_directori)

    # Crear la carpeta en el sistema de archivos
    try:
        os.makedirs(ruta_completa)
        print(f'Se ha creado la carpeta "{ruta_completa}"')
    except FileExistsError:
        print(f'La carpeta "{ruta_completa}" ya existe')

    # Recorrer los subdirectorios
    for subdirectori in directori.findall('directori'):
        crear_carpetas(subdirectori, ruta_completa)

def interpretar_xml(archivo):
    # Parsear el archivo XML
    tree = ET.parse(archivo)
    root = tree.getroot()

    # Llamar a la función para crear las carpetas
    for directori in root.findall('directori'):
        crear_carpetas(directori)

# Obtener el nombre del archivo XML como argumento de línea de comandos
nombre_archivo = sys.argv[1]

# Llamar a la función para interpretar el XML
interpretar_xml(nombre_archivo)
