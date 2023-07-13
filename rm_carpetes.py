import os
import xml.etree.ElementTree as ET
import shutil

def eliminar_carpetes_des_de_xml(ruta_xml):
    # Analitzar el fitxer XML
    tree = ET.parse(ruta_xml)
    root = tree.getroot()

    # Recórrer els elements "directori" en ordre invers
    for directori_elem in reversed(root.findall("./directori")):
        nom_directori = directori_elem.get("nom")
        eliminar_directori(nom_directori)

def eliminar_directori(nom_directori):
    # Comprovar si el directori existeix
    if os.path.exists(nom_directori):
        # Eliminar el directori de manera recursiva
        shutil.rmtree(nom_directori)
        print(f"S'ha eliminat el directori '{nom_directori}'.")
    else:
        print(f"El directori '{nom_directori}' no existeix.")

# Ruta del fitxer XML
ruta_xml = "carpetes_M7.xml"

# Cridar la funció per eliminar les carpetes
eliminar_carpetes_des_de_xml(ruta_xml)
