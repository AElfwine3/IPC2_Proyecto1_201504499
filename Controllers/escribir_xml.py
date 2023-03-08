import xml.etree.ElementTree as ET

def escribir_xml(lista_organismo, lista_muestra):

    root = ET.Element("datosMarte")
    listado_organismos = ET.SubElement(root, "listaOrganismos")

    for i in range(lista_organismo.tamano()):
        organismo = lista_organismo.recorrer(i)
        hijo_organismo = ET.SubElement(listado_organismos, "organismo")
        ET.SubElement(hijo_organismo, "codigo").text = organismo.codigo
        ET.SubElement(hijo_organismo, "nombre").text = organismo.nombre
    
    listado_muestras = ET.SubElement(root, "listadoMuestras")

    for i in range(lista_muestra.tamano()):
        muestra = lista_muestra.recorrer(i)
        hijo_muestra = ET.SubElement(listado_muestras, "muestra")
        ET.SubElement(hijo_muestra, "codigo").text = muestra.codigo
        ET.SubElement(hijo_muestra, "descripcion").text = muestra.descripcion
        ET.SubElement(hijo_muestra, "filas").text = str(muestra.filas)
        ET.SubElement(hijo_muestra, "columnas").text = str(muestra.columnas)
        celdas_vivas = ET.SubElement(hijo_muestra, "listadoCeldasVivas")
        for j in range(muestra.listado_celda_viva.tamano()):
            celda_viva = muestra.listado_celda_viva.recorrer(j)
            hijo_celda_viva = ET.SubElement(celdas_vivas, "celdaViva")
            ET.SubElement(hijo_celda_viva, "fila").text = str(celda_viva.fila)
            ET.SubElement(hijo_celda_viva, "columna").text = str(celda_viva.columna)
            ET.SubElement(hijo_celda_viva, "codigoOrganismo").text = celda_viva.codigo_organismo

    tree = ET.ElementTree(root)
    ET.indent(tree, space='\t')
    tree.write("Salida.xml", encoding="utf-8")
