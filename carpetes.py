import os
import xml.etree.ElementTree as ET

def crear_carpetes_des_de_xml(ruta_xml):
    # Analitzar el fitxer XML
    tree = ET.parse(ruta_xml)
    root = tree.getroot()

    # Recórrer els elements "directori"
    for directori_elem in root.findall("./directori"):
        nom_directori = directori_elem.get("nom")
        crear_directori(nom_directori)

        # Recórrer els elements "subdirectori" dins de cada "directori"
        for subdirectori_elem in directori_elem.findall("./directori"):
            nom_subdirectori = subdirectori_elem.get("nom")
            crear_directori(os.path.join(nom_directori, nom_subdirectori))

def crear_directori(nom_directori):
    # Comprovar si el directori ja existeix
    if os.path.exists(nom_directori):
        print(f"El directori '{nom_directori}' ja existeix.")
    else:
        # Crear el directori
        os.mkdir(nom_directori)
        print(f"S'ha creat el directori '{nom_directori}'.")

# Ruta del fitxer XML
ruta_xml = "carpetes_M7.xml"

# Cridar la funció per crear les carpetes.
crear_carpetes_des_de_xml(ruta_xml)
